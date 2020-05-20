from abc import ABC


class MenuComponent(ABC):

    def __init__(self, name):
        self.name = name
        self._parent = None

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, value):
        self._parent = value

    def add(self, component):
        pass

    def remove(self, component):
        pass

    def __str__(self):
        return self.name


class Menu(MenuComponent):

    def __init__(self, name):
        super().__init__(name)
        self._children = {}

    @property
    def children(self):
        return self._children

    def add(self, component: MenuComponent):
        self._children[component.name] = component
        component.parent = self
        return self

    def remove(self, component: MenuComponent):
        self._children.pop(component.name)
        component.parent = None

    def __getitem__(self, item):
        return self._children[item] if item in self._children.keys() else None

    def __repr__(self):
        return f'Menu("{self.name}") ({len(self.children)})'


class MenuAction(MenuComponent):

    def __init__(self, name, action):
        super().__init__(name)
        self.action = action

    def execute(self):
        self.action()

    def __repr__(self):
        return f'MenuAction("{self.name}", {self.action})'
