import wave
import pygame

VALID_RANGE = range(10) + range(10, 101, 10) + [1000] 
EXTENTION = ".wav"
PREFIX = "et.wav"
AudioDirectory = "sounds/"
AudioLoaded = False
OPERATORS = ["+" , "-" , "*" , "/" ]

class compositeObj:
    def __init__( self, the_file, fname ):
        self.the_file = the_file
        self.fname = fname



dic = { number: compositeObj(wave.open(AudioDirectory + wave_name), wave_name) 
                for (number, wave_name) in zip(VALID_RANGE, 
                                               map(lambda x: str(x) + EXTENTION, VALID_RANGE)) }

dic.update( { 
                "et" : "et.wav",
                "+" : "plus.wav",
                "-" : "moin.wav",
                "*" : "sowa.wav",
                "/" : "div.wav"
            } 
        )

def is_valid( number ):
    sn = str(number)
    return (number in dic.keys() or
            (len(sn) in [4, 3] and sn[0] != '1' and sn[1:] in ["00", "000"]))

def regularize_me(item):
    size, sn = len(str(item)), str(item)
    if size in [4, 3] and sn[0] != '1':
        return ( ["1000.wav", "100.wav"][size == 3], sn[0] + EXTENTION )
    return sn + EXTENTION

def partition(items):
    tups = []
    others = []
    for each in items:
        if isinstance(each, tuple):
            tups.append(each)
        else:
            others.append(each)
    return  tups, others

#def recpart(items):
#    if not items:
#        return [ [], [] ]
#    if len(items) == 1:
#        if isinstance(items[0], tuple):
#            return [ [ items[0] ], [] ]
#        return [ [], items[0] ]
#
#    if len(items) == 2:
#        return [ 
#                [[ items[0] ], [ items[1] ] ],
#                [[ items[1] ], [ items[0] ] ],
#                ][ not isinstance(items[1], tuple) ]
#    else: pass

def _prepare( number ):
    if is_valid( number ):
        return [ number ]

    sv = str(number)
    size = len(sv) - 1
    q = int(sv[0])
    return [ q * ( 10 ** size ) ] + _prepare(int(sv[1:]))


def recjoin(items, sep):
    if len(items) == 1:
        return items
    if len(items) == 2:
        return [items[0], sep, items[1]]
    else:
        return [items[0], sep, items[1]] + [sep] + recjoin(items[2:], sep)

def myJoin(items, sep):
    out = []
    for q in items:
        if q != items[-1]:
            out.append(q)
            out.append(sep)
        else:
            out.append(q)
    return out


def play2(number):
    if number in VALID_RANGE:
        return play(str(number) + EXTENTION)

    if number in OPERATORS:
        return play(dic[number])

    items = map(regularize_me, _prepare(number))
    items = myJoin(items, PREFIX)
    '''
    empty = lambda q: q == ['']
    tups, others = partition(items)

    items = (tups + ( [] if len(tups) == 1 
                        else ["et.wav"] )

                  + ( [] if empty(others) 
                        else PREFIX.join(others).split('-') ))
    '''
    return map(lambda q: play(q) 
        if not isinstance(q, tuple) 
               else (play(q[0]), play(q[1])), items)


def play(sound_file, limit=60):
    sound_file = AudioDirectory + sound_file
    pygame.init()
    song = pygame.mixer.Sound(sound_file)
    clock = pygame.time.Clock()
    song.play()
    i = limit
    while i > 0:
        clock.tick(limit)
        i -= 1
    pygame.quit()
