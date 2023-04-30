from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

web = 'https://twitter.com/'
path = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(path)

driver.get(web)
driver.maximize_window()
time.sleep(5)

login = driver.find_element_by_xpath('//a[contains(@href, "/login")]')
login.click()
time.sleep(5)

username = driver.find_element_by_xpath('//input[contains(@autocomplete, "username")]')
username.click()
username.send_keys('ankit.patne25@gmail.com')

next = driver.find_element_by_xpath('//div[contains(@role, "button")][2]')
next.click()
time.sleep(2)

verify = driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
verify.send_keys('ankitbgmi12')
next_2 = driver.find_element_by_xpath('//div[@data-testid="ocfEnterTextNextButton"]')
next_2.click()

time.sleep(2)

password = driver.find_element_by_xpath('//input[@name="password"]')
password.send_keys('doraemon123')

login_click = driver.find_element_by_xpath('//div[@data-testid="LoginForm_Login_Button"]')
login_click.click()
time.sleep(5)
search_twitter = driver.find_element_by_xpath('//input[@placeholder="Search Twitter"]')
search_twitter.click()
search_twitter.send_keys('openai')
search_twitter.send_keys(Keys.ENTER)

# time.sleep(5)
tweets = WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.XPATH, '//article[@role="article"]')))

user_data = []
tweet_data = []
i = 1

def get_tweet(element):
    try:
        user = element.find_element_by_xpath(".//span[contains(text(), '@')]").text
        text = element.find_element_by_xpath(".//div[@lang]").text
        data = [user, text]
        
    
    except:
        data = ["user", "text"]

    return data
        

# tweets = driver.find_elements_by_xpath('//article[@role="article"]')
for tweet in tweets:
    try:
        cont_list = get_tweet(tweet)
        
        # text = " ".join(text.split())

        user_data.append(cont_list[0])
        tweet_data.append(" ".join(cont_list[1]))
        print(f'Tweet{i}')
        i+=1

    except:
        print("No Data")

time.sleep(2)
driver.quit()

df = pd.DataFrame()
df["Username"] = user_data
df["Tweet"] = tweet_data
df.to_csv("Twitter_data.csv", index=False)
print(df)
