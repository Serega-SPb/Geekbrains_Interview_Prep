import sys

from PyQt5.QtWidgets import QApplication

from ui.model import MainModel as Model
from ui.qt_view.view import MainView as View
from ui.controller import MainController as Controller


if __name__ == '__main__':
    app = QApplication(sys.argv)
    model = Model()
    controller = Controller(model)
    view = View(model, controller)
    view.show()
    app.exec_()
