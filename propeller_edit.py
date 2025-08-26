import sys
import cv2
import asyncio
import multiprocessing as mp
import numpy as np
import ipaddress
import logging
import websockets
import json
import time


from PySide6 import QtCore, QtGui
from PySide6.QtGui import QImage, QPixmap, QPen, QPainter, QBrush, QColor
from PySide6.QtCharts import QChart, QChartView, QLineSeries, QValueAxis
from PySide6.QtCore import QTimer, QThread, Qt
from PySide6.QtWidgets import QMainWindow, QApplication, QDialog, QMessageBox
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout
from PySide6.QtWidgets import QScrollArea, QPushButton, QLineEdit, QLabel

from ui.propeller_edit_form import Ui_Dialog_propeller_set


class EditDialog(QDialog, Ui_Dialog_propeller_set):
    def __init__(self, title, params: list[float], parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.setWindowTitle(title)

        self.lineEdit_id.setText(title[4:])
        self.lineEdit_pitch.setText(str(params[0]))
        self.lineEdit_yaw.setText(str(params[1]))
        self.lineEdit_x.setText(str(params[2]))
        self.lineEdit_y.setText(str(params[3]))
        self.lineEdit_z.setText(str(params[4]))

        self.pushButton_confirm.clicked.connect(self.accept)

    def get_edited_text(self):
        """获取编辑后的数据"""

        params = [0 for i in range(5)]
        try:
            id = "推进器 " + self.lineEdit_id.text().strip()
            params[0] = int(self.lineEdit_pitch.text())
            params[1] = int(self.lineEdit_yaw.text())
            params[2] = int(self.lineEdit_x.text())
            params[3] = int(self.lineEdit_y.text())
            params[4] = int(self.lineEdit_z.text())

            return id, params

        except Exception as e:
            logging.error(f"{self.windowIconText} : {e}")

        return None
