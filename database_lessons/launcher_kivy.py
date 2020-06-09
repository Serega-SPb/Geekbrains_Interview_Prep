from ui.model import MainModel as Model
from ui.kivy_view.view import ViewApp as View
from ui.controller import MainController as Controller


if __name__ == '__main__':
    model = Model()
    controller = Controller(model)
    view = View(model, controller)
    view.run()

