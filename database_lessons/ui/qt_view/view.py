from PyQt5.QtCore import Qt, QAbstractTableModel
from PyQt5.QtWidgets import (QMainWindow, QFileDialog, QWidget, QDialog,
                             QLabel, QLineEdit, QHBoxLayout,
                             QGridLayout, QPushButton, QTableWidget, QTableWidgetItem)

from .main_view_ui import Ui_MainWindow


class AddDialog(QDialog):

    line_edits = {}

    def __init__(self, fields, parent=None):
        super().__init__(parent)
        self.fields = fields
        self.data = {f: '' for f in fields if 'id' not in f}
        self.filled = False
        self.init_ui()

    def init_ui(self):
        def update_data(value):
            key = self.sender().objectName()
            self.data[key] = value

        self.setWindowTitle('Add')
        self.grid = QGridLayout(self)
        for i, field in enumerate(self.fields):
            if 'id' in field:
                continue
            lbl = QLabel(field, self)
            self.grid.addWidget(lbl, i, 0, 1, 1)
            ln_ed = QLineEdit(self)
            self.line_edits[field] = ln_ed
            ln_ed.setObjectName(field)
            ln_ed.textEdited.connect(update_data)
            self.grid.addWidget(ln_ed, i, 1, 1, 1)
        h_box = QHBoxLayout(self)
        ok_btn = QPushButton('Ok', self)
        ok_btn.clicked.connect(lambda x: self.end_edit(True))
        h_box.addWidget(ok_btn)
        cancel_btn = QPushButton('Cancel', self)
        cancel_btn.clicked.connect(lambda x: self.end_edit(False))
        h_box.addWidget(cancel_btn)
        self.grid.addLayout(h_box, len(self.fields), 0, 1, 2)

    def update_ui(self):
        for f, d in self.data.items():
            self.line_edits[f].setText(d)

    def change_title(self, title):
        self.setWindowTitle(title)

    def end_edit(self, flag):
        self.filled = flag
        self.close()


class TabWidget(QWidget):

    def __init__(self, model, parent=None):
        super().__init__(parent)
        self.model = model
        self.init_ui()
        self.init_data()

    def init_data(self):
        for i, col in enumerate(self.model.columns):
            self.table.insertColumn(i)
        self.table.setHorizontalHeaderLabels(self.model.columns)
        self.load_data()

    def load_data(self):
        self.table.setRowCount(0)
        for d in self.model.data:
            self._add_row_data(d)

    def init_ui(self):
        self.grid = QGridLayout(self)

        self.table = QTableWidget(self)
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.table.setSelectionMode(QTableWidget.SingleSelection)
        self.table.setSelectionBehavior(QTableWidget.SelectRows)
        self.table.cellDoubleClicked.connect(self.edit_data)
        self.grid.addWidget(self.table, 0, 0, 1, 2)

        self.add_btn = QPushButton('Add', self)
        self.add_btn.clicked.connect(self.add_new_data)
        self.grid.addWidget(self.add_btn, 1, 0, 1, 1)
        self.remove_btn = QPushButton('Remove', self)
        self.remove_btn.clicked.connect(self.remove_row)
        self.remove_btn.setEnabled(False)
        self.grid.addWidget(self.remove_btn, 1, 1, 1, 1)

        self.table.itemSelectionChanged.connect(self.selected_changed)

    def add_new_data(self):
        add_dlg = AddDialog(self.model.columns, self)
        add_dlg.exec()
        if not add_dlg.filled:
            return
        new_data = add_dlg.data
        obj = self.model.insert(new_data.values())
        self._add_row_data(obj)

    def _add_row_data(self, obj):
        row = self.table.rowCount()
        self.table.insertRow(row)
        for i, col in enumerate(self.model.columns):
            value = getattr(obj, col, 'NULL')
            item = QTableWidgetItem(str(value))
            item.key = col
            item.value = value
            self.table.setItem(row, i, item)

    def edit_data(self, *args):
        row = args[0]
        old_data = {}
        key = None
        for i in range(len(self.model.columns)):
            item = self.table.item(row, i)
            if i == 0:
                key = item.value
            else:
                old_data[item.key] = item.value

        ed_dlg = AddDialog(self.model.columns, self)
        ed_dlg.change_title('Edit')
        ed_dlg.data = dict(old_data)
        ed_dlg.update_ui()
        ed_dlg.exec()
        if not ed_dlg.filled:
            return
        changes = {k: v for k, v in ed_dlg.data.items() if v != old_data[k]}
        if changes:
            self.model.update(key, changes)

        for i, col in enumerate(self.model.columns):
            if col not in changes:
                continue
            item = self.table.item(row, i)
            item.setText(str(changes[col]))
            item.value = changes[col]

    def remove_row(self):
        items = self.table.selectedItems()
        if items:
            self.model.delete(items[0].value)  # TODO temp solution
            index = self.table.indexFromItem(items[0])
            self.table.removeRow(index.row())

    def selected_changed(self, *args):
        self.remove_btn.setEnabled(bool(self.table.selectedItems()))


class MainView(QMainWindow):

    def __init__(self, model, controller, parent=None):
        super().__init__(parent)

        self.model = model
        self.controller = controller

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.init_ui()
        self.connect_widgets()
        self.connect_model_signals()

    def init_ui(self):
        self.setWindowTitle('Storage browser')
        self.ui.dbTabWidget.clear()

    def connect_widgets(self):
        self.ui.opeDbBtn.clicked.connect(self._open_db_file)

    def connect_model_signals(self):
        self.model.db_path_changed += self.ui.dbPathLnEd.setText
        self.model.tables_changed += self.load_tabels

    def _open_db_file(self):
        file = QFileDialog.getOpenFileName(self, 'Select db file')[0]
        if file:
            self.controller.set_db_path(file)

    def load_tabels(self, tbl_mods):
        self.ui.dbTabWidget.clear()
        for tbl in tbl_mods:
            tab = TabWidget(tbl, self.ui.dbTabWidget)
            self.ui.dbTabWidget.addTab(tab, tbl.name)
