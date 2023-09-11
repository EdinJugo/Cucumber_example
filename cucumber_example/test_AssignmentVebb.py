from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.selenium.dev/selenium/web/web-form.html")


radio_elements = driver.find_elements(By.XPATH, "//input[@type = 'radio']")

i = 0
j = 0

for i in range (len(radio_elements)):
    radio_elements[i].click()
    print("Radio click " + str (i+1))

    for j in range (len(radio_elements)):
        if i != j:
            if radio_elements[j].is_selected():

                print("Radio " + str(j+1) + " is checked" )

            else:
                print("Radio " + str(j+1) + " is not checked" )

            
    
