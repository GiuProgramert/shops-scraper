from bs4 import BeautifulSoup
from requests import get
from datetime import datetime

class ScrappedSite():
    """
        Site Representation
    """

    def __init__(self, url: str, name: str, class_: str, shop: str) -> None:
        self.url = url
        self.name = name
        self.class_ = class_
        self.shop = shop
        self.site = None

    def _get_site(self) -> BeautifulSoup:
        """Make a HTTP request to get price and parse the HTML"""
        
        response = get(self.url)
        soup = BeautifulSoup(response.text, "html.parser")

        return soup
    
    def _update_site(self):
        """Update the site"""

        self.site = self._get_site()

    def get_price(self) -> str:
        """Get price from the class_ element"""
        
        self._update_site()
        price = self.site.find(class_=self.class_).text
        
        self.price = price

        return price

    def format(self, format) -> str:
        now = datetime.now().strftime("%d/%m/%Y %H:%M")
        return format % (self.shop, self.name, now, self.get_price())