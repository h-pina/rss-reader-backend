from Parsers.Generic.RSSParser import RSSParser
import unittest
from unittest.mock import Mock
from Tests.Mocks.rssfeedMock import feedMock

#Redo those tests to assume that a instance of a RSSParser holds information for a specific rss feed
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

    def test_parse(self): 
        parserMock = Mock()
        parserMock.getFeedFromUrl.return_value = feedMock 
        feed = parserMock.getFeedFromUrl()
        result = self.parser.parse(feed)
        expectedResult = [{
            'title': 'Native JSON Output from GPT-4',
            'link': 'https://yonom.substack.com/p/native-json-output-from-gpt-4',
            'date': '14-06-2023'
        },
        {
            'title': 'Gorilla: Large Language Model Connected with APIs',
            'link': 'https://shishirpatil.github.io/gorilla/',
            'date': '14-06-2023'
        }]        
        self.assertListEqual(result,expectedResult)


if __name__ == '__main__':
    unittest.main()