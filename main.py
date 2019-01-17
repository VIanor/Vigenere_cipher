# import interface from file
from ginterface import *
from PyQt5 import QtCore, QtGui, QtWidgets
from tkinter import Tk
import time

class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_ValidateCipher()
        self.ui.setupUi(self)
    
        # Events defenition
        self.ui.checkBox.stateChanged.connect(self.ChooseRu)
        self.ui.checkBox_2.stateChanged.connect(self.ChooseEn)
        self.ui.pushButton_3.clicked.connect(self.Copying)

    #logic of widgets                                                             
    def ChooseEn(self, state):
        if state == QtCore.Qt.Checked:
            self.ui.pushButton.clicked.connect(self.EncryptEn)
            self.ui.pushButton_2.clicked.connect(self.DecryptEn)
            self.ui.textEdit.setReadOnly(False)
            self.ui.lineEdit.setReadOnly(False)
    
    def ChooseRu(self, state):
        if state == QtCore.Qt.Checked:
            self.ui.pushButton.clicked.connect(self.EncryptRu)
            self.ui.pushButton_2.clicked.connect(self.DecryptRu)
            self.ui.textEdit.setReadOnly(False)
            self.ui.lineEdit.setReadOnly(False)
    
    @staticmethod
    def KeyGenEn(string, key):
        sum = 0
        for i in range(len(key)):
            sum += ord(key[i])
        i = 1
        while len(key) < len(string):
            key += chr(((sum + i**sum) % 26) + 97)
            i += 1
        return key

    @staticmethod
    def KeyGenRu(string, key):
        sum = 0
        for i in range(len(key)):
            sum += ord(key[i])
        i = 1
        while len(key) < len(string):
            key += chr(((sum + i**sum) % 32) + 1072)
            i += 1
        return key

    def EncryptEn(self):
        word = self.ui.textEdit.toPlainText().lower()
        key = self.ui.lineEdit.text().lower()
        key = MyWin.KeyGenEn(word, key)
        a = 0
        n = 97

        if any([j == ord(word[i]) for j in range(1072, 1104) for i in range(len(word))]):
            self.ui.textEdit_2.setText("Conflict: Invalid message")
            return

        if any([j == ord(key[i]) for j in range(1072, 1104) for i in range(len(word))]):
            self.ui.textEdit_2.setText("Conflict: Invalid key")
            return

        for i in range(len(word)):
            if not any([j == ord(word[i]) for j in range(97, 123)]):
                continue
            if not any([j == ord(key[i]) for j in range(97, 123)]):
                continue
            a = ((ord(word[i]) - n) + (ord(key[i]) - n))
            if a >= 26:
                a = a % 26
            word = word[:i] + chr(a + n) + word[i + 1:len(word)]
        self.ui.textEdit_2.setText(word)
    
    def DecryptEn(self):
        word = self.ui.textEdit.toPlainText().lower()
        key = self.ui.lineEdit.text().lower()
        key = MyWin.KeyGenEn(word, key)
        a = 0
        n = 97

        if any([j == ord(word[i]) for j in range(1072, 1104) for i in range(len(word))]):
            self.ui.textEdit_2.setText("Conflict: Invalid cipher")
            return

        if any([j == ord(key[i]) for j in range(1072, 1104) for i in range(len(word))]):
            self.ui.textEdit_2.setText("Conflict: Invalid key")
            return

        for i in range(len(word)):
            if not any([j == ord(word[i]) for j in range(97, 123)]):
                continue
            if not any([j == ord(key[i]) for j in range(97, 123)]):
                continue
            a = ((ord(word[i])-n)-(ord(key[i])-n))
            if a < 0:
                a += 26
            word = word[:i] + chr(a+n) + word[i+1:len(word)]
        self.ui.textEdit_2.setText(word)
    
    def EncryptRu(self):
        word = self.ui.textEdit.toPlainText().lower()
        key = self.ui.lineEdit.text().lower()
        key = MyWin.KeyGenRu(word, key)
        a = 0
        n = 1072

        if any([j == ord(word[i]) for j in range(97, 123) for i in range(len(word))]):
            self.ui.textEdit_2.setText("Conflict: Invalid message")
            return

        if any([j == ord(key[i]) for j in range(97, 123) for i in range(len(word))]):
            self.ui.textEdit_2.setText("Conflict: Invalid key")
            return

        for i in range(len(word)):
            if not any([j == ord(word[i]) for j in range(1072, 1104)]):
                continue
            if not any([j == ord(key[i]) for j in range(1072, 1104)]):
                continue
            a = ((ord(word[i]) - n) + (ord(key[i]) - n))
            if a >= 32:
                a = a % 32
            word = word[:i] + chr(a + n) + word[i + 1:len(word)]
        self.ui.textEdit_2.setText(word)
    
    def DecryptRu(self):
        word = self.ui.textEdit.toPlainText().lower()
        key = self.ui.lineEdit.text().lower()
        key = MyWin.KeyGenRu(word, key)
        a = 0
        n = 1072

        if any([j == ord(word[i]) for j in range(97, 123) for i in range(len(word))]):
            self.ui.textEdit_2.setText("Conflict: Invalid cipher")
            return

        if any([j == ord(key[i]) for j in range(97, 123) for i in range(len(word))]):
            self.ui.textEdit_2.setText("Conflict: Invalid key")
            return

        for i in range(len(word)):
            if not any([j == ord(word[i]) for j in range(1072, 1104)]):
                continue
            if not any([j == ord(key[i]) for j in range(1072, 1104)]):
                continue
            a = ((ord(word[i]) - n) - (ord(key[i]) - n))
            if a < 0:
                a += 32
            word = word[:i] + chr(a + n) + word[i + 1:len(word)]
        self.ui.textEdit_2.setText(word)

    def Copying(self):
        string = self.ui.textEdit_2.toPlainText()
        r = Tk()
        r.withdraw()
        r.clipboard_clear()
        r.clipboard_append(string)

        r.update()
        time.sleep(.2)
        r.update()

        r.destroy()

        self.ui.textEdit_2.setText("")
        self.ui.textEdit.setText("")

if __name__=="__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ValidateCipher = MyWin()
    ValidateCipher.show()
    sys.exit(app.exec_())
