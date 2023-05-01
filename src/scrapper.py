from src.scrapped_site import ScrappedSite
import json   

def load_sites() -> list[ScrappedSite]:
    sites: list[ScrappedSite] = []
    
    with open("sites.json", "r") as file:
        sites_json = json.load(file)

        sites = [
            ScrappedSite(
                url=site["url"],
                name=site["name"],
                class_=site["class_"],
                shop=site["shop"]
            ) 
            for site in sites_json
        ]

    return sites