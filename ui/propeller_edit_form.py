# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'propeller_edit.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Dialog_propeller_set(object):
    def setupUi(self, Dialog_propeller_set):
        if not Dialog_propeller_set.objectName():
            Dialog_propeller_set.setObjectName(u"Dialog_propeller_set")
        Dialog_propeller_set.resize(285, 221)
        self.pushButton_confirm = QPushButton(Dialog_propeller_set)
        self.pushButton_confirm.setObjectName(u"pushButton_confirm")
        self.pushButton_confirm.setGeometry(QRect(200, 190, 75, 24))
        self.lineEdit_pitch = QLineEdit(Dialog_propeller_set)
        self.lineEdit_pitch.setObjectName(u"lineEdit_pitch")
        self.lineEdit_pitch.setGeometry(QRect(110, 40, 161, 20))
        self.lineEdit_yaw = QLineEdit(Dialog_propeller_set)
        self.lineEdit_yaw.setObjectName(u"lineEdit_yaw")
        self.lineEdit_yaw.setGeometry(QRect(110, 70, 161, 20))
        self.lineEdit_x = QLineEdit(Dialog_propeller_set)
        self.lineEdit_x.setObjectName(u"lineEdit_x")
        self.lineEdit_x.setGeometry(QRect(110, 100, 161, 20))
        self.lineEdit_y = QLineEdit(Dialog_propeller_set)
        self.lineEdit_y.setObjectName(u"lineEdit_y")
        self.lineEdit_y.setGeometry(QRect(110, 130, 161, 20))
        self.lineEdit_z = QLineEdit(Dialog_propeller_set)
        self.lineEdit_z.setObjectName(u"lineEdit_z")
        self.lineEdit_z.setGeometry(QRect(110, 160, 161, 20))
        self.label = QLabel(Dialog_propeller_set)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 40, 54, 16))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_2 = QLabel(Dialog_propeller_set)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 70, 54, 16))
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_3 = QLabel(Dialog_propeller_set)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 100, 71, 16))
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_4 = QLabel(Dialog_propeller_set)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 130, 71, 16))
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_5 = QLabel(Dialog_propeller_set)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 160, 71, 16))
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_id = QLabel(Dialog_propeller_set)
        self.label_id.setObjectName(u"label_id")
        self.label_id.setGeometry(QRect(20, 10, 54, 16))
        self.label_id.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_id = QLineEdit(Dialog_propeller_set)
        self.lineEdit_id.setObjectName(u"lineEdit_id")
        self.lineEdit_id.setGeometry(QRect(110, 10, 161, 20))

        self.retranslateUi(Dialog_propeller_set)

        QMetaObject.connectSlotsByName(Dialog_propeller_set)
    # setupUi

    def retranslateUi(self, Dialog_propeller_set):
        Dialog_propeller_set.setWindowTitle(QCoreApplication.translate("Dialog_propeller_set", u"Dialog", None))
        self.pushButton_confirm.setText(QCoreApplication.translate("Dialog_propeller_set", u"\u786e\u8ba4", None))
        self.label.setText(QCoreApplication.translate("Dialog_propeller_set", u"\u504f\u822a\u89d2", None))
        self.label_2.setText(QCoreApplication.translate("Dialog_propeller_set", u"\u4fef\u4ef0\u89d2", None))
        self.label_3.setText(QCoreApplication.translate("Dialog_propeller_set", u"\u6c34\u5e73\u4f4d\u7f6e  X", None))
        self.label_4.setText(QCoreApplication.translate("Dialog_propeller_set", u"\u6c34\u5e73\u4f4d\u7f6e  Y", None))
        self.label_5.setText(QCoreApplication.translate("Dialog_propeller_set", u"\u7ad6\u76f4\u4f4d\u7f6e  Z", None))
        self.label_id.setText(QCoreApplication.translate("Dialog_propeller_set", u"\u63a8\u8fdb\u5668 ID", None))
    # retranslateUi

