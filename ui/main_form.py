# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLineEdit, QMainWindow, QPushButton,
    QScrollArea, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(459, 686)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.scrollArea_show = QScrollArea(self.centralwidget)
        self.scrollArea_show.setObjectName(u"scrollArea_show")
        self.scrollArea_show.setGeometry(QRect(9, 119, 441, 561))
        self.scrollArea_show.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 439, 559))
        self.scrollArea_show.setWidget(self.scrollAreaWidgetContents)
        self.pushButton_add = QPushButton(self.centralwidget)
        self.pushButton_add.setObjectName(u"pushButton_add")
        self.pushButton_add.setGeometry(QRect(350, 20, 101, 24))
        self.pushButton_clear = QPushButton(self.centralwidget)
        self.pushButton_clear.setObjectName(u"pushButton_clear")
        self.pushButton_clear.setGeometry(QRect(10, 50, 441, 24))
        self.lineEdit_input = QLineEdit(self.centralwidget)
        self.lineEdit_input.setObjectName(u"lineEdit_input")
        self.lineEdit_input.setGeometry(QRect(10, 20, 331, 20))
        self.pushButton_show = QPushButton(self.centralwidget)
        self.pushButton_show.setObjectName(u"pushButton_show")
        self.pushButton_show.setGeometry(QRect(10, 80, 211, 24))
        self.pushButton_summon = QPushButton(self.centralwidget)
        self.pushButton_summon.setObjectName(u"pushButton_summon")
        self.pushButton_summon.setGeometry(QRect(240, 80, 211, 24))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u63a8\u529b\u5206\u914d\u77e9\u9635\u8ba1\u7b97", None))
        self.pushButton_add.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0", None))
        self.pushButton_clear.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u7a7a\u533a\u57df", None))
        self.pushButton_show.setText(QCoreApplication.translate("MainWindow", u"\u663e\u793a\u63a8\u529b\u77e9\u9635", None))
        self.pushButton_summon.setText(QCoreApplication.translate("MainWindow", u"\u751f\u6210\u63a8\u529b\u5206\u914d\u6587\u4ef6", None))
    # retranslateUi

