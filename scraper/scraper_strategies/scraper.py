import re
from urllib.error import URLError, HTTPError
from urllib.request import urlopen

from html_classes import Tag
from html_classes.html_full import Html


class Scraper:

    def attempt_open(self, url):
        try:
            page = urlopen(url).read().decode("utf-8")
        except (URLError, UnicodeDecodeError, ConnectionError) as e:
            return None
        return page

    def scrape(self, args):
        result = []
        for url in args:
            page = self.attempt_open(url)

            if page is None:
                result.append(None)
                continue

            print(' scraping ', url)

            tag_regex = "<(.*?)>"

            html = Html()
            tags = re.findall(tag_regex, page)

            section = "head"
            table_rows = 0

            for tag in tags:
                # split by space and index 1 should be the tag type, do not save the delimited string as a list as it would be inacurrate for certain types
                tag_type = tag.split(" ")[0]
                if tag[0] == '/' or tag[0] == '!' or tag[0] == "=":
                    if tag_type == '/table':
                        table_rows = 0
                    continue
                new_tag = Tag(tag_type)

                if tag_type == "html":
                    try:
                        html.set_language(tag.split("=")[1].replace('"', ""))
                    except IndexError:
                        html.set_language("N/A")
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
                        html.set_title("N/A")
                    continue
                elif tag_type == 'tr':
                    table_rows += 1
                    if table_rows > 50:
                        result.append(None)
                        break
                else:
                    html.add_tag(tag, section)
            result.append(html)
        return result
