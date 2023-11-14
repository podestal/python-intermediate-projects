from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://en.wikipedia.org/wiki/Main_Page')

driver.maximize_window()

interaccions = driver.find_element(By.CSS_SELECTOR, value='div#articlecount a')
# interaccions.click()

view_source = driver.find_element(By.PARTIAL_LINK_TEXT, value='View source')
# view_source.click()

search_bar = driver.find_element(By.NAME, value='search')
search_bar.send_keys('Python')
search_bar1 = driver.find_element(By.NAME, "search")
search_bar1.send_keys(Keys.ENTER)

# driver.quit()
