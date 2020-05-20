from core.menu import Menu, MenuAction


class ConsoleUi:

    BACK_KEY = 'b'
    QUIT_KEY = 'q'

    menu_list = {}
    exit_flag = False

    def __init__(self, menu: Menu):
        self.current_menu = menu

    @property
    def current_menu(self):
        return self._menu

    @current_menu.setter
    def current_menu(self, value):
        self._menu = value
        self._update_menu_list()

    def _update_menu_list(self):
        self.menu_list = {str(i): m for i, m in enumerate(self.current_menu.children.values(), 1)}
        if self.current_menu.parent:
            self.menu_list[self.BACK_KEY] = MenuAction('back', self.__back_action)
        self.menu_list[self.QUIT_KEY] = MenuAction('quit', self.__quit_action)

    def __back_action(self):
        self.current_menu = self.current_menu.parent

    def __quit_action(self):
        self.exit_flag = True

    def start(self):
        while not self.exit_flag:
            print(f'{self.current_menu.name:-^50}')
            print('\n'.join([f'{i}. {str(m)}' for i, m in self.menu_list.items()]))
            action = input()
            if action not in self.menu_list.keys():
                print('Incorrect command')
                continue

            sub_menu = self.menu_list[action]
            if isinstance(sub_menu, Menu):
                self.current_menu = sub_menu
            else:
                print(f'{sub_menu.name:_^50}')
                sub_menu.execute()
            print('='*50)
