from src.scraped_site import ScrapedSite
import json   

def load_sites() -> list[ScrapedSite]:
    sites: list[ScrapedSite] = []
    
    with open("sites.json", "r") as file:
        sites_json = json.load(file)

        sites = [
            ScrapedSite(
                url=site["url"],
                name=site["name"],
                class_=site["class_"],
                shop=site["shop"]
            ) 
            for site in sites_json
        ]

    return sites