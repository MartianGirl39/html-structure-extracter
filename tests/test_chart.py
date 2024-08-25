import unittest

from data import chart
from data.chart import Plot
from data.html_data import HtmlData
import numpy as np

class MyTestCase(unittest.TestCase):
    def test_tag_occurences(self):
        data = HtmlData()
        data.set_html_object("https://www.w3schools.com/")
        occurences = data.get_tag_occurences()
        self.assertEqual(True, np.unique([x.items() for x in occurences]).size == len(occurences))

    def test_tag_occurences(self):
        plot = Plot("https://www.w3schools.com/")
        plot.get_tag_occurences()

    def test_style_occurences_plot(self):
        data = HtmlData()
        data.set_html_object("https://www.w3schools.com/")
        occurences = data.get_style_occurences()
        self.assertEqual(True, np.unique([x.items() for x in occurences]).size == len(occurences))

    def test_style_occurences_plot(self):
        plot = Plot("https://www.w3schools.com/")
        plot.get_style_occurences()

    def test_tag_style_occurences_plot(self):
        data = HtmlData()
        data.set_html_object("https://www.w3schools.com/")
        occurences = data.get_tag_style_occurences()
        self.assertEqual(True, np.unique([x.items() for x in occurences]).size == len(occurences))

    def test_tag_style_occurences_plot(self):
        plot = Plot("https://www.w3schools.com/")
        plot.get_tag_style_occurences("topnav")

    def test_tag_value_occurences_plot(self):
        plot = Plot("https://www.w3schools.com/")
        plot.get_style_value_occurences()

if __name__ == '__main__':
    unittest.main()
