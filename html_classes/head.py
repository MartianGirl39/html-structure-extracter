from html_classes.script import Script
import re


class Head:
    __slots__ = ('__meta', '__scripts', '__charset')

    def __init__(self):
        self.__meta = {}
        self.__scripts = []
        self.__charset = ""

    def meta(self, meta_name):
        for data in self.__meta:
            if data[meta_name] == meta_name:
                return data[meta_name]
        return ""

    def add_meta(self, meta_name, content):
        self.__meta[meta_name] = content

    def script_with_rel_of(self, rel):
        matching_scripts = []
        for script in self.__scripts:
            if script.rel() == rel:
                matching_scripts.append(script.src())
        return matching_scripts

    def script_with_file_type_of(self, file_type):
        matching_scripts = []
        for script in self.__scripts:
            if script.type() == file_type:
                matching_scripts.append(script.src())
        return matching_scripts

    def scripts(self):
        return self.__scripts.copy()

    def add_script(self, rel, src, file_type):
        self.__scripts.append(Script(rel, src, file_type))

    def title(self):
        return self.__title

    def charset(self):
        return self.__charset

    def set_title(self, title):
        self.__title = title

    def add_tag(self, tag):
        tag_type = tag.split(" ")[0].strip()
        data = re.split(r'="|=\'|" |\' ', tag[len(tag_type):])

        #print("tag type is ", tag_type)
        for i in range(1, len(data), 2):
            name = data[i-1].strip()
            value = data[i].replace('"', "").replace("'", "").strip()
            if tag_type == 'meta':
                meta_id = ""
                if name == 'charset':
                    self.__charset = value
                elif name == 'name' or name == 'property':
                    self.__meta[value] = ""
                    meta_id = value
                    #print(meta_id)
                elif name == 'content':
                    self.__meta[meta_id] = value
            elif tag_type == 'script' or tag_type == 'link':
                rel = ""
                type = ""
                src = ""
                if name == 'rel' or name == 'type':
                    rel = value
                elif name == 'src' or name == 'href':
                    src = value
                    if rel == "" and name == 'src':
                        rel = 'text/javascript'

                if rel == 'stylesheet':
                    type = 'css'
                elif rel == 'text/javascript':
                    type = 'javascript'
                self.__scripts.append(Script(rel, src, type))
