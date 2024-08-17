import unittest

from html_classes import html_attr, Attribute


class MyHtmlAttr(unittest.TestCase):
    def test_init(self):
        attribute = Attribute("div", "main")
        self.assertEqual(attribute.name(), "div")# add assertion here
        self.assertEqual(attribute.value(), "main")

if __name__ == '__main__':
    unittest.main()
