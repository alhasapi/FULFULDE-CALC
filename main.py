# -*- coding: utf-8 -*-


from __future__ import division
from copy import deepcopy
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from sound_manager import *
import sys
import pyglet


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

evaluer = eval


class Ui_Form(QtGui.QMainWindow):
    def __init__(self, Form, parent=None):
        super(Ui_Form, self).__init__(parent)
        self.pushButton = QtGui.QPushButton(Form)
        
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_3 = QtGui.QPushButton(Form)
        self.pushButton_4 = QtGui.QPushButton(Form)
        self.pushButton_5 = QtGui.QPushButton(Form)
        self.pushButton_6 = QtGui.QPushButton(Form)
        self.pushButton_7 = QtGui.QPushButton(Form)
        self.pushButton_8 = QtGui.QPushButton(Form)
        self.pushButton_9 = QtGui.QPushButton(Form)
        self.pushButton_10 = QtGui.QPushButton(Form)
        self.pushButton_11 = QtGui.QPushButton(Form)
        self.pushButton_12 = QtGui.QPushButton(Form)
        self.pushButton_13 = QtGui.QPushButton(Form)
        self.pushButton_14 = QtGui.QPushButton(Form)
        self.pushButton_15 = QtGui.QPushButton(Form)
        self.pushButton_16 = QtGui.QPushButton(Form)
        self.pushButton_17 = QtGui.QPushButton(Form)
        self.pushButton_18 = QtGui.QPushButton(Form)
        self.pushButton_19 = QtGui.QPushButton(Form)
        self.pushButton_20 = QtGui.QPushButton(Form)

        self.checkBox = QtGui.QCheckBox(Form)
        self.checkBox.setChecked(True) 
        self.line = QtGui.QFrame(Form)
        self.plain = QtGui.QPlainTextEdit(Form)

        self.current_buffer = ""
        self.global_inputs = ""
        self.voice_is_active = True

        self.connect(self.pushButton, SIGNAL("clicked()"), self.clicked)
        self.connect(self.pushButton_2, SIGNAL("clicked()"), self.clicked)
        self.connect(self.pushButton_3, SIGNAL("clicked()"), self.clicked)
        self.connect(self.pushButton_4, SIGNAL("clicked()"), self.clicked)
        self.connect(self.pushButton_5, SIGNAL("clicked()"), self.clicked)
        self.connect(self.pushButton_6, SIGNAL("clicked()"), self.clicked)
        self.connect(self.pushButton_7, SIGNAL("clicked()"), self.clicked)
        self.connect(self.pushButton_8, SIGNAL("clicked()"), self.clicked)
        self.connect(self.pushButton_9, SIGNAL("clicked()"), self.clicked)
        self.connect(self.pushButton_10, SIGNAL("clicked()"), self.clicked)
        self.connect(self.pushButton_11, SIGNAL("clicked()"), self.clicked)
        self.connect(self.pushButton_12, SIGNAL("clicked()"), self.clicked)
        self.connect(self.pushButton_13, SIGNAL("clicked()"), self.clicked)
        self.connect(self.pushButton_14, SIGNAL("clicked()"), self.clicked)
        self.connect(self.pushButton_15, SIGNAL("clicked()"), self.eq_clicked)
        self.connect(self.pushButton_16, SIGNAL("clicked()"), self.m_clicked)
        self.connect(self.pushButton_17, SIGNAL("clicked()"), self.ce_clicked)
        self.connect(self.pushButton_18, SIGNAL("clicked()"), self.del_clicked)
        self.connect(self.pushButton_19, SIGNAL("clicked()"), self.parent_clicked)
        self.connect(self.checkBox, SIGNAL("clicked()"), self.check_box_clicked)
        self.connect(self.pushButton_20, SIGNAL("clicked()"), self.mr_clicked)


    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(331, 265)

        self.pushButton.setGeometry(QtCore.QRect(10, 120, 51, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2.setGeometry(QtCore.QRect(70, 120, 51, 27))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3.setGeometry(QtCore.QRect(130, 120, 51, 27))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4.setGeometry(QtCore.QRect(10, 150, 51, 27))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_5.setGeometry(QtCore.QRect(70, 150, 51, 27))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.pushButton_6.setGeometry(QtCore.QRect(130, 150, 51, 27))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.pushButton_7.setGeometry(QtCore.QRect(10, 180, 51, 27))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.pushButton_8.setGeometry(QtCore.QRect(70, 180, 51, 27))
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.pushButton_9.setGeometry(QtCore.QRect(130, 180, 51, 27))
        self.pushButton_9.setObjectName(_fromUtf8("pushButton_9"))
        self.pushButton_10.setGeometry(QtCore.QRect(70, 210, 51, 27))
        self.pushButton_10.setObjectName(_fromUtf8("pushButton_10"))
        self.pushButton_11.setGeometry(QtCore.QRect(210, 150, 51, 27))
        self.pushButton_11.setObjectName(_fromUtf8("pushButton_11"))
        self.pushButton_12.setGeometry(QtCore.QRect(210, 120, 51, 27))
        self.pushButton_12.setObjectName(_fromUtf8("pushButton_12"))
        self.pushButton_13.setGeometry(QtCore.QRect(270, 150, 51, 27))
        self.pushButton_13.setObjectName(_fromUtf8("pushButton_13"))
        self.pushButton_14.setGeometry(QtCore.QRect(270, 120, 51, 27))
        self.pushButton_14.setObjectName(_fromUtf8("pushButton_14"))
        self.pushButton_15.setGeometry(QtCore.QRect(210, 180, 51, 27))
        self.pushButton_15.setObjectName(_fromUtf8("pushButton_15"))
        self.pushButton_16.setGeometry(QtCore.QRect(270, 180, 51, 27))
        self.pushButton_16.setObjectName(_fromUtf8("pushButton_16"))
        self.pushButton_17.setGeometry(QtCore.QRect(270, 90, 51, 27))
        self.pushButton_17.setObjectName(_fromUtf8("pushButton_17"))
        self.pushButton_18.setGeometry(QtCore.QRect(210, 90, 51, 27))
        self.pushButton_18.setObjectName(_fromUtf8("pushButton_18"))
        self.pushButton_19.setGeometry(QtCore.QRect(270, 210, 51, 27))
        self.pushButton_19.setObjectName(_fromUtf8("pushButton_19")) 
        self.pushButton_20.setGeometry(QtCore.QRect(210, 210, 51, 27))

        self.line.setGeometry(QtCore.QRect(180, 120, 20, 121))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.checkBox.setGeometry(QtCore.QRect(20, 90, 121, 22))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.plain.setGeometry(QtCore.QRect(10, 10, 301, 41))
        self.plain.setObjectName(_fromUtf8("plain"))
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        
    def afficher(self, smthg):
        self.plain.setPlainText(smthg)

    def parent_clicked(self):
        expr = str(self.global_inputs)
        expr = "(" + expr + ")"
        self.global_inputs = expr
        self.afficher(self.global_inputs)

    def del_clicked(self):
        expr = self.global_inputs
        expr = str(expr).split()
        self.global_inputs = ' '.join(expr[:-1])
        play("wila.wav")
        self.afficher(self.global_inputs)

    def check_box_clicked(self):
        if self.voice_is_active:
            self.voice_is_active = False
        else:
            self.voice_is_active = True

    def error(self):
        if self.voice_is_active:
            play("error.wav")
        self.ce_clicked()
        self.afficher("ERREUR")
 
    def eq_clicked(self):
        is_float = lambda q: '.' in q 
        try:
            resultat = evaluer(str(self.global_inputs)) 
        except:
            self.error()
            return
        
        resultat, q =  str(resultat), resultat
        if is_float(resultat) and self.voice_is_active:
            self.error()
            return

        self.afficher(QString(resultat))
        if self.voice_is_active:
            play("eq.wav")
            play2(q)

    def m_clicked(self):
        self.current_buffer = self.global_inputs
        '''
        if not self.current_buffer.empty:
            self.current_buffer.empty = False
        else:
            self.global_inputs += self.current_buffer.a
        '''

    def mr_clicked(self):
        self.global_inputs += self.current_buffer
        self.global_inputs = str(evaluer(str(self.global_inputs)))
        self.afficher(self.global_inputs)

    def ce_clicked(self):
        self.global_inputs = ""
        self.afficher(self.global_inputs)

    def clicked(self):
        button = self.sender()
        self.prepare(button)

    def prepare(self, button):
        is_an_operator = lambda q: q in ["+", "-", "*", "/"]
        if button is None or not isinstance(button, QPushButton): 
            return
        text = button.text()
        self.global_inputs += (" " + text + " " if is_an_operator(text) else text)
        self.afficher(self.global_inputs)

        if self.voice_is_active:
            n = button.text() 
            play2(int(n) if not is_an_operator(n) else str(n))

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.pushButton.setText(_translate("Form", "1", None))
        self.pushButton_2.setText(_translate("Form", "2", None))
        self.pushButton_3.setText(_translate("Form", "3", None))
        self.pushButton_4.setText(_translate("Form", "4", None))
        self.pushButton_5.setText(_translate("Form", "5", None))
        self.pushButton_6.setText(_translate("Form", "6", None))
        self.pushButton_7.setText(_translate("Form", "7", None))
        self.pushButton_8.setText(_translate("Form", "8", None))
        self.pushButton_9.setText(_translate("Form", "9", None))
        self.pushButton_10.setText(_translate("Form", "0", None))
        self.pushButton_11.setText(_translate("Form", "*", None))
        self.pushButton_12.setText(_translate("Form", "+", None))
        self.pushButton_13.setText(_translate("Form", "/", None))
        self.pushButton_14.setText(_translate("Form", "-", None))
        self.pushButton_15.setText(_translate("Form", "=", None))
        self.pushButton_16.setText(_translate("Form", "M", None))
        self.pushButton_17.setText(_translate("Form", "CE", None))
        self.pushButton_18.setText(_translate("Form", "Del", None))
        self.pushButton_19.setText(_translate("Form", "()", None))
        self.pushButton_20.setText(_translate("Form", "MR", None))
        self.checkBox.setText(_translate("Form", "Voix", None))

class myWin(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Form(self)
        self.ui.setupUi(self)

    def keyPressEvent(self, event):
        if type(event) == QtGui.QKeyEvent:
            key = event.key()
            fn = lambda q: eval("QtCore.Qt.%s" % q)
            operators_keys = map(fn,  ['Key_multiply',
                                      'Key_Plus',
                                      'Key_division',
                                      'Key_Minus',
                                      'Key_Return',
                                      'Key_Backspace'])
                                      

            Keys = ["Key_%s" %i for i in range(10)]
            key_list = map(fn, Keys)
            if key in key_list:
                dc = dict(zip(key_list, [ self.ui.pushButton_10, 
                                          self.ui.pushButton, 
                                          self.ui.pushButton_2,
                                          self.ui.pushButton_3, 
                                          self.ui.pushButton_4, 
                                          self.ui.pushButton_5,
                                          self.ui.pushButton_6, 
                                          self.ui.pushButton_7, 
                                          self.ui.pushButton_8,
                                          self.ui.pushButton_9 ]))

                self.ui.prepare(dc[key])
            elif key in operators_keys:
                dc = dict(zip(operators_keys, [ self.ui.pushButton_11,
                                                self.ui.pushButton_12,
                                                self.ui.pushButton_13,
                                                self.ui.pushButton_14 ]))
                if dc.has_key(key):
                    self.ui.prepare(dc[key])
                else:
                    if key == QtCore.Qt.Key_Return:
                        self.ui.eq_clicked()
                    elif key == QtCore.Qt.Key_Backspace:
                        self.ui.del_clicked()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    mainW = myWin()
    mainW.show()
    sys.exit(app.exec_())

