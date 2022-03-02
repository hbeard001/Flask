from selenium import webdriver
from selenium.webdrive.common.by import By
import time

driver=webdriver.Chrome()
driver.get("File:///C:/Users/Administrator/Desktop/flask/selenium/copy.html")
element1=driver.find_element_by_name("msg1")
elements.send_keys("Shafeeq is BACK")

time.sleep(5)
# Button1=driver.find_element_by_name("btn1")
Button1=driver.find_element(by=By.NAME, value="btn1")
Buttom1.click()
time.sleep(5)

Button2=Button1=driver.find_element(by=By.ID, value="B")
Buttom2.click()
time.sleep(5)

Button3=driver.find_element(by=By.NAME, value="btn3")
Buttom3.click()

element2=driver.find_element(by=By.NAME,value="nmsg2")
data=element2.get_attribute("value")
print("========================>",data)

element3=driver.find_element(by=By.ID,value="T")
data1=element3.text
print("========================>",data1)

time.sleep(3)
driver.quit()