from Parsers.Parser import Parser
from bs4 import BeautifulSoup
import requests
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
