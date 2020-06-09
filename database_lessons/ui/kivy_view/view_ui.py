from kivy.properties import ListProperty, StringProperty, BooleanProperty, ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.recycleview import RecycleView
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem

from event import Event
from notify_property import NotifyProperty


class EventTabHub:
    def __init__(self, name):
        self.name = name
        self.selected_row_changed = Event(str)
        self.current_data_changed = Event(object)
    pass


class TableCell(BoxLayout):
    text = StringProperty('')
    hub = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text = kwargs.get('text')
        self._toggled = NotifyProperty('toggled', False)
        self.toggled_chanegd = Event(bool)
        self._toggled += self.toggled_chanegd.emit

    def on_state_changed(self):
        if not self.is_header:
            self._toggled.set(self.state == 'down')


class TableRow(BoxLayout):
    values = ListProperty([])
    hub = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_values(self, instance, value):
        [self._unsub(w) for w in self.children if hasattr(w, 'toggled')]
        self.clear_widgets()
        for i, v in enumerate(value):
            cell = TableCell(text=str(v))
            cell.is_header = self.is_header
            cell.toggled_chanegd += self.select_hndl
            cell.background_color = self.background_color
            self.add_widget(cell)

    def on_hub(self, instance, value):
        self.hub = value
        for ch in self.children:
            ch.group = self.hub.name

    def _unsub(self, cell):
        cell.toggled_chanegd -= self.select_hndl

    def select_hndl(self, value):
        if value is True:
            self.hub.selected_row_changed.emit(self.values[0])


class DbTable(BoxLayout):
    headers = ListProperty([])
    data = ListProperty([])
    objects = ListProperty([])
    hub = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_hub(self, instance, value):
        self.hub = value
        self.hub.selected_row_changed += self.on_selected_row_changed

    def on_objects(self, instance, value):
        formated_data = []
        for obj in value:
            formated_data.append({'values': tuple(getattr(obj, col) for col in self.headers), 'hub': self.hub})
        self.data = formated_data

    def on_selected_row_changed(self, value):
        index = [i for i, d in enumerate(self.data) if d['values'][0] == value]
        if index:
            index = index.pop()
            self.hub.current_data_changed.emit(self.objects[index])


class DbTab(TabbedPanelItem):
    title = StringProperty('')
    table_headers = ListProperty([])
    table_data = ListProperty([])
    hub = ObjectProperty()

    def __init__(self, model, **kwargs):
        self.hub = EventTabHub(model.name)
        super().__init__(**kwargs)
        self.__current_data = None
        self.model = model
        self.hub.current_data_changed += self.set_current_data
        self.title = self.model.name
        self.table_headers = self.model.columns
        self.table_data = self.model.data

    def set_current_data(self, value):
        if self.__current_data == value:
            return
        self.__current_data = value

    def add_btn_click(self):
        add_popup = self.popup
        add_popup.open()
        add_popup.ok.on_press = lambda: self.apply_new_data(True)
        add_popup.cancel.on_press = lambda: self.apply_new_data(False)

    def apply_new_data(self, *args):
        self.popup.dismiss()
        if args[0] is False:
            return
        new_data = self.popup.data
        new_data = [new_data[head] for head in self.table_headers if 'id' not in head]
        obj = self.model.insert(new_data)
        self.table_data.append(obj)

    def remove_btn_click(self):
        if self.__current_data is None:
            return
        self.table_data.remove(self.__current_data)
        self.model.delete(getattr(self.__current_data, self.table_headers[0]))
        self.__current_data = None


class DbTabs(TabbedPanel):
    do_default_tab = False
    tabs = ListProperty([])

    def on_tabs(self, instance, value):
        self.clear_widgets()
        for mod in value:
            self.add_widget(DbTab(mod))


class AddDataPopup(Popup):
    fields = ListProperty([])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_fields(self, instance, value):
        self.container.clear_widgets()
        for f in value:
            if 'id' in f:
                continue
            row = AddRow()
            row.title = f
            self.container.add_widget(row)

    def open(self, *largs, **kwargs):
        for wid in self.container.children:
            wid.value = ''
        super().open(*largs, **kwargs)

    def dismiss(self, *largs, **kwargs):
        self.data = {}
        for wid in self.container.children:
            self.data[wid.title] = wid.value
        super().dismiss(*largs, **kwargs)


class AddRow(BoxLayout):
    title = StringProperty('')
    value = StringProperty('')
