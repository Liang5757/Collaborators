import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QDesktopWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QFileDialog

from utils.Arithmetic import *


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        # element
        self.btn1 = QPushButton('Generate Exercise', self)
        self.btn2 = QPushButton('Generate Answer', self)
        self.btn3 = QPushButton('Inspect Answer', self)
        # motion
        self.btn1.clicked.connect(self.generate_exercise)
        self.btn2.clicked.connect(self.generate_answer)
        self.btn3.clicked.connect(self.check_files)
        # Add button
        vbox = QVBoxLayout()
        vbox.addWidget(self.btn1)
        vbox.addWidget(self.btn2)
        vbox.addWidget(self.btn3)
        self.setLayout(vbox)
        # 界面绘制交给InitUi方法
        self.initUI()

    # 初始化GUI
    def initUI(self):
        # 设置窗口的位置和大小
        self.setGeometry(300, 300, 30, 120)
        # 设置窗口的标题
        self.setWindowTitle('Arithmetic')
        self.setWindowFlags(Qt.WindowCloseButtonHint|Qt.WindowStaysOnTopHint)
        # self.center()
        # 显示窗口
        self.show()

    # 弹窗退出程序
    # def closeEvent(self, QCloseEvent):
    #     reply = QMessageBox.question(self, "Info", "exit?", QMessageBox.Yes | QMessageBox.Cancel)
    #     if reply == QMessageBox.Yes:
    #         QCloseEvent.accept()
    #     else:
    #         QCloseEvent.ignore()

    # Windows properties
    # def center(self):
    #     qr = self.frameGeometry()
    #     cp = QDesktopWidget().availableGeometry().center()
    #     qr.moveCenter(cp)
    #     self.move(qr.topLeft())

    # function help
    def generate_exercise(self):
        openfile_name = '\'' + QFileDialog.getOpenFileName(self, '请选择Exercise.txt', '', 'txt files(*.txt)')[0] + '\''
        print(openfile_name)

    def generate_answer(self):
        openfile_name = '\'' + QFileDialog.getOpenFileName(self, '请选择Answer.txt', '', 'txt files(*.txt)')[0] + '\''
        print(openfile_name)

    def check_files(self):
        openfile_name_exercise = '\'' + QFileDialog.getOpenFileName(self, '请选择Exercise.txt', '', 'txt files(*.txt)')[0] + '\''
        if openfile_name_exercise == "''":
            return
        openfile_name_answer = '\'' + QFileDialog.getOpenFileName(self, '请选择Answer.txt', '', 'txt files(*.txt)')[0] + '\''
        if openfile_name_answer == "''":
            return
        print(openfile_name_exercise)
        print(openfile_name_answer)


if __name__ == '__main__':
    # 创建应用程序和对象
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())
