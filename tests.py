import unittest

from bs4 import BeautifulSoup

from src.scraper import load_sites
from src.scraped_site import ScrapedSite


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

        # self.assertEqual(isinstance(site_soap, BeautifulSoup), True)
        self.assertIsInstance(site_soap, BeautifulSoup)

    def test_scraper_get_price(self):
        price = self.site.get_price()

        self.assertIsInstance(price, str)

    def test_scraper_format(self):
        format_table = "|%15s | %50s | %35s | %20s|"
        format = self.site.format(format_table)

        self.assertIsInstance(format, str)


class TestScraper(unittest.TestCase):

    def test_load_sites(self):
        sites = load_sites()

        valid = True

        if not isinstance(sites, list):
            valid = False

        if len(sites) == 0 and not isinstance(sites[0], ScrapedSite):
            valid = False

        self.assertEqual(valid, True)

if __name__ == '__main__':
    unittest.main()