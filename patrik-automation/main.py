# .env variables
import os
# loading dotenv variables
from dotenv import load_dotenv
load_dotenv()

# selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

from time import sleep


class Metakocka():    
    LOGIN_URL = "https://metakocka.si/prijava.html"
    USER = os.getenv("MK_USER")
    PASS = os.getenv("MK_PASS")
    
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.LOGIN_URL)
    
    def login(self):
        # retriving html elements
        email_input = self.driver.find_element(By.CSS_SELECTOR, '#ID_WPLOGIN input[name="Email"]')
        pass_input = self.driver.find_element(By.CSS_SELECTOR, '#ID_WPLOGIN input[name="Passwd"]')
        submit_btn = self.driver.find_element(By.CSS_SELECTOR, '#ID_WPLOGIN .wplogin-button-login')
        
        # filling form
        email_input.send_keys(self.USER)
        pass_input.send_keys(self.PASS)
        submit_btn.click()
    
    def open_sales_foreign(self):
         # Wait for the element to be clickable before attempting to interact with it
        sleep(5)
        links = self.driver.find_elements(By.CSS_SELECTOR, '.gwt-CubeGadget-Link_2')
        
        foreign_link = self.find_element_with_text(links, "Foreign")
        foreign_link.click()
    
    def search_foreign_invoice(self, what):
        sleep(5)
        search_input = self.driver.find_element(By.CSS_SELECTOR, "#x-auto-87-input")
        search_input.send_keys(what)
        
        
    @staticmethod    
    def find_element_with_text(elements, text):
        found_element = None
        for element in elements:
            if element.text == text:
                found_element = element
                break
        return found_element

    



metakocka = Metakocka()

metakocka.login()
metakocka.open_sales_foreign()
metakocka.search_foreign_invoice("1/2025")

sleep(100)
