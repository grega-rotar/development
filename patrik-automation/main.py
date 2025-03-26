from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()

driver.get("https://example.com")

element = driver.find_element(By.XPATH, "/html/body/div/p[2]/a")
element.click()
sleep(100)
