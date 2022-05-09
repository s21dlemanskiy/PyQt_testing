# -*- coding:utf-8 -*-
from PyQt5.output import Ui_MainWindow
from PyQt5 import QtCore, QtWidgets

class Ui_MainWindow1(Ui_MainWindow):
    def setupUi(self, MainWindow):
        Ui_MainWindow.setupUi(self, MainWindow)
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)            # Удаляет TitleBar
        MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)         # делает фон прозрачным
        def move_window(event):
            if event.buttons() == QtCore.Qt.LeftButton:
                MainWindow.move(MainWindow.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        self.frame_2.mouseMoveEvent = move_window

    def mousePressEvent(self, event):
        print("__________________")
        self.dragPos = event.globalPos()











if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()#flags=QtCore.Qt.WindowStaysOnTopHint)
    ui = Ui_MainWindow1()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())