from bs4 import BeautifulSoup
import requests

URL = "https://www.amazon.com/SkyTech-Blaze-Gaming-Computer-Desktop/dp/B08VYVY71J/ref=sr_1_4?dchild=1&keywords=gaming+pc&qid=1621013372&sr=8-4"
response = requests.get(URL, headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.56",
    "Accept-Language": "en-US,en;q=0.9"})
website_html = response.text
soup = BeautifulSoup(website_html, "html.parser")

# get price of item
def gets_price():
    web_price = soup.find_all(name="span", class_="a-size-medium a-color-price priceBlockBuyingPriceString")
    separated_price = str(web_price).split(" ")
    separate_again = separated_price[4]
    separate_again2 = separate_again.split(">")
    separate_again3 = separate_again2[1]
    separate_again4 = separate_again3.split("<")
    separate_again5 = separate_again4[0]
    separate_again6 = separate_again5.split("$")
    price_replaced = separate_again6[1].replace(",", "")
    price_replace_d = price_replaced.replace(".", "")

    return int(price_replace_d)

print(gets_price())
