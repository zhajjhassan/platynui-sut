from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import Slot
from src.platynui_sut.ui.ui_mainwindow import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Signal verbinden: Button -> Slot
        self.ui.pushButton.clicked.connect(self.say_hello)

    @Slot()
    def say_hello(self):
        self.ui.label.setText("Hallo, Ziyad! 👋")


app = QApplication([])
window = MainWindow()
window.show()
app.exec()
