from html_classes import Tag
from html_classes.html_full import Html
from scraper.scraper_strategies.scraper import Scraper
import re


class BlindScraper(Scraper):
    def scrape(self, args):
        result = []

        for url in args:

            page = self.attempt_open(url)

            if page is None:
                continue

            tag_regex = "<(.*?)>"

            html = Html()
            tags = re.findall(tag_regex, page)

            section = "head"
            table_rows = 0

            for tag in tags:
                # split by space and index 1 should be the tag type, do not save the delimited string as a list as it would be inacurrate for certain types
                tag_type = tag.split(" ")[0]
                if tag[0] == '/' or tag[0] == '!' or tag[0] == "=":
                    continue
                new_tag = Tag(tag_type)

                if tag_type == "html":
                    html.set_language(tag.split("=")[1].replace('"', ""))
                    continue
                    # check if type is head or body and set a flag
                elif tag_type == "head":
                    section = "head"
                    continue
                    # check if type is style and is not empty and set flag
                elif tag_type == "body":
                    section = "body"
                    continue
                elif tag_type == 'title':
                    try:
                        html.set_title(re.findall(r'<title>(.*?)</title>', page)[0])
                    except IndexError:
                        html.__title = "N/A"
                        continue
                else:
                    html.add_tag(tag, section)
            result.append(html)
        return result
