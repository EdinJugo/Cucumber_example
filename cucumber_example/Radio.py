from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("https://www.selenium.dev/selenium/web/web-form.html")


status = driver.find_element (By.XPATH, "//input[@type = 'radio']")

driver.find_element (By.ID, "my-radio-1").click()
print("Radio one is checked")

blue_checkbox_field2 = driver.find_element (By.ID, "my-radio-2") 


if blue_checkbox_field2.is_selected():

    print("Radio two is checked ")

else:
    print("Radio two is not checked")




driver.find_element (By.ID, "my-radio-2").click()
print("Radio two is checked")

blue_checkbox_field1 = driver.find_element (By.ID, "my-radio-1")     


if blue_checkbox_field1.is_selected():
    
    print("Radio one is checked")

else:
    print("Radio one is not checked")    



driver.quit()

