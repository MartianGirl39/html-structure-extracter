from html_classes import Tag
from html_classes.html_full import Html
from scraper.scraper_strategies.scraper import Scraper
import re


class BodyOnlyScraper(Scraper):

    def __init__(self):
        super().__init__()

    def scrape(self, args):
        result = []

        for url in args:

            page = self.attempt_open(url)

            if page is None:
                continue

            tag_regex = "<(.*?)>"

            html = Html()
            skip_to = page.find("/head")
            page = page[skip_to+5:]
            tags = re.findall(tag_regex, page)
            table_rows = 0
            # tags = tags[skip_to + 4:]

            for tag in tags:
                # split by space and index 1 should be the tag type, do not save the delimited string as a list as it would be inacurrate for certain types
                tag_type = tag.split(" ")[0]
                if tag[0] == '/' or tag[0] == '!' or tag[0] == "=":
                    continue
                new_tag = Tag(tag_type)
                html.add_tag(tag, "body")
            result.append(html)
        return result