from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
import time


chromedriver_autoinstaller.install()

driver = webdriver.Chrome()

driver.get("https://www.google.co.in/")

search_bar = driver.find_element(By.CLASS_NAME, 'gLFyf')
search_bar.clear()

# add the search 
#search_text = input("Enter that you want to search ")
search_bar.send_keys("pc tower")
search_bar.send_keys(Keys.RETURN)
shoppingbutton =driver.find_element(By.XPATH, '//*[@id="hdtb-msb"]/div[1]/div/div[2]/a')
shoppingbutton.click()

list = driver.find_element(By.CLASS_NAME,'GhTN2e').find_elements(By.CLASS_NAME , 'KZmu8e')
for l in list:
    print(l.find_element(By.CLASS_NAME,'ljqwrc').text)
    #print(l.find_element(By.CLASS_NAME, 'translate-content').get_attribute('innerHTML'))

time.sleep(5)


