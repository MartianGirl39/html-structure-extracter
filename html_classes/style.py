from html_classes.html_attr import Attribute


class Style(Attribute):
    def __init__(self, name, value):
        if value.count("!important") > 0:
            self.__isImportant = True
        else:
            self.__isImportant = False
        super().__init__(name, value.replace("!important", ""))

    def __str__(self):
        return self.name() + ': ' + self.value()
