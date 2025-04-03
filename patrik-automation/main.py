# .env variables
import os
import json
# loading dotenv variables
from dotenv import load_dotenv
load_dotenv()

WAIT_TIME = 2

# selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class Product():
    code = None
    name = None
    quantity = None
    price = None
    discount = None
    
    def to_json(self):
        return json.dumps(self.__dict__)

class Metakocka():    
    LOGIN_URL = "https://metakocka.si/prijava.html"
    USER = os.getenv("MK_USER")
    PASS = os.getenv("MK_PASS")
    
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.LOGIN_URL)
        self.actions = ActionChains(self.driver)
    
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
        products_table_rows.pop(0)
        
        products_list = []
        
        for row in products_table_rows:
            if row.text == "":
                None
            else:                
                product_data = row.text.split("\n")
                product = Product()
                product.code  = product_data[1].split(" - ")[0]
                product.name  = product_data[1].split(" - ")[1]
                product.quantity = int(product_data[2])
                product.price = self.currency_to_num(product_data[4])
                
                products_list.append(product.to_json())
        return products_list
    
    def get_invoice_amount(self):
        selector = ".gwt-MetaKockaMain-RacuniNarocilnicaPrevzemnicaSumComp-Table .gwt-MetaKockaMain-Forme-Labels"
        elements = self.driver.find_elements(By.CSS_SELECTOR, selector)
        
        total_amount_index = self.find_element_with_text_index(elements, "Total amount (EUR) :")
        
        total_amount = elements[total_amount_index + 1].text
        total_amount = self.currency_to_num(total_amount)
        print(total_amount)
        
        return total_amount
        
    
    def add_freight_cost(self):
        # press Ctrl+E
        self.actions.key_down(Keys.CONTROL).send_keys('e').key_up(Keys.CONTROL).perform()
        add_product_btn_selector = ".gwt-Anchor"
        add_product_btn = self.driver.find_elements(By.CSS_SELECTOR, add_product_btn_selector)
        add_product_btn = self.find_element_with_text(add_product_btn, "Add a product")
        
        add_product_btn.click()
        
        sleep(WAIT_TIME)
        # search_element_selector = "#x-auto-996-input"
        # WebDriverWait(self.driver, 15).until(
        #     EC.presence_of_all_elements_located((By.CSS_SELECTOR, search_element_selector))
        # )
        # search_element = self.driver.find_element(By.CSS_SELECTOR, search_element_selector)
        # search_element.send_keys("SHIPPING")
        self.actions.send_keys("SHIPPING").perform()
        sleep(WAIT_TIME)
        self.actions.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
        
    @staticmethod    
    def find_element_with_text(elements, text):
        found_element = None
        for element in elements:
            if text == element.text:
                found_element = element
                break
        return found_element
    
    @staticmethod
    def find_element_with_text_index(elements, text):
        found_element_index = None
        for index, element in enumerate(elements):
            if text == element.text:
                found_element_index = index
                break
        return found_element_index

    @staticmethod
    def currency_to_num(currency_str):
        return float(currency_str.replace(".", "").replace(",", "."))
    

    



metakocka = Metakocka()

metakocka.login()
metakocka.open_sales_foreign()
metakocka.search_open_foreign_invoice("1/2025")
metakocka.extract_invoice_products()

metakocka.get_invoice_amount()

metakocka.add_freight_cost()

sleep(100000)
