from dataclasses import dataclass

from html_classes import Tag, Attribute
import re

from html_classes.style import Style

class Body:

    __slots__ = ('__tags', '__styles')

    def __new__(cls):
        instance = super().__new__(cls)
        instance.__tags = {}
        instance.__styles = []
        return instance

    def style(self, style_name):
        for style in self.__styles:
            if style.name() == style_name:
                return style.value()
        return ""

    def styles(self):
        return self.__styles.copy()

    def add_style(self, style):
        self.__styles.append(style)

    def get_tag(self, tag_name):
        return self.__tags[tag_name]

    def tags(self):
        return [value.get_id() for value in self.__tags.values()]

    def tag_types(self):
        return [value.tag_type() for value in self.__tags.values()]

    def copy_tags(self):
        return self.__tags.values()

    def add_tag(self, tag):
        tag_type = tag.split(" ")[0].strip()
        new_tag = Tag(tag_type)
        tag_id = ""
        attributes = re.split(r'="|=\'|" |\' ', tag[len(tag_type):])
        for i in range(1, len(attributes), 2):
            name = attributes[i-1].strip()
            value = attributes[i].replace('"', "").replace("'", "").strip()
            if name == 'id':
                tag_id = value
                new_tag.set_id(tag_id)
            elif name == 'style':
                styles = value.split(";")
                # split string after style by ";" and then again by ":" and trim the strings as we go
                for style in styles:
                    if style == "":
                        break
                    style_attributes = style.split(":")
                    if len(style_attributes) < 2:
                        break
                    new_tag.add_style(Style(style_attributes[0], style_attributes[1].strip()))
            elif name == 'class':
                iteration = 1
                for class_name in value.split(" "):
                    new_tag.add_class(class_name)
            else:
                new_tag.add_attribute(Attribute(name, value))
        if tag_id in self.__tags.keys():
            if tag_id == "":
                tag_id = tag_type
            tag_id = self.get_id_for_type(tag_id)
            new_tag.set_id(tag_id)
        self.__tags[tag_id] = new_tag


    def get_id_for_type(self, tag_type):
        count = 0
        id = tag_type
        while id in self.__tags.keys():
            id = f'{tag_type}-{count}'
            count += 1
        return id

    def check_id(self, value):
        try:
            self.__tags[value] = ""
            return False
        except KeyError:
            return True
