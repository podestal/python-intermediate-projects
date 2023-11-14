from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.python.org/')

times = driver.find_elements(By.XPATH, value='//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li/time')
names = driver.find_elements(By.XPATH, value='//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li/a')

events = {}

for n in range(0, 5):
    events[n] = {'time': times[n].text, 'name': names[n].text}

driver.quit()