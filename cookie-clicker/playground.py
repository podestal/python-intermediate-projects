from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep the browser open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)
# driver.get('https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1')
driver.get('https://www.python.org/')

# price_dollar = driver.find_element(By.CSS_SELECTOR, value="div#centerCol span.a-price-whole")
# price_cents = driver.find_element(By.CSS_SELECTOR, value="div#centerCol span.a-price-fraction")

# print(f"The price is {price_dollar.text}.{price_cents.text}")

search_bar = driver.find_element(By.NAME, value='q')
print(search_bar.get_attribute('placeholder'))
button = driver.find_element(By.ID, value='submit')
print(button.size)
# documentation_link = driver.find_element(By.CSS_SELECTOR, value='.documentation-widget a')
# print(documentation_link.text)
documentation_link = driver.find_element(By.XPATH, value='//*[@id="content"]/div/section/div[2]/div[3]/p[2]/a')
print(documentation_link.text)

# Closes a single active tab
# driver.close()

# Quit the entire browser
driver.quit()