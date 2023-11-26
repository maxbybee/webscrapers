
import json

# imports
from lev_distance import levenshtein_distance
from num_remove import keep_numbers_only
from clean_url import clean_url

# item requests
from scrape import scrape_ebay

if __name__ == '__main__':

    query = "Laptop"
    data = scrape_ebay(query)
    if data:
        for product in data:
            print(json.dumps(product, indent=2))