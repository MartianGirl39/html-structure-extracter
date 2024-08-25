
import pandas as pd
import matplotlib.pyplot as plt

from data.html_data import HtmlData

class Plot:
    def __init__(self, html):
        self.__data = HtmlData()
        self.__data.set_html_object(html)

    def set_html_object(self, html):
        self.__data.set_html_object(html)

    def get_tag_occurences(self):
        dist = pd.DataFrame(self.__data.get_tag_occurences())
        dist.plot(x='tag', y='count', kind='barh', xlabel='count', title='tag occurences')
        plt.show()

    def get_style_occurences(self):
        dist = pd.DataFrame(self.__data.get_style_occurences())
        dist.plot(x='tag', y='count', kind='barh', xlabel='count', title='styles occurences')
        plt.show()

    def get_tag_style_occurences(self, tag):
        dist = pd.DataFrame(self.__data.get_tag_style_occurences('topnav'))
        dist.plot(x='tag', y='count', kind='bar', xlabel='count', title='styles occurences by tag')
        plt.show()

    def get_style_value_occurences(self):
        dist = pd.DataFrame(self.__data.get_style_value_occurences()).head()
        dist.plot(x='tag', y='count', kind='barh', xlabel='count', title='style value occurences')
        plt.show()

