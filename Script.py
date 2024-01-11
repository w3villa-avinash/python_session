from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import chromedriver_autoinstaller

chromedriver_autoinstaller.install()
driver = webdriver.Chrome()
driver.get("https://www.python.org")
print(driver.title)
search_bar = driver.find_element("id","id-search-field")
search_bar.clear()
search_bar.send_keys("getting started with python")
search_bar.send_keys(Keys.RETURN)
print(driver.current_url)