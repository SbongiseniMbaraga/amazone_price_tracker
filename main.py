from bs4 import BeautifulSoup
import requests

URL = "https://www.amazon.com/Instant-Pot-Duo-Evo-Plus/dp/B07W55DDFB/ref=sr_1_1?qid=1597662463"
response = requests.get(URL, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.56", "Accept-Language": "en-US,en;q=0.9"})
website_html = response.text
soup = BeautifulSoup(website_html, "html.parser")

print(soup)
