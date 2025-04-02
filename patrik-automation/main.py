# .env variables
import os
# loading dotenv variables
from dotenv import load_dotenv
load_dotenv()

WAIT_TIME = 5

# selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
        try: 
            foregin_link_selector = '.gwt-CubeGadget-Link_2'
            # Waits up to 15 seconds until at least one element is found
            WebDriverWait(self.driver, 15).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, foregin_link_selector))
            )
            links = self.driver.find_elements(By.CSS_SELECTOR, foregin_link_selector)
            foreign_link = self.find_element_with_text(links, "Foreign")
        
            # Optional: Wait until the specific foreign link is clickable
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(foreign_link)
            )
            foreign_link.click()
                  
        except Exception as e:
            print(e)

    def search_open_foreign_invoice(self, invoice_num):
        try:
            search_input_selector = "#x-auto-87-input"
            WebDriverWait(self.driver, 15).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, search_input_selector))
            )
                        
            search_input = self.driver.find_element(By.CSS_SELECTOR, search_input_selector)
            search_input.send_keys(invoice_num)
            search_input.send_keys(Keys.RETURN)
            
            # waiting for search results
            # FIXME
            sleep(WAIT_TIME)
            
            search_results_invoices_query = "td.x-grid3-td-id_number > div"
            WebDriverWait(self.driver, 15).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, search_results_invoices_query))
            )
            search_results_invoices = self.driver.find_elements(By.CSS_SELECTOR, search_results_invoices_query)
            
            result_invoice = self.find_element_with_text(search_results_invoices, invoice_num)
            result_invoice.click()
            
            open_it_selector = ".x-btn-text"
            WebDriverWait(self.driver, 15).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, open_it_selector))
            )
            open_it = self.find_element_with_text(self.driver.find_elements(By.CSS_SELECTOR, open_it_selector), "Open it")
            open_it.click()
            
        except Exception as e:
            print(e)
    
    def extract_invoice_products(self):
        products_table_selector = ".gwt-MetaKockaMain-Forme-Table"
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, products_table_selector))
        )
        
        sleep(WAIT_TIME)
        products_table = self.driver.find_elements(By.CSS_SELECTOR, products_table_selector)[0]
        products_table_rows = products_table.find_elements(By.CSS_SELECTOR, "tbody > tr")
        
        for row in products_table_rows:
            print(row.text)
        
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
metakocka.search_open_foreign_invoice("1/2025")
metakocka.extract_invoice_products()

sleep(100)
