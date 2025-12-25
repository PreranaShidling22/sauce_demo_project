from selenium.webdriver.common.by import By
import time
class InventoryPage:
    def __init__(self, driver):
        self.driver = driver

    # Locators
    inventory_container = (By.CLASS_NAME, "inventory_list")
    add_to_cart_backpack = (By.ID, "add-to-cart-sauce-labs-backpack")
    cart_badge = (By.CLASS_NAME, "shopping_cart_badge")

    # Page actions
    def is_inventory_page_loaded(self):
        return self.driver.find_element(*self.inventory_container).is_displayed()

    def add_backpack_to_cart(self):
        self.driver.find_element(*self.add_to_cart_backpack).click()

    def get_cart_count(self):
        return self.driver.find_element(*self.cart_badge).text



