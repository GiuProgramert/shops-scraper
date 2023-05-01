from time import sleep

from src.scraper import load_sites
from src.helpers import separator

def main():
    sites = load_sites()
    
    format_table = "|%15s | %50s | %35s | %20s|"

    separator()
    print(format_table % ("Tienda", "Producto", "Fecha", "Precio"))
    separator()
    
    while True:
        
        for site in sites:
            message = site.format(format_table)
            print(message)
 
        separator()  

        sleep(60 * 10)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()