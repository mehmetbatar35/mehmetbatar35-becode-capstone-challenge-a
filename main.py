from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options = chrome_options)
driver.get('https://www.rtbf.be/en-continu')

WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "didomi-notice-disagree-button"))
).click()



all_titles = []   
all_contents = []  


while len(all_titles) < 2000 and len(all_contents) < 2000:
    titles = driver.find_elements(By.CSS_SELECTOR, "h3.card-title a.stretched-link")
    contents = driver.find_elements(By.CSS_SELECTOR, "p.text-14")
    for title in titles:
        all_titles.append(title.text)
    for content in contents:
        all_contents.append(content.text)
    articles = list(zip(all_titles, all_contents))
    button = driver.find_element(By.CSS_SELECTOR, "button.border-yellow-500.bg-yellow-500")
    button.click()


for i in articles:
    print(i)
print(len(articles))    

driver.quit()







        
