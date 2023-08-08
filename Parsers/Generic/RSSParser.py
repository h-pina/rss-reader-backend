from Parsers.Parser import Parser
from bs4 import BeautifulSoup
import requests
from  datetime import datetime
import lxml
class RSSParser(Parser):
    
    def __init__(self) -> None:
        self.bs = None
        pass

    def getFeedFromUrl(self, url):
        r = requests.get(url)
        r.raise_for_status()
        self.bs = BeautifulSoup(r.text, features="xml")
        return self.bs 
    
    def parse(self, feed):
        results = []
        self.bs = BeautifulSoup(feed, features="xml")
        for item in self.bs.find_all("item"):
            pubDate = datetime.strptime(item.pubDate.text,"%a, %d %b %Y %H:%M:%S %z")
            results.append({
                'title':item.title.text,
                'link':item.link.text,
                'date': pubDate.strftime("%d-%m-%Y")
            })
        self.articlesList = results
        return results
