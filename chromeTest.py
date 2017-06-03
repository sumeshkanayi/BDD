from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
webPage=driver.get("http://www.amazon.co.uk")

element = driver.find_element_by_id("twotabsearchtextbox")
element.send_keys("Software Testing")
element.send_keys(Keys.RETURN)

driver.close()