from selenium import webdriver
from selenium.webdriver.common.by import By
from chrome_options import ChromeOptions

chrome_options = ChromeOptions()
driver = webdriver.Chrome(options=chrome_options.get_options())



driver.quit()