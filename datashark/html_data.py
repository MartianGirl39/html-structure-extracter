from html_classes.html_full import Html
from scraper.html_scraper import HtmlScraper
from scraper.scraper_strategies.scraper import Scraper


class HtmlData:

    __slots__ = ('__html')
    def __init__(self):
        self.__html = None

    def set_html_object(self, url):
        if(isinstance(url, str)):
            scraper = Scraper()
            self.__html = HtmlScraper().get_structure_from(url, scraper)
            return True
        elif(isinstance(url, Html)):
            self.__html = url
            return True
        return False

    def __check_valid_html(self):
        if self.__html == None:
            raise TypeError
    def get_tags_as_data(self):
        if not self.__tags == None:
            return self.__tags
        self.__check_valid_html()
        data = []
        row = {}
        for tag in self.__html.copy_tags():
            row['id'] = tag.get_id()
            row['type'] = tag.tag_type()
            row['class count'] = len(tag.class_names())
            row['styles count'] = len(tag.styles())
            row['attributes count'] = len(tag.attributes())
            data.append(row)
            row = {}
        return data

    def get_tag_as_data(self, tag):
        self.__check_valid_html()
        data = []
        row = {}
        row['id'] = tag.get_id()
        row['type'] = tag.tag_type()
        row['class count'] = len(tag.class_names())
        row['styles count'] = len(tag.styles())
        row['attributes count'] = len(tag.attributes())
        data.append(row)
        row = {}
        return data

    def get_styles_as_data(self):
        data = []
        row = {}
        for tag in self.__html.copy_tags():
            for style in tag.styles():
                row['tag_id'] = tag.get_id()
                row['tag type'] = tag.tag_type()
                row['style'] = style.name()
                row['value'] = style.value()
                data.append(row)
                row = {}
        return data

    def get_tag_styles_as_data(self, tag_id):
        self.__check_valid_html()
        data = []
        row = {}
        for style in self.__html.tag_style(tag_id):
            row['tag_id'] = tag_id
            row['tag type'] = self.__html.tag_type(tag_id)
            row['style'] = style.name()
            row['value'] = style.value()
            data.append(row)
            row = {}
        return data

    # actual useful data
    def get_tag_occurences(self):
        self.__check_valid_html()
        data = []
        row = {}
        for tag in self.__html.copy_tags():
            # check if row is not already existing in data
            index = self.__x_exists_in_data(tag.tag_type(), data)
            if index > -1:
                data[index]['count'] += 1
                continue
            row['tag'] = tag.tag_type()
            row['count'] = 1
            data.append(row)
            row = {}
        return data

    def get_style_occurences(self):
        self.__check_valid_html()
        data = []
        row = {}
        for tag in self.__html.copy_tags():
            # check if row is not already existing in data
            for style in tag.styles():
                index = self.__x_exists_in_data(style.name(), data)
                if index > -1:
                    data[index]['count'] += 1
                    continue
                row['tag'] = style.name()
                row['content'] = style.value()
                row['count'] = 1
                data.append(row)
                row = {}
        return data

    def get_tag_style_occurences(self, tag_id):
        self.__check_valid_html()
        data = []
        row = {}
        for style in self.__html.tag_style(tag_id):
            index = self.__x_exists_in_data(style.name(), data)
            if index > -1:
                data[index]['count'] += 1
                continue
            row['tag'] = style.name()
            row['content'] = style.value()
            row['count'] = 1
            data.append(row)
            row = {}
        return data

    def get_style_value_occurences(self):
        self.__check_valid_html()
        data = []
        row = {}
        for tag in self.__html.copy_tags():
            # check if row is not already existing in data
            for style in tag.styles():
                index = self.__x_exists_in_data(style.value(), data)
                if index > -1:
                    data[index]['count'] += 1
                    continue
                row['content'] = style.name()
                row['tag'] = style.value()
                row['count'] = 1
                data.append(row)
                row = {}
        return data

    def __x_exists_in_data(self, x, array):
        for i in range(0, len(array), 1):
            if x == array[i]['tag']:
                return i
        return -1