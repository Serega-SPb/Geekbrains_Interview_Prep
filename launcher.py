import os

from core.menu import Menu, MenuAction
from core.console_ui import ConsoleUi


def start_script(script_path):
    os.system(f'python {script_path}')


class Launcher:
    EXCLUDES = ['.git', '.idea', 'venv', '.gitignore', 'core', 'launcher.py']
    main_menu = Menu('Main menu')

    def __init__(self):
        self.init_menu()

    def init_menu(self):

        def create_script_action(name, sc_path):
            return MenuAction(name, lambda: start_script(sc_path))

        def create_sub_menu(parent_menu, s_path):
            for d in os.listdir(s_path):
                if d in self.EXCLUDES:
                    continue

                d_path = os.path.join(s_path, d)
                if os.path.isdir(d_path):
                    sub_menu = Menu(d)
                    create_sub_menu(sub_menu, d_path)
                    parent_menu.add(sub_menu)
                elif d.endswith('.py'):
                    parent_menu.add(create_script_action(d, d_path))

        create_sub_menu(self.main_menu, os.path.dirname(__file__))

    def start(self):
        ui = ConsoleUi(self.main_menu)
        ui.start()


def main():
    launcher = Launcher()
    launcher.start()


if __name__ == '__main__':
    main()
