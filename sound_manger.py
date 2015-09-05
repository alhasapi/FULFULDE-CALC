
VALID_RANGE = range(10) + range(10, 101, 10) + [1000] 
EXTENTION = ".wav"
AudioDirectory = "sounds/"
AudioLoaded = False

import wave
import pygame

'''
class Node(object):
    _fields = []
    def __init__( self, *args ):
        for (attr, value) in zip( self.__class__._fields, args ):
            setattr(self, attr, value)
'''

class compositeObj:
    def __init__( self, the_file, fname ):
        self.the_file = the_file
        self.fname = fname



dic = { number : compositeObj(wave.open(AudioDirectory + wave_name), wave_name) 
                for (number, wave_name) in zip(VALID_RANGE, 
                                               map(lambda x: str(x) + EXTENTION, VALID_RANGE)) }

dic.update( { "et" : "et.wav" } )

#XXX: Maybe it is a bad idea, probably i'm gonna find a more consice way of it



def is_valid( number ):
    return number in dic.keys()

def _prepare( number ):
    if is_valid( number ):
        return [ number ]

    sv = str(number)
    size = len(sv) - 1
    q = int(sv[0])
    return [ q * ( 10 ** size ) ] + _prepare(int(sv[1:])) 

def regularize_me(item):
    size, sn = len(str(item)), str(item)
    if size in [4, 3]:
        return ( ["1000.wav", "100.wav"][size == 3], sn[0] + EXTENTION )
    return sn + EXTENTION
                

def play(sound_file):
    sound_file = AudioDirectory + sound_file
    pygame.init()
    song = pygame.mixer.Sound(sound_file)
    clock = pygame.time.Clock()
    song.play()
    i = 80
    while i > 0:
        clock.tick(60)
        i -= 1
    pygame.quit()


