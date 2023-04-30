from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()   # option in lower case on LHS
options.headless = False  #doesnt show browser when opened when True
options.add_argument('window-size=1920x1080')  # we dont use maximize_window() because it doesnt work well with headless = true

web = "https://www.audible.com/adblbestsellers?ref=a_search_t1_navTop_pl0cg1c0r0&pf_rd_p=8a113f1a-dc38-418d-b671-3cca04245da5&pf_rd_r=56B0J7P2EYN26AW42ANW&pageLoadId=OTjNrVXE6GwATpBB&creativeId=1642b4d1-12f3-4375-98fa-4938afc1cedc"

path = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(path, options=options)

driver.get(web)
driver.maximize_window()

change_country = driver.find_element_by_xpath('//div[contains(@id, "notification-banner-message")]/span/a')
change_country.click()

# Pagination
pagination = driver.find_element_by_xpath('//ul[contains(@class, "pagingElements")]')
pages = pagination.find_elements_by_xpath('li')
last_page = int(pages[-2].text)   #to get the total number of pages i.e. the last page




current_page = 1

audio_title = []
audio_author = []
audio_length = []
i = 1

while current_page <= last_page:

    # time.sleep(3)    # wait for some time to render the page
    # container = driver.find_element_by_class_name('adbl-impression-container')
    container = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'adbl-impression-container')))

    # products = container.find_elements_by_xpath('.//li[contains(@class, "productListItem")]')   # . represents current container and / represent immediate next tag li 
    products = WebDriverWait(container, 5).until(EC.presence_of_all_elements_located((By.XPATH, './/li[contains(@class, "productListItem")]')))

    for product in products:
        try:
            audio_title.append(product.find_element_by_xpath('.//h3[contains(@class, "bc-heading")]').text)   # . is important before //
            audio_author.append(product.find_element_by_xpath('.//li[contains(@class, "authorLabel")]').text )  
            audio_length.append(product.find_element_by_xpath('.//li[contains(@class, "runtimeLabel")]').text)   
            print("Book ", i)
            i+=1
            
        
        except:
            print("<--------Some error occured--------->")
    
    try:
        current_page+=1
        next_page = driver.find_element_by_xpath('//span[contains(@class, "nextButton")]')
        next_page.click()

    except:
        pass
        

df = pd.DataFrame()
df['Audio Title'] = audio_title
df['Author'] = audio_author
df['Length'] = audio_length

df.to_csv('Audio_Books.csv', index=False)
print(df)

time.sleep(5)
driver.quit()
   

