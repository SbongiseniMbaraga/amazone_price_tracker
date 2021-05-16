from bs4 import BeautifulSoup
import requests

# gets the amazon product
URL = "https://www.amazon.com/SkyTech-Blaze-Gaming-Computer-Desktop/dp/B08VYVY71J/ref=sr_1_4?dchild=1&keywords=gaming+pc&qid=1621013372&sr=8-4"
response = requests.get(URL, headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.56",
    "Accept-Language": "en-US,en;q=0.9"})
website_html = response.text
soup = BeautifulSoup(website_html, "html.parser")

# get product price
def gets_price():
    find_price = soup.find(id="priceblock_ourprice").get_text()
    remove_dollar = find_price.split("$")[1]
    remove_comma = remove_dollar.replace(",", "")
    convert_to_num = float(remove_comma)

    return convert_to_num

# get product title
def gets_title():
    title = soup.find(id="productTitle").get_text()

    return title

# get product link
def gets_link():
    link = URL

    return link
