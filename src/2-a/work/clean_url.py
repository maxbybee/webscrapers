from urllib.parse import urlparse, urlunparse

def clean_url(url):
    # Parse the URL
    parsed_url = urlparse(url)

    # Create a new parsed URL with the cleaned components
    cleaned_url = parsed_url._replace(query=None, fragment=None)

    # Unparse the cleaned URL
    result_url = urlunparse(cleaned_url)

    return result_url


if __name__ == '__main__':

    url_to_clean = "https://www.ebay.com/itm/254078693996?hash=item3b2845326c:g:Ob0AAOSwfyxlQNY2&amdata=enc%3AAQAIAAAA4AmiyrgFsOBpYl2KNgTiLWr3hTIItST2kpZOUDA033mDzuhBTg5UK4H5uXAO5H03yjdkELJtKJttKzy0%2BpWjeAWcvk3whBeKnjDGg1F483ijgIlflt%2BZdatHwsqhxlrict%2BHuMrU3WLeUJ3%2FoKUszQ0YdaZLswvBWs%2BQAr8cHMu1Vt38ufEPxQflyyKkiC%2FED6vA7XGpDKJDh99w7bBaYNxRX7j0kX6GBhUSudN251c%2Ft77PpUDNU%2B1ejWUkR%2FT4VL8f85w%2FZRCbbM3aN3UwdWATBF9nOf7Kq6H7j9eqgLLS%7Ctkp%3ABFBM0PDZlIFj"
    cleaned_url = clean_url(url_to_clean)
    print(cleaned_url)
