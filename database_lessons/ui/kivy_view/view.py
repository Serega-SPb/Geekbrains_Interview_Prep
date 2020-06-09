from kivy.app import App
from kivy.properties import ListProperty, StringProperty

from .view_ui import DbTabs


class ViewApp(App):

    db_path = StringProperty('')
    table_models = ListProperty([])

    def __init__(self, model, controller, **kwargs):
        super().__init__(**kwargs)
        self. model = model
        self.controller = controller

        self.title = 'Database Browser'

        self.subscribe_to_events()

    def subscribe_to_events(self):
        self.model.db_path_changed += self.set_db_path
        self.model.tables_changed += self.load_tabels

    def set_db_path(self, value):
        self.db_path = value

    def load_tabels(self, mods):
        self.table_models = mods

    def open_popup_dialog(self):
        popup = self.root.popup
        popup.open()

    def apply_path(self, filepath):
        self.controller.set_db_path(filepath)
        popup = self.root.popup
        popup.dismiss()
