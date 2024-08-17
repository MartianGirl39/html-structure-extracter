from dataclasses import dataclass
from urllib.request import urlopen
import re

from html_classes import Attribute, Tag
from html_classes.body import Body
from html_classes.head import Head
from html_classes.style import Style


class Html:
    __slots__ = ('__body', '__head', '__language', '__title')

    def __init__(self):
        self.__body = Body()
        self.__head = Head()
        self.__language = ""
        self.__title = ""

    def copy_tags(self):
        return self.__body.copy_tags()

    def tag_types(self):
        return self.__body.tag_types()

    def tag_of_type(self, tag_type):
        tags = []
        for tag in self.__body.tags():
            if tag.tag_type() == tag_type:
                tags.append(tag.get_id())
        return tags

    def tag_type(self, tag_id):
        for tag in self.__body.tags():
            if tag.get_id() == tag_id:
                return tag_id
        return ""

    def tag_attributes(self, tag_id):
        # attributes = []
        for tag in self.__body.tags():
            if tag.get_id() == tag_id:
                return tag.attributes()
        return []

    def tag_attribute_value(self, tag_id, attribute_type):
        for tag in self.__body.copy_tags():
            if tag.get_id() == tag_id:
                for attribute in tag.attributes():
                    if attribute == attribute_type:
                        return tag.attribute(attribute)
        return ""

    def tag_style_value(self, tag_id, style):
        tag = self.__body.get_tag(tag_id)
        return tag.style(style)

    def tag_style(self, tag_id):
        tag = self.__body.get_tag(tag_id)
        return tag.styles()

    def add_tag(self, tag, section):
        if section == 'body':
            self.__body.add_tag(tag)
        elif section == 'head':
            self.__head.add_tag(tag)

    def langauge(self):
        return self.__language

    def set_language(self, language):
        self.__language = language

    def get_classes(self, tag_id):
        tag = self.__body.get_tag(tag_id)
        return tag.class_names()

    def get_title(self):
        return self.__title

    def set_title(self, title):
        self.__title = title

    def get_charset(self):
        return self.__head.charset()

    def get_meta(self, name):
        return self.__head.meta(name)

    def get_scripts(self, rel):
        return self.__head.script_with_rel_of(rel)

    def get_scripts_of_type(self, type):
        return self.__head.script_with_file_type_of(type)