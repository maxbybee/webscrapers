import requests
from bs4 import BeautifulSoup
from clean_url import clean_url

def scrape_ebay(query):
    # eBay search URL
    url = f'https://www.ebay.com/sch/i.html?_nkw={query.replace(" ", "+")}'

    # Make the request to eBay
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract content within div elements with class s-item__info
        title_divs = soup.find_all('div', class_='s-item__info')

        # Check if there are no titles
        if not title_divs:
            print("No titles found. Check if the HTML structure or class names have changed.")
            return []

        product_info_list = []

        for title_div in title_divs:
            title_text = title_div.find('div', class_='s-item__title').text.strip()

            # Skip titles containing "Shop on eBay"
            if "Shop on eBay" in title_text:
                continue

            # Extract product information
            product_name_tag = title_div.find('div', class_='s-item__title').find('span', {'role': 'heading', 'aria-level': '3'})
            product_price = title_div.find('span', class_='s-item__price')
            product_description = title_div.find('div', class_='s-item__subtitle')
            shipping_info = title_div.find('span', class_='s-item__shipping')
            logistics_cost = title_div.find('span', class_='s-item__logisticsCost')
            product_link = title_div.find('a', class_='s-item__link').get('href')
            if product_name_tag and product_price:
                product_info = {
                    "name": product_name_tag.text.strip() if product_name_tag else "N/A",
                    "price": product_price.text.strip() if product_price else "N/A",
                    "description": product_description.text.strip() if product_description else "N/A",
                    "shipping_info": shipping_info.text.strip() if shipping_info else "N/A",
                    "logistics_cost": logistics_cost.text.strip() if logistics_cost else "N/A",
                    "product_link": clean_url(product_link.strip()) if product_link else "N/A"

                }
                product_info_list.append(product_info)

        return product_info_list

    else:
        print(f"Error {response.status_code}: {response.text}")
        return []



if __name__ == '__main__':
    # Example query
    query = "laptop"
    
    # Get product information from eBay using BeautifulSoup
    product_info_array = scrape_ebay(query)
    
    # View the array of product information
    for index, product_info in enumerate(product_info_array, start=1):
        print(f"Product {index} Information: {product_info}")
    