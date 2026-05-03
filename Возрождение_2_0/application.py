from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPalette, QBrush, QPixmap
from baza import Ui_Window_revival
from o_nas import Ui_Window_onax
from Turistichescay_baza import Ui_Window_turBaz
from Turistichescay_marshrut import Ui_Window_turMar
from found import Ui_Window_found
from aubook import Ui_Window_aubook
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl
import sys
import webbrowser
from PyQt5.QtWinExtras import QWinTaskbarButton,QWinTaskbarProgress
from PyQt5.QtWinExtras import QtWin                                         #  !!!
     


import sys, os
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, \
                            QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.window_width, self.window_height = 800, 120
        self.setFixedSize(self.window_width, self.window_height)
        self.setStyleSheet("background-color: rgb(239, 182, 111);")
        self.setWindowTitle("Возрождение - аудиогид")

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        btn = QPushButton('Play', clicked=self.playAudioFile)
        btn.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.layout.addWidget(btn)

        volumeControl = QHBoxLayout()
        self.layout.addLayout(volumeControl)

        btnVolumeUp = QPushButton('+', clicked=self.volumeUp)
        btnVolumeUp.setStyleSheet("background-color: rgb(255, 255, 255);")
        btnVolumeDown = QPushButton('-', clicked=self.volumeDown)
        btnVolumeDown.setStyleSheet("background-color: rgb(255, 255, 255);")
        butVolumeMute = QPushButton('Mute', clicked=self.volumeMute)
        butVolumeMute.setStyleSheet("background-color: rgb(255, 255, 255);")
        volumeControl.addWidget(btnVolumeUp)
        volumeControl.addWidget(butVolumeMute)
        volumeControl.addWidget(btnVolumeDown)

        self.player = QMediaPlayer()

    def volumeUp(self):
        currentVolume = self.player.volume() # 
        print(currentVolume)
        self.player.setVolume(currentVolume + 5)

    def volumeDown(self):
        currentVolume = self.player.volume() # 
        print(currentVolume)
        self.player.setVolume(currentVolume - 5)

    def volumeMute(self):
        self.player.setMuted(not self.player.isMuted())

    def playAudioFile(self):
        full_file_path = os.path.join(os.getcwd(), 'audio.wav')
        url = QUrl.fromLocalFile(full_file_path)
        content = QMediaContent(url)

        self.player.setMedia(content)
        self.player.play()

        
class My_Ui_Window_found(QtWidgets.QMainWindow, Ui_Window_found):
    def __init__(self, parent=None):
        super(My_Ui_Window_found, self).__init__(parent=parent)
        self.setupUi(self)

        self.palette = QPalette()
        self.palette.setBrush(QPalette.Background, QBrush(QPixmap("./f3.jpg")))
        self.setPalette(self.palette)

        self.b_clear.clicked.connect(lambda: webbrowser.open('https://cleanarctic.ru/'))
        self.b_arct.clicked.connect(lambda: webbrowser.open('https://arctic-resources.ru/'))
        self.b_v.clicked.connect(lambda: webbrowser.open('http://www.sberbank.ru/ru/person'))
        
class My_Ui_Window_aubook(QtWidgets.QMainWindow, Ui_Window_aubook):
    def __init__(self, parent=None):
        super(My_Ui_Window_aubook, self).__init__(parent=parent)
        self.setupUi(self)
        
        self.palette = QPalette()
        self.palette.setBrush(QPalette.Background, QBrush(QPixmap("./чувкарыч.jpg")))
        self.setPalette(self.palette)

        self.pushButton.clicked.connect(self.on_clicked_aubook)

    def on_clicked_aubook(self):
        self.basic = MyApp()
        self.basic.show()
        


class My_Ui_Window_turMar(QtWidgets.QMainWindow, Ui_Window_turMar):
    def __init__(self, parent=None):
        super(My_Ui_Window_turMar, self).__init__(parent=parent)
        self.setupUi(self)
        
        self.palette = QPalette()
        self.palette.setBrush(QPalette.Background, QBrush(QPixmap("./karf1.png")))
        self.setPalette(self.palette)


class My_Ui_Window_turBaz(QtWidgets.QMainWindow, Ui_Window_turBaz):
    def __init__(self, parent=None):
        super(My_Ui_Window_turBaz, self).__init__(parent=parent)
        self.setupUi(self)

        self.palette = QPalette()
        self.palette.setBrush(QPalette.Background, QBrush(QPixmap("./ежик.jpg")))
        self.setPalette(self.palette)


class My_Ui_Window_onax(QtWidgets.QMainWindow, Ui_Window_onax):
    def __init__(self, parent=None):
        super(My_Ui_Window_onax, self).__init__(parent=parent)
        self.setupUi(self)

        self.setStyleSheet("background-color: rgb(239, 182, 111);")
        

class My_Ui_Window_revival(QtWidgets.QMainWindow, Ui_Window_revival):
    def __init__(self, parent=None):
        super(My_Ui_Window_revival, self).__init__(parent=parent)
        self.setupUi(self)

        self.palette = QPalette()
        self.palette.setBrush(QPalette.Background, QBrush(QPixmap("./f1.jpg")))
        self.setPalette(self.palette)

        self.b_oNax.clicked.connect(self.on_clicked_oNax)
        self.b_turBaz.clicked.connect(self.on_clicked_turbaz)
        self.b_turMar.clicked.connect(self.on_clicked_turMar)
        self.b_aubook.clicked.connect(self.on_clicked_aubook)
        self.b_fond.clicked.connect(self.on_clicked_fond)

    def on_clicked_oNax(self):
        self.basic = My_Ui_Window_onax()
        self.basic.show()

    def on_clicked_turbaz(self):
        self.basic = My_Ui_Window_turBaz()
        self.basic.show()

    def on_clicked_turMar(self):
        self.basic = My_Ui_Window_turMar()
        self.basic.show()

    def on_clicked_aubook(self):
        self.basic = My_Ui_Window_aubook()
        self.basic.show()

    def on_clicked_fond(self):
        self.basic = My_Ui_Window_found()
        self.basic.show()



if __name__ == "__main__":
    myappid = 'mycompany.myproduct.subproduct.version'                          #  !!!
    QtWin.setCurrentProcessExplicitAppUserModelID(myappid)
    
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('лого2.png'))
    
    window = My_Ui_Window_revival()
    window.setWindowIcon(QtGui.QIcon('лого2.png'))
    window.show()

    window.taskbar_button = QWinTaskbarButton()
    window.taskbar_button.setWindow(window.windowHandle())
    window.taskbar_button.setOverlayIcon(QtGui.QIcon('лого2.png'))
    
    sys.exit(app.exec_())
