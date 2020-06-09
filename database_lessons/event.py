class Event:
    def __init__(self, *arg_types):
        self.__subscribers = []
        self.arg_types = arg_types

    def __iadd__(self, func):
        if not callable(func):
            raise ValueError(f'{func.__name__} not callable')
        self.__subscribers.append(func)
        return self

    def __isub__(self, func):
        self.__subscribers.remove(func)
        return self

    def emit(self, *args):
        [sub(*args) for sub in self.__subscribers]