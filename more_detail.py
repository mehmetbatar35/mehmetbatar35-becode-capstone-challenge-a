from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options = chrome_options)
driver.get('https://www.rtbf.be/en-continu')

WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "didomi-notice-disagree-button"))
).click()

driver.maximize_window()


urls = []
contents = []

while len(urls) < 600:
    titles = driver.find_elements(By.CSS_SELECTOR, "h3.card-title a.stretched-link")    
    for title in titles:
        urls.append(title.get_attribute('href'))
    print(len(urls))
    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.border-yellow-500.bg-yellow-500"))
    )
    button.click()


for i, url in enumerate(urls, start=1):
    driver.get(url)
    first_paragraph = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.js-block-text.prose p:first-of-type")))
    contents.append(first_paragraph.text)


data = {'URL': urls, 'Content': contents}
df = pd.DataFrame(data)
df.to_csv("more_detail.csv", index=False, encoding='utf-8')
print('Data saved to more_detail.csv')







driver.quit()
