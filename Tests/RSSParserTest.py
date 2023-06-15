from Parsers.Generic.RSSParser import RSSParser
import unittest
from bs4 import BeautifulSoup as bs

class RSSParserTest(unittest.TestCase):
    def setUp(self) -> None:
        self.parser = RSSParser()
        
    def test_get_feed_from_url(self):
        parser = self.parser
        goodUrl = 'https://news.ycombinator.com/rss'
        badUrl = 'https://asdfajhkfhaskjfasjfa/feed'

        feed = parser.getFeedFromUrl(goodUrl)
        
        self.assertGreater(len(feed.find('rss').text), 0)
        with self.assertRaises(Exception):
            parser.getFeedFromUrl(badUrl)

    def test_parse_data_from_feed(self):
        expectedResult = [{
            'title': 'Native JSON Output from GPT-4',
            'link': 'https://yonom.substack.com/p/native-json-output-from-gpt-4',
            'date': '14-06-2023'
        },
        {
            'title': 'Gorilla: Large Language Model Connected with APIs',
            'link': 'https://shishirpatil.github.io/gorilla',
            'date': '14-06-2023'
        }]

        #TODO: Finish writing this test and the functionality (maybe add other xml formats??)

    def test_save_parsed_data_to_db(self):
        pass

    

if __name__ == '__main__':
    unittest.main()