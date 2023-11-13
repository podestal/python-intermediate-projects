#1. Scrape the product
import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6',
                        headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
                                 "Accept-Language": "en-US,en;q=0.9"})
soup = BeautifulSoup(response.text, 'html.parser')

price = soup.select_one('span.a-offscreen').getText()
float_price = float(price.split('$')[1])

#2. Set an email alert with the best value