from dataclasses import dataclass

class Attribute:
    def __init__(self, name, value):
        self.__name = name
        self.__value = value

    def name(self):
        return self.__name

    def value(self):
        return self.__value

    def __str__(self):
        return self.name() + '="' + self.value() + '"'
