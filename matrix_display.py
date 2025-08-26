import sys
import numpy as np
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QScrollArea,
    QPushButton,
    QLineEdit,
    QLabel,
    QMessageBox,
    QDialog,
    QTableWidget,
    QTableWidgetItem,
    QHeaderView,
)
from PySide6.QtCore import Qt


class MatrixDisplayWindow(QMainWindow):
    def __init__(self, matrix):
        super().__init__()
        self.setWindowTitle("Numpy矩阵显示")
        self.setGeometry(100, 100, 800, 600)

        self.matrix = matrix

        # 创建中央部件和主布局
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        # 创建矩阵显示区域
        self.matrix_widget = QWidget()
        matrix_layout = QVBoxLayout(self.matrix_widget)

        # 创建表格控件
        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(6)  # 固定6列
        self.table_widget.setHorizontalHeaderLabels(["x", "y", "z", "rx", "ry", "rz"])

        # 设置表格属性
        self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table_widget.setAlternatingRowColors(True)
        self.table_widget.setStyleSheet(
            """
            QTableWidget {
                gridline-color: #d0d0d0;
                font-family: Consolas, Monaco, monospace;
            }
            QTableWidget::item:selected {
                background-color: #b8d6f6;
            }
        """
        )

        matrix_layout.addWidget(self.table_widget)
        main_layout.addWidget(self.matrix_widget)

        # 信息显示标签
        self.info_label = QLabel("请生成或加载矩阵")
        self.info_label.setAlignment(Qt.AlignCenter)
        self.info_label.setStyleSheet("QLabel { color: #666; padding: 10px; }")
        main_layout.addWidget(self.info_label)

    def display_matrix(self):
        """显示矩阵到表格中"""
        if not hasattr(self, "matrix") or self.matrix.size == 0:
            self.table_widget.setRowCount(0)
            self.info_label.setText("矩阵为空")
            return

        rows, cols = self.matrix.shape

        # 设置表格行数
        self.table_widget.setRowCount(rows)

        # 填充表格数据
        for i in range(rows):
            for j in range(cols):
                item = QTableWidgetItem(str(self.matrix[i, j]))
                item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
                # 设置不可编辑
                item.setFlags(item.flags() & ~Qt.ItemIsEditable)
                self.table_widget.setItem(i, j, item)

        # 更新信息标签
        self.info_label.setText(f"矩阵形状: {rows} × {cols} | 数据类型: {self.matrix.dtype}")

    def load_custom_matrix(self, matrix):
        """加载自定义矩阵"""
        if not isinstance(matrix, np.ndarray):
            QMessageBox.warning(self, "错误", "输入必须是numpy数组")
            return

        if matrix.ndim != 2:
            QMessageBox.warning(self, "错误", "必须是二维矩阵")
            return

        if matrix.shape[1] != 6:
            QMessageBox.warning(self, "错误", "矩阵必须有6列")
            return

        self.matrix = matrix
        self.display_matrix()
