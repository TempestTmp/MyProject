from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPalette, QBrush, QPixmap
import sys



class Window_preview(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(900, 600)
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 200, 900, 50))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(300, 260, 271, 101))
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255, 0);")
        
        self.pushButton.setObjectName("pushButton")
        #MainWindow.setCentralWidget(self.centralwidget)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Простые шифры"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">   Простые шифры</span></p></body></html>"))
        #self.pushButton.setText(_translate("MainWindow", "Начать"))


        
class Window_basic(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(900, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 110, 581, 30))
        self.label.setObjectName("label")
        self.btn_cezar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_cezar.setGeometry(QtCore.QRect(340, 300, 231, 71))
        self.btn_cezar.setStyleSheet("background-color: rgb(255, 255, 255, 0);")
        self.btn_cezar.setObjectName("btn_cezar")
        self.btn_afin = QtWidgets.QPushButton(self.centralwidget)
        self.btn_afin.setGeometry(QtCore.QRect(350, 370, 221, 71))
        self.btn_afin.setObjectName("btn_afin")
        self.btn_afin.setStyleSheet("background-color: rgb(255, 255, 255, 0);")
        #MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Простые Шифры"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Простые шифры</span></p></body></html>"))
        #self.btn_cezar.setText(_translate("MainWindow", "Шифр Цезаря"))
        #self.btn_afin.setText(_translate("MainWindow", "Мультипликативный шифр"))




class Window_afin(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(900, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(255, 255, 255, 0);")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setStyleSheet("QTabWidget::pane\n"
"{\n"
"    border: 1px;\n"
"    background: rgb(0, 0, 0, 0);\n"
"}\n"
"\n"
"QTabBar::tab\n"
"{\n"
"    background: rgb(98, 30, 37);\n"
"}\n"
"\n"
"QTabBar::tab:selected\n"
"{\n"
"    background: rgb(89, 52, 85);\n"
"}")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.tab)
        self.textBrowser.setStyleSheet("background-color: rgb(255, 255, 255, 0);")
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_2.addWidget(self.textBrowser)
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../Мультипликативный шифр.png"))
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2, 0, QtCore.Qt.AlignHCenter)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.tab_2)
        self.textBrowser_2.setStyleSheet("background-color: rgb(255, 255, 255, 0);")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.verticalLayout_3.addWidget(self.textBrowser_2)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tab_4)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.lineEdit = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255, 0);")
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_5.addWidget(self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255, 0);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_5.addWidget(self.lineEdit_2)
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_2.setStyleSheet("background-color: rgba(255, 172, 168, 175);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_5.addWidget(self.pushButton_2)
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.tab_4)
        self.textBrowser_5.setStyleSheet("background-color: rgb(255, 255, 255, 0);")
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.verticalLayout_5.addWidget(self.textBrowser_5)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_3.setStyleSheet("background-color: rgb(255, 255, 255, 0);")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout_4.addWidget(self.lineEdit_3)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_4.setStyleSheet("background-color: rgb(255, 255, 255, 0);")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout_4.addWidget(self.lineEdit_4)
        self.pushButton = QtWidgets.QPushButton(self.tab_3)
        self.pushButton.setStyleSheet("background-color: rgb(255, 172, 168, 175);\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_4.addWidget(self.pushButton)
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.tab_3)
        self.textBrowser_4.setStyleSheet("background-color: rgb(255, 255, 255, 0);")
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.verticalLayout_4.addWidget(self.textBrowser_4)
        self.tabWidget.addTab(self.tab_3, "")
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Простые Шифры - Мультипликативный шифр"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#ffaca8;\">Мультипликативный шифр</span></p></body></html>"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; color:#ffaca8;\">В мультипликативном шифре алгоритм шифрования применяет умножение исходного текста ключом, а алгоритм дешифрования применяет деление зашифрованного текста ключом, т.е. умножение на мультипликативную инверсию ключа. Именно поэтому он называется мультипликативным.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt; color:#ffaca8;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; color:#ffaca8;\">Мультипликативная инверсия означает, что ключ должен принадлежать набору Zn, например: пусть  мультипликативная инверсия a, это b, тогда (a * b) mod n = 1. Записывается это так a</span><span style=\" font-size:16pt; color:#ffaca8; vertical-align:super;\">-1</span><span style=\" font-size:16pt; color:#ffaca8;\"> = b. Для сокращения запишем: (a, b).</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Описание"))
        self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#ffaca8;\">Шифрование:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt; color:#ffaca8;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#ffaca8;\">В мультипликативном шифре шифрование происходит по формуле n</span><span style=\" font-size:14pt; color:#ffaca8; vertical-align:sub;\">new</span><span style=\" font-size:14pt; color:#ffaca8;\"> = (n * k) mod 26.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt; color:#ffaca8;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#ffaca8;\">Пример:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#ffaca8;\">Мы используем мультипликативный шифр, чтобы зашифровать сообщение &quot;hello&quot; с ключом (7, 16). Сообщение написано на англиском языке, значит используем английский алфавит.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt; color:#ffaca8;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#ffaca8;\">АЛФАВИТ -  A B C D E F G H I J K L M N O P Q R S T U V W X Y Z</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#ffaca8;\">Пронумеруем буквы A-0, B-1 C-2, D-3... Z-25. Теперь берем буквы из сообщения, смотрим на их номер(n), вспоминаем ключ(k) и считаем номер новой буквы(n</span><span style=\" font-size:14pt; color:#ffaca8; vertical-align:sub;\">new</span><span style=\" font-size:14pt; color:#ffaca8;\">) </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#ffaca8;\">по форуле n</span><span style=\" font-size:14pt; color:#ffaca8; vertical-align:sub;\">new</span><span style=\" font-size:14pt; color:#ffaca8;\"> = (n * k) mod 26.  </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#ffaca8;\">Считаем:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#ffaca8; vertical-align:sub;\">                                                 n                                  (n * k) mod 26                                       n1  </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#ffaca8;\">Исходный текст h -&gt; 07 Шифрование(07 x 07) mod 26 -&gt; Шифр. 23 X</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#ffaca8;\">Исходный текст e -&gt; 04 Шифрование(04 x 07) mod 26 -&gt; Шифр. 02 C</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#ffaca8;\">Исходный текст l -&gt;  11 Шифрование(11 x 07) mod 26 -&gt; Шифр. 25 Z</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#ffaca8;\">Исходный текст l -&gt;  11 Шифрование(11 x 07) mod 26 -&gt; Шифр. 25 Z</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#ffaca8;\">Исходный текст o -&gt; 14 Шифрование(14 x 07) mod 26 -&gt; Шифр. 20 U</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt; color:#ffaca8;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#ffaca8;\">Зашифрованный текст &quot;XCZZU&quot;.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt; color:#ffaca8;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt; color:#ffaca8;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#ffaca8;\">Расшифровование:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#ffaca8;\">В мультипликативном шифре шифрование происходит по формуле  (n</span><span style=\" font-size:14pt; color:#ffaca8; vertical-align:sub;\">new</span><span style=\" font-size:14pt; color:#ffaca8;\"> * k</span><span style=\" font-size:14pt; color:#ffaca8; vertical-align:super;\">-1</span><span style=\" font-size:14pt; color:#ffaca8;\">) mod 26 = n.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt; color:#ffaca8;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#ffaca8;\">Пример:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#ffaca8;\">У нас есть зашифрованное мультипликативны шифром сообщение &quot;XCZZU&quot; с ключом (7, 16). Сообщение написано на англиском языке, значит используем английский алфавит.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt; color:#ffaca8;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#ffaca8;\">АЛФАВИТ -  A B C D E F G H I J K L M N O P Q R S T U V W X Y Z</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt; color:#ffaca8;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#ffaca8;\">Нумеруем буквы A-0, B-1 C-2, D-3... Z-25. Теперь берем буквы из зашифрованного сообщения, смотрим на их номер(n</span><span style=\" font-size:14pt; color:#ffaca8; vertical-align:sub;\">new</span><span style=\" font-size:14pt; color:#ffaca8;\">), вспоминаем ключ(k</span><span style=\" font-size:14pt; color:#ffaca8; vertical-align:super;\">-1</span><span style=\" font-size:14pt; color:#ffaca8;\">) и считаем исходной буквы(n) </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#ffaca8;\">по форуле n = (n</span><span style=\" font-size:14pt; color:#ffaca8; vertical-align:sub;\">new</span><span style=\" font-size:14pt; color:#ffaca8;\"> * k</span><span style=\" font-size:14pt; color:#ffaca8; vertical-align:super;\">-1</span><span style=\" font-size:14pt; color:#ffaca8;\">) mod 26.  </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#ffaca8;\">Считаем:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt; color:#ffaca8;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#ffaca8;\">Зашифр. текст X -&gt; 23 Шифрование(23 x 16) mod 26 -&gt; Шифр. 07 h</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#ffaca8;\">Зашифр. текст C -&gt; 02 Шифрование(02 x 16) mod 26 -&gt; Шифр. 04 e</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#ffaca8;\">Зашифр. текст Z -&gt; 25 Шифрование(25 x 16) mod 26 -&gt; Шифр. 11 l</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#ffaca8;\">Зашифр. текст Z -&gt; 25 Шифрование(25 x 16) mod 26 -&gt; Шифр. 11 l</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#ffaca8;\">Зашифр. текст U -&gt; 20 Шифрование(20 x 16) mod 26 -&gt; Шифр. 14 o</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt; color:#ffaca8;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#ffaca8;\">Исходный текст &quot;hello&quot;.</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Принцип работы"))
        self.pushButton_2.setText(_translate("MainWindow", "Зашифровать"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Зашифровать"))
        self.pushButton.setText(_translate("MainWindow", "Расшифровать"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Взломать"))


        
class Window_cezar(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(900, 600)
        MainWindow.setStyleSheet("QLabel\n"
"{\n"
"    color: rgb(93, 206, 204)\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(255, 255, 255, 0);")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setMaximumSize(QtCore.QSize(882, 16777215))
        self.tabWidget.setStyleSheet("QTabWidget::pane\n"
"{\n"
"    border: 1px;\n"
"    background: rgb(0, 0, 0, 0);\n"
"}\n"
"\n"
"QTabBar::tab\n"
"{\n"
"    background: rgb(25, 128, 139);\n"
"}\n"
"\n"
"QTabBar::tab:selected\n"
"{\n"
"    background: rgb(45, 69, 93)\n"
"}")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.tab)
        self.textBrowser.setStyleSheet("")
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_2.addWidget(self.textBrowser)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.tab_2)
        self.textBrowser_2.setStyleSheet("")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.verticalLayout_3.addWidget(self.textBrowser_2)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tab_4)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.lineEdit = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit.setStyleSheet("border-color: rgb(93, 206, 204);")
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_5.addWidget(self.lineEdit)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout_5.addWidget(self.lineEdit_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_2.setStyleSheet("background-color: rgb(93, 206, 204, 175);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_5.addWidget(self.pushButton_2)
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.tab_4)
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.verticalLayout_5.addWidget(self.textBrowser_5)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_4.addWidget(self.lineEdit_2)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout_4.addWidget(self.lineEdit_4)
        self.pushButton = QtWidgets.QPushButton(self.tab_3)
        self.pushButton.setStyleSheet("background-color: rgb(93, 206, 204, 175);")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_4.addWidget(self.pushButton)
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.tab_3)
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.verticalLayout_4.addWidget(self.textBrowser_4)
        self.tabWidget.addTab(self.tab_3, "")
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Простые Шифры - Шифр Цезаря"))
        self.label.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; color:#9bffff;\">Шифр цезаря</span></p></body></html>"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#9bffff;\">Название шифра уже указывает на его создателя, Гая Юлия Цезаря, использовавшего такую схему в переписках с военными командирами. На войне часто случались кражи писем, особенно написанные важными лицами, поэтому союзникам требовалась своя защита против утечки информации. Получив сообщение с непонятным содержанием, враги не могли рассекретить планы римского полководца и помешать ему. Такое простое, но гениальное изобретение играло большую роль, так как образованных людей раньше было мало, и расшифровать текст никто не мог. Бывали даже догадки, что Цезарь писал на другом языке, неизвестном никому.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; color:#9bffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#9bffff;\">Ключ к шифру Юлий постоянно менял, еще больше путая перехватчиков, но самым популярным было смещение алфавита на 3 буквы. Об этом пишет Гай Светоний Транквилл: «Если у него было что-либо конфиденциальное для передачи, то он записывал это шифром, то есть так изменял порядок букв алфавита, что нельзя было разобрать ни одно слово. Если кто-либо хотел дешифровать его и понять его значение, то он должен был подставлять четвертую букву алфавита, а именно, D, для A, и так далее, с другими буквами». (Данные из первой книги «Жизнь двенадцати цезарей»). Шифр стал популярным, дойдя до нашего времени, о чем свидетельствует то, что племянник Цезаря тоже использовал его, как и остальные поколения. Сейчас такой способ преобразования информации используется совсем не для засекречивания, так как взломать его довольно просто, но применение у него все же есть.</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "История создания"))
        self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#9bffff;\">Разберемся, что же такое Шифр Цезаря. Шифр Цезаря – это преобразование информации методом замены букв на другие, стоящие от данных через определенное количество символов в алфавите. Следовательно, зашифровать можно сообщение на любом языке, имеющем алфавит.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; color:#9bffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#9bffff;\">Шифрование: </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; color:#9bffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#9bffff;\">Рассмотрим это на примере:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; color:#9bffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#9bffff;\">Дано сообщение: «В эту минуту дверь тихо отворилась, и в комнату вошла одна девушка».</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; color:#9bffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#9bffff;\">1. Написано оно на русском языке, значит, будем использовать русский алфавит.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#9bffff;\">Алфавит     -     А Б В Г Д Е Ё Ж З И Й К Л М Н О П Р С Т У Ф Х Ц Ч Ш Щ Ъ Ы Ь Э Ю Я</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; color:#9bffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#9bffff;\">2. Теперь двигаем буквы в сторону в зависимости от ключа (цифры). Если ключ положительный, то двигаем влево, если отрицательный – вправо. Пусть ключом будет число 2. Начинаем с первой буквы и меняем ее на другую – делаем 2 шага вперед. Получим:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#9bffff;\">Шифрованный - В Г Д Е Ё Ж З И Й К Л М Н О П Р С Т У Ф Х Ц Ч Ш Щ Ъ Ы Ь Э Ю Я А Б</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; color:#9bffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#9bffff;\">3. Теперь находим номер каджой буквы в данном предложении в алфавите и ищем букву с таким же номером в шифрованном алфавите. Например первая буква в предолежнии это &quot;В&quot;, в алфавите она имеет номер 3. Под номером 3 в Шифрованном алфавите стоит буква &quot;Д&quot;. Записываем её. И так продолжаем делать пока не закончится предложение.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; color:#9bffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#9bffff;\">Было: В эту минуту дверь тихо отворилась, и в комнату вошла одна девушка.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#9bffff;\">Стало: В яфх окпхфх ёджтю фкчр рфдрткнвую, к д мропвфх дрънв рёпв ёждхъмв. </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; color:#9bffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#9bffff;\">Чтобы усложнить дешифровку, ключ можно менять с каждым новым словом, например, в виде определенной последовательности цифр. Такой текст будет сложнее взломать, так как придется дольше подбирать ключ, но это все равно не защищает содержание сообщения на 100%.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; color:#9bffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#9bffff;\">Дешифрование:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; color:#9bffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#9bffff;\">Дешифрование – преобразование зашифрованного текста в исходный вид. Данный процесс происходит по такому же алгоритму, как и шифрование, только в обратном направлении. Из смещенного алфавита буквы будут заменяться соответствующими буквами исходного.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; color:#9bffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#9bffff;\">Шифрованный - В Г Д Е Ё Ж З И Й К Л М Н О П Р С Т У Ф Х Ц Ч Ш Щ Ъ Ы Ь Э Ю Я А Б</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#9bffff;\">Алфавит     -     А Б В Г Д Е Ё Ж З И Й К Л М Н О П Р С Т У Ф Х Ц Ч Ш Щ Ъ Ы Ь Э Ю Я</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; color:#9bffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#9bffff;\">Было: В яфх окпхфх ёджтю фкчр рфдрткнвую, к д мропвфх дрънв рёпв ёждхъмв.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; color:#9bffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#9bffff;\">Стало: В эту минуту дверь тихо отворилась, и в комнату вошла одна девушка.</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Принцип работы"))
        self.pushButton_2.setText(_translate("MainWindow", "Зашифровать"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Зашифровать"))
        self.pushButton.setText(_translate("MainWindow", "Расшифровать"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Расшифровать"))




class My_Window_cezar(QtWidgets.QMainWindow, Window_cezar):
    def __init__(self, parent=None):
        super(My_Window_cezar, self).__init__(parent=parent)
        self.setupUi(self)
        self.palette = QPalette()
        self.palette.setBrush(QPalette.Background, QBrush(QPixmap("./w3.jpg")))
        self.setPalette(self.palette)

        self.lineEdit.setStyleSheet("""QLineEdit {color: rgb(155, 255, 255) }""")
        self.lineEdit_3.setStyleSheet("""QLineEdit {color: rgb(155, 255, 255) }""")
        self.lineEdit_2.setStyleSheet("""QLineEdit {color: rgb(155, 255, 255) }""")
        self.lineEdit_4.setStyleSheet("""QLineEdit {color: rgb(155, 255, 255) }""")

        
        self.textBrowser_5.setText("Введите текст, который хотите зашифровать, в верхнем блоке для текста\nВведите ключ шифрования, который хотите зашифровать, в реднем блоке для текста")
        self.textBrowser_5.setStyleSheet("""QTextBrowser {color: rgb(155, 255, 255) }""")
        self.textBrowser_4.setText("Введите текст, который хотите расшифровать, в верхнем блоке для текста\nВведите ключ шифрования, которым хотите расшифровать, в среднем блоке для текста")
        self.textBrowser_4.setStyleSheet("""QTextBrowser {color: rgb(155, 255, 255) }""")
        
        self.pushButton_2.clicked.connect(self.onClicked2)
        self.pushButton.clicked.connect(self.onClicked)
        

    def onClicked2(self):
        #print(2)
        self.textBrowser_5.setText("Введите текст, который хотите зашифровать, в верхнем блоке для текста\nВведите ключ (Целое число без пробелов!) шифрования, которым хотите зашифровать, в среднем блоке для текста")
        try:
            text = self.lineEdit.text()
            k = int(self.lineEdit_3.text())
        except ValueError:
            self.textBrowser_5.setText("Введите текст, который хотите зашифровать, в верхнем блоке для текста\nВведите ключ (Целое число без пробелов!) шифрования, которым хотите зашифровать, в среднем блоке для текста")
        try:
            k = k
            text = text
            self.encrypt_cezar(text, k)
        except:
            self.textBrowser_5.setText("Введите текст, который хотите зашифровать, в верхнем блоке для текста\nВведите ключ (Целое число без пробелов!) шифрования, которым хотите зашифровать, в среднем блоке для текста")

    def onClicked(self):
        try:
            text = self.lineEdit_2.text()
            k = int(self.lineEdit_4.text())
        except ValueError:
            self.textBrowser_4.setText("Введите текст, который хотите расшифровать, в верхнем блоке для текста\nВведите ключ (Целое число без пробелов!) шифрования, которым хотите расшифровать, в среднем блоке для текста")
        try:
            k = k
            text = text
            self.decrypt_cezar(text, k)
        except:
            pass
    
    def encrypt_cezar(self, text, k):
        alphabet=('а','б','в','г','д','е','ё','ж','з','и','й','к','л','м','н','о',
                  'п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю',
                  'я','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o',
                  'p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5',
                  '6','7','8','9','0',' ','.',',','?','!','<','>','#','$','%')
        #wordIn = input('Зашифровать:')
        wordIn = text.lower()
        wordKey = k # +++
        """while True:
            try:wordKey = int(self.k)
            except:print("Ведите число")
            else:break"""
        wordOut = ''
        for i in wordIn:
            try:
                x = (alphabet.index(i))
            except ValueError:
                wordOut += i
            else:
                x += wordKey
                while x >= len(alphabet):
                    x -= len(alphabet)
                while x < 0:
                    x += len(alphabet)
                wordOut += alphabet[x]
        #print('Зашифровал:',wordOut)
        a = "Исходный текст - " + text + "\n"
        k = "Ключ - " + str(k) + "\n"
        b = "Зашифрованный текст - " + wordOut + "\n"
        c = a + k + b 
        self.textBrowser_5.setText(c)


    def decrypt_cezar(self, text, k):
        alphabet=('а','б','в','г','д','е','ё','ж','з','и','й','к','л','м','н','о',
              'п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю',
              'я','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o',
              'p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5',
              '6','7','8','9','0',' ','.',',','?','!','<','>','#','$','%')
        #wordIn = input('Расшифровать:')
        wordIn = text.lower()
        wordKey = k # +++
        """while True:
            try:wordKey = int(input('Ключ:'))
            except:print('Введите число!')
            else:break"""
        wordOut = ''
        for i in wordIn:
            try:
                x = (alphabet.index(i))
            except ValueError:
                wordOut += i
            else:
                x -= wordKey
                while x >= len(alphabet):
                    x -= len(alphabet)
                while x < 0:
                    x += len(alphabet)
                wordOut += alphabet[x]
        #print('Зашифровал:',wordOut)
        a = "Зашифрованный текст - " + text + "\n"
        k = "Ключ - " + str(k) + "\n"
        b = "Исходный текст - " + wordOut + "\n"
        c = a + k + b 
        self.textBrowser_4.setText(c)



class My_Window_afin(QtWidgets.QMainWindow, Window_afin):
    def __init__(self, parent=None):
        super(My_Window_afin, self).__init__(parent=parent)
        self.setupUi(self)
        self.palette = QPalette()
        self.palette.setBrush(QPalette.Background, QBrush(QPixmap("./w4.jpg")))
        self.setPalette(self.palette)

        self.lineEdit.setStyleSheet("""QLineEdit {color: rgb(255, 172, 168) }""")
        self.lineEdit_3.setStyleSheet("""QLineEdit {color: rgb(255, 172, 168) }""")
        self.lineEdit_2.setStyleSheet("""QLineEdit {color: rgb(255, 172, 168) }""")
        self.lineEdit_4.setStyleSheet("""QLineEdit {color: rgb(255, 172, 168) }""")
        
        self.textBrowser_5.setText("Введите текст, который хотите зашифровать, в верхнем блоке для текста\nВведите ключ шифрования, который хотите зашифровать, в реднем блоке для текста")
        self.textBrowser_5.setStyleSheet("""QTextBrowser {color: rgb(255, 172, 168) }""")
        self.textBrowser_4.setText("Введите текст, который хотите расшифровать, в верхнем блоке для текста\nВведите ключ шифрования, которым хотите расшифровать, в среднем блоке для текста")
        self.textBrowser_4.setStyleSheet("""QTextBrowser {color: rgb(255, 172, 168) }""")
        
        self.pushButton_2.clicked.connect(self.onClicked2)
        self.pushButton.clicked.connect(self.onClicked)

        

    def onClicked2(self):
        try:
            text = self.lineEdit.text()
            k = int(self.lineEdit_2.text())
        except ValueError:
            self.textBrowser_5.setText("Введите текст, который хотите зашифровать, в верхнем блоке для текста\nВведите ключ (Целое число без пробелов!) шифрования, которым хотите зашифровать, в среднем блоке для текста")
        try:
            k = k
            text = text
            #print(text, k)
            self.encrypt_afin(text, k)
        except:
            pass

    def onClicked(self):
        try:
            text = self.lineEdit_3.text()
            k = int(self.lineEdit_4.text())
        except ValueError:
            self.textBrowser_4.setText("Введите текст, который хотите расшифровать, в верхнем блоке для текста\nВведите ключ (Целое число без пробелов!) шифрования, которым хотите расшифровать, в среднем блоке для текста")
        try:
            k = k
            text = text
            #print(text, k)
            self.decrypt_afin(text, k)
        except:
            pass

    def encrypt_afin(self, text, k):
        alphabet=('а','б','в','г','д','е','ё','ж','з','и','й','к','л','м','н','о',
          'п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю',
          'я','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o',
          'p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5',
          '6','7','8','9','0',' ','.',',','?','!','<','>','#','$','%')
        #wordIn = input('Зашифровать:')
        wordIn = text.lower()
        wordKey = int(k)
        """while True:
            try:wordKey = int(input('Ключ:'))
            except:print('Введите число!')
            else:break"""
        wordOut = ''
        for i in wordIn:
            try:
                x = (alphabet.index(i))
            except ValueError:
                wordOut += i
            else:
                x *= wordKey
                while x >= len(alphabet):
                    x -= len(alphabet)
                while x < 0:
                    x += len(alphabet)
                wordOut += alphabet[x]
        #print('Зашифровал:',wordOut)
        a = "Исходный текст - " + text + "\n"
        k = "Ключ - " + str(k) + "\n"
        b = "Зашифрованный текст - " + wordOut + "\n"
        c = a + k + b 
        self.textBrowser_5.setText(c)

    def decrypt_afin(self, text, k):
        alphabet=('а','б','в','г','д','е','ё','ж','з','и','й','к','л','м','н','о',
          'п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю',
          'я','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o',
          'p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5',
          '6','7','8','9','0',' ','.',',','?','!','<','>','#','$','%')
        #wordIn = input('Зашифровать:')
        wordIn = text.lower()
        wordKey = int(k)
        """while True:
            try:wordKey = int(input('Ключ:'))
            except:print('Введите число!')
            else:break"""
        wordOut = ''
        for i in wordIn:
            try:
                x = (alphabet.index(i))
            except ValueError:
                wordOut += i
            else:
                x *= (wordKey ** -1)
                while x >= len(alphabet):
                    x -= len(alphabet)
                while x < 0:
                    x += len(alphabet)
                wordOut += alphabet[int(x)]
        #print('Зашифровал:',wordOut)
        a = "Зашифрованный текст - " + text + "\n"
        k = "Ключ - " + str(k) + "\n"
        b = "Исходный текст - " + wordOut + "\n"
        c = a + k + b 
        self.textBrowser_4.setText(c)



        
class My_Window_basic(QtWidgets.QWidget, Window_basic):
    def __init__(self, parent=None):
        super(My_Window_basic, self).__init__(parent)
        self.setupUi(self)
        self.palette = QPalette()
        self.palette.setBrush(QPalette.Background, QBrush(QPixmap("./baza1.png")))
        self.setPalette(self.palette)
        
        self.btn_cezar.clicked.connect(self.onCezrClicked)
        self.btn_afin.clicked.connect(self.onAfinClicked)

    def onCezrClicked(self):
        self.cezar = My_Window_cezar()
        self.cezar.show()

    def onAfinClicked(self):
        self.cezar = My_Window_afin()
        self.cezar.show()


        
class My_Window_preview(QtWidgets.QWidget, Window_preview):
    def __init__(self, parent=None):
        super(My_Window_preview, self).__init__(parent)
        self.setupUi(self)
        
        self.pushButton.clicked.connect(self.onClicked)
        self.palette = QPalette()
        self.palette.setBrush(QPalette.Background, QBrush(QPixmap("./prew.png")))
        self.setPalette(self.palette)

    def onClicked(self):
        self.basic = My_Window_basic()
        self.basic.show()
        self.close()

        
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    
    w1 = My_Window_preview()
    w1.show()
    
    sys.exit(app.exec_())