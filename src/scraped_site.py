from bs4 import BeautifulSoup
from requests import get
from datetime import datetime

class ScrapedSite():
    """
        Site Representation
    """

    def __init__(self, url: str, name: str, class_: str, shop: str) -> None:
        self.url = url
        self.name = name
        self.class_ = class_
        self.shop = shop
        self.date = None
        self.site = None

    def _get_site(self) -> BeautifulSoup:
        """Make a HTTP request to get price and parse the HTML"""
        
        response = get(self.url)
        soup = BeautifulSoup(response.text, "html.parser")

        return soup
    
    def _update_site(self):
        """Update the site"""

        self.site = self._get_site()

    def _update_now(self):
        """Update now info"""

        self.now = datetime.now().strftime("%d/%m/%Y %H:%M")

    def get_price(self) -> str:
        """Get price from the class_ element"""
        
        self._update_site()
        self._update_now()
        price = self.site.find(class_=self.class_).text
        
        self.price = price

        return price

    def to_list(self) -> list[str]:
        price = self.get_price()

        return [self.shop, self.name, self.now, price]