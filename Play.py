import os
from selenium.webdriver.common.by import By
from selenium import webdriver
os.environ['PATH'] += r"C:\Selenium"

driver = webdriver.Chrome()
driver.get("https://www.pexels.com/photo/sea-flight-dawn-sunset-16884742/")
driver.implicitly_wait(2000)
btton=driver.find_element(By.CLASS_NAME,"dropdown_wrapper__0W_Kf")
btton.click()
driver.quit()