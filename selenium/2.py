from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get("File:///C:/Users/Administrator/Desktop/flask/selenium/copy.html")

try:
    element1=driver.find_element_by_name("msg1")
    elements.send_keys("Shafeeq is BACK")
    print("==========================>")

except NoSuchElementException:
    print("oops George has created the element with the name of msg1")

time.sleep(3)
driver.quit()