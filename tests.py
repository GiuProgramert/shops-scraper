import unittest

from bs4 import BeautifulSoup

from src.scraper import load_sites
from src.scraped_site import ScrapedSite
from src.scraped_site_table import ScrapedSiteTable


class TestScraperSiteClass(unittest.TestCase):

    def setUp(self) -> None:
        self.site = ScrapedSite(
            url="https://nissei.com/py/auricular-jbl-tune-230nc-tws-bluetooth",
            name="Auricular JBL Tune 230NC TWS Bluetooth",
            class_="price",
            shop="Nissei"
        )

    def test_scraper_get_site(self):
        site_soap = self.site._get_site()

        self.assertIsInstance(site_soap, BeautifulSoup)

    def test_scraper_get_price(self):
        price = self.site.get_price()

        self.assertIsInstance(price, str)


class TestScraper(unittest.TestCase):

    def test_load_sites(self):
        sites = load_sites()

        valid = True

        if not isinstance(sites, list):
            valid = False

        if len(sites) == 0 and not isinstance(sites[0], ScrapedSite):
            valid = False

        self.assertEqual(valid, True)


class TestScrapedSiteTable(unittest.TestCase):
    
    def setUp(self):
        self.table = ScrapedSiteTable()
        
        self.site = ScrapedSite(
            url="https://nissei.com/py/auricular-jbl-tune-230nc-tws-bluetooth",
            name="Auricular JBL Tune 230NC TWS Bluetooth",
            class_="price",
            shop="Nissei"
        )

        self.maxDiff = None

    def test_add_scraped_site(self):        
        site_list = self.site.to_list()
        self.table.add_scraped_site(site_list)
        
        expected_output = str(self.table.table)
        self.assertEqual(
            expected_output, 
            "+--------+----------------------------------------+------------------+-------------+"
            "\n| Tienda |                Producto                |      Fecha       |    Precio   |"
            "\n+--------+----------------------------------------+------------------+-------------+"
            f"\n| Nissei | Auricular JBL Tune 230NC TWS Bluetooth | {self.site.now} | {self.site.price} |"
            "\n+--------+----------------------------------------+------------------+-------------+"
        )

if __name__ == '__main__':
    unittest.main()