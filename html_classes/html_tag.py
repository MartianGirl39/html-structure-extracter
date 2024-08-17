class Tag:
    __slots__ = ('__id_name', '__tag_type', '__styles', '__classes', '__attributes')
    def __init__(self, tag_type):
        self.__id_name = ""
        self.__tag_type = tag_type
        self.__styles = []
        self.__classes = []
        self.__attributes = []

    def get_id(self):
        return self.__id_name

    def set_id(self, value):
        self.__id_name = value

    def tag_type(self):
        return self.__tag_type

    def attribute(self, item):
        for attr in self.__attributes:
            if attr.name() == item:
                return attr.value()
        return ""

    def attributes(self):
        return [attribute.name() for attribute in self.__attributes]

    def copy_attributes(self):
        return self.__attributes

    def add_attribute(self, attr):
        self.__attributes.append(attr)

    def style(self, style_type):
        for style in self.__styles:
            if style.name() == style_type:
                return style.value()
        return ""

    def styles(self):
        return self.__styles

    def add_style(self, style):
        try:
            self.__styles.append(style)
            return True
        except:
            return False

    def add_styles(self, styles):
        try:
            self.__styles.append(styles)
            return True
        except:
            return False

    def has_class_name(self, class_name):
        for style in self.__styles:
            if style.name() == class_name:
                return True
        return False

    def class_names(self):
        return self.__classes

    def add_class(self, class_name):
        try:
            self.__classes.append(class_name)
            return True
        except:
            return False

    def add_styles(self, class_names):
        try:
            self.__classes.append(class_names)
            return True
        except:
            return False


    def __str__(self):
        str = "<" + self.tag_type()
        if self.__id_name != "":
            str += ' id="' + self.__id_name + '"'
        for attr in self.__attributes:
            str += (" " + attr.__str__())
        if(len(self.__classes) > 0):
            str += ' class="'
            for class_name in self.__classes:
                str += class_name + " "
            str += '"'
        if(len(self.__styles) > 0):
            str += ' style="'
            for style in self.__styles:
                str += style.__str__() + " "
            str += '"'
        str += ">"
        return str