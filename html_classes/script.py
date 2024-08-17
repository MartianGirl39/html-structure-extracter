from html_classes import Attribute


class Script(Attribute):
    def __init__(self, rel, src, file_type):
        self.__type = file_type
        super().__init__(rel, src)

    def type(self):
        return self.__type

    def rel(self):
        return super().name()

    def src(self):
        return super().value()

    def __str__(self):
        return self.name() + '="' + self.value() + '"'
