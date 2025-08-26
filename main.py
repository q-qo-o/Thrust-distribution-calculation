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
import math

from PySide6 import QtCore, QtGui
from PySide6.QtGui import QImage, QPixmap, QPen, QPainter, QBrush, QColor
from PySide6.QtCharts import QChart, QChartView, QLineSeries, QValueAxis
from PySide6.QtCore import QTimer, QThread, Qt
from PySide6.QtWidgets import QMainWindow, QApplication, QDialog, QMessageBox
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout
from PySide6.QtWidgets import QScrollArea, QPushButton, QLineEdit, QLabel


from ui.main_form import Ui_MainWindow
from propeller_edit import EditDialog
from matrix_display import MatrixDisplayWindow
from file_genrate import generate_files


def cross_product(a, b):
    if len(a) != 3 or len(b) != 3:
        raise ValueError("向量必须是三维的")

    x = a[1] * b[2] - a[2] * b[1]
    y = a[2] * b[0] - a[0] * b[2]
    z = a[0] * b[1] - a[1] * b[0]

    return [x, y, z]


def generalized_force_direction(params):
    force = [
        -math.cos(params[0]) * math.sin(params[1]),
        math.cos(params[0]) * math.cos(params[1]),
        math.sin(params[0]),
    ]

    position = [params[2], params[3], params[4]]

    torque = cross_product(position, force)

    return force + torque


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setFixedSize(459, 686)
        self.setWindowFlags(Qt.Window | Qt.WindowMinimizeButtonHint | Qt.WindowCloseButtonHint)

        self.pushButton_add.clicked.connect(self.add_propellor)
        self.pushButton_clear.clicked.connect(self.clear_propellor)
        self.pushButton_summon.clicked.connect(self.summon_c_file)
        self.pushButton_show.clicked.connect(self.show_matrix)

        # 创建用于放置条目的容器部件
        self.items_container = QWidget()
        self.items_layout = QVBoxLayout(self.items_container)
        self.items_layout.setAlignment(Qt.AlignTop)

        self.scrollArea_show.setWidget(self.items_container)

        # 存储所有条目的列表
        self.item_widgets = []

        self.thrust_matrix = None

        self.cache_path = "./tmp/cache.json"

        # 初始化界面
        self.load_propellers_info_cache()


    def add_item_widget(self, id, params):
        # 创建条目部件
        item_widget = QWidget()
        item_layout = QHBoxLayout(item_widget)
        item_layout.setContentsMargins(5, 2, 5, 2)

        # 添加标签显示文本
        label = QLabel(id)
        item_layout.addWidget(label)

        item_widget.label = label
        item_widget.params = params  # [0 for i in range(5)]

        # 添加编辑按钮
        edit_btn = QPushButton("编辑")
        edit_btn.clicked.connect(lambda: self.edit_item(item_widget))
        item_layout.addWidget(edit_btn)

        # 添加删除按钮
        delete_btn = QPushButton("删除")
        delete_btn.clicked.connect(lambda: self.remove_item(item_widget))
        item_layout.addWidget(delete_btn)

        # 添加到布局中
        self.items_layout.addWidget(item_widget)
        self.item_widgets.append(item_widget)

    def add_propellor(self):
        """添加一个新条目"""
        text = "推进器 " + self.lineEdit_input.text().strip()
        if text:
            self.add_item_widget(text, [0 for i in range(5)])

            # 清空输入框并聚焦
            self.lineEdit_input.clear()
            self.lineEdit_input.setFocus()

            self.save_propellers_info_cache()

    def save_propellers_info_cache(self):

        cache_dic = {}

        with open(self.cache_path, "r") as f:
            cache_json = f.read()
            cache_dic = json.loads(cache_json)

        propellers_info_list = []

        for item_widget in self.item_widgets:
            propellers_info_list.append(
                {
                    "id": item_widget.label.text().strip(),
                    "params": item_widget.params.copy(),
                }
            )

        cache_dic["propeller_info"] = propellers_info_list

        with open(self.cache_path, "w") as f:
            cache_json = json.dumps(cache_dic)
            f.write(cache_json)

    def load_propellers_info_cache(self):
        try:
            cache_dic = None
            with open(self.cache_path, "r") as f:
                cache_dic = json.loads(f.read())
        except json.decoder.JSONDecodeError:
            with open(self.cache_path, "w") as f:
                empty_json = json.dumps(
                    {
                        "propeller_info": [],
                    }
                )
                cache_dic = {
                    "propeller_info": [],
                }
                f.write(empty_json)
        except Exception as e:
            logging.warning(f"{self.objectName} : {e}")
            return

        propellers_info_list = cache_dic["propeller_info"]
        if propellers_info_list:
            for propeller_info in propellers_info_list:
                self.add_item_widget(propeller_info["id"], propeller_info["params"])

    def remove_item(self, item_widget):
        """移除指定条目"""
        if item_widget in self.item_widgets:
            self.items_layout.removeWidget(item_widget)
            self.item_widgets.remove(item_widget)
            item_widget.deleteLater()

    def edit_item(self, item_widget):
        """编辑指定条目 - 弹出独立窗口"""
        # 获取当前文本
        id = item_widget.label.text().strip()
        params = item_widget.params

        # 创建并显示编辑对话框
        dialog = EditDialog(id, params, self)
        result = dialog.exec()  # 显示模态对话框

        # 如果用户点击了保存
        if result == QDialog.Accepted:
            ret = dialog.get_edited_text()
            if ret is not None:
                item_widget.label.setText(ret[0])
                item_widget.params = ret[1]
            else:
                QMessageBox.warning(self, "警告", "内容输入有误")

    def clear_propellor(self):
        if not self.item_widgets:
            return

        reply = QMessageBox.question(
            self, "确认清空", "确定要清空所有推进器吗？", QMessageBox.Yes | QMessageBox.No, QMessageBox.No
        )

        if reply == QMessageBox.Yes:
            for item_widget in self.item_widgets[:]:  # 使用副本遍历
                self.items_layout.removeWidget(item_widget)
                item_widget.deleteLater()
            self.item_widgets.clear()

    def summon_c_file(self):
        if self.thrust_matrix is None:
            try:
                generalized_force_matrix = [generalized_force_direction(i.params) for i in self.item_widgets]
                generalized_force_matrix = np.array(generalized_force_matrix).T               
                self.thrust_matrix = np.linalg.pinv(generalized_force_matrix)
            except np.linalg.LinAlgError as e:
                QMessageBox.critical(self, "计算错误", f"无法计算伪逆矩阵: {str(e)}")
                return
        if self.thrust_matrix is not None:
            generate_files("./output", self.thrust_matrix)
            QMessageBox.information(self, "文件生成成功", "存储路径：./output")

    def show_matrix(self):
        generalized_force_matrix = [generalized_force_direction(i.params) for i in self.item_widgets]
        generalized_force_matrix = np.array(generalized_force_matrix).T

        try:
            self.thrust_matrix = np.linalg.pinv(generalized_force_matrix)
        except np.linalg.LinAlgError as e:
            QMessageBox.critical(self, "计算错误", f"无法计算伪逆矩阵: {str(e)}")
            return

        self.matrix_display_window = MatrixDisplayWindow(self.thrust_matrix)  # 保存为实例变量以防垃圾回收
        self.matrix_display_window.show()
        self.matrix_display_window.display_matrix()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    mp.freeze_support()

    app = QApplication(sys.argv)
    main_form = MainWindow()
    app.setWindowIcon(QtGui.QIcon("./tmp/propeller.ico"))

    main_form.show()

    sys.exit(app.exec())
