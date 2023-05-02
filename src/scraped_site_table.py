from prettytable import PrettyTable

from src.scraped_site import ScrapedSite

class ScrapedSiteTable:

    def __init__(self) -> None:
        self.table = PrettyTable([
            "Tienda", 
            "Producto", 
            "Fecha", 
            "Precio"
        ])

    def add_scraped_site(self, site: list[str]) -> None:
        """Add new row to the table"""

        self.table.add_row(site)
