from time import sleep

from src.helpers import clear_console
from src.scraper import load_sites
from src.scraped_site_table import ScrapedSiteTable
# from src.helpers import separator


def main():
    sites = load_sites()
    scraped_site_table = ScrapedSiteTable()
    
    while True:
        
        for site in sites:
            site_list = site.to_list()
            scraped_site_table.add_scraped_site(site_list)

        clear_console()
        print(scraped_site_table.table)

        sleep(60 * 10)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()