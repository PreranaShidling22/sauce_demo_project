from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self,driver):
        self.driver = driver

    cart_icon = (By.CLASS_NAME, "shopping_cart_link")
    cart_title = (By.CLASS_NAME, "title")
    cart_item = (By.CLASS_NAME, "cart_item")
    remove_button = (By.ID,"remove-sauce-labs-backpack")
    cart_badge = (By.CLASS_NAME, "shopping_cart_badge")

    def open_cart(self):
        self.driver.find_element(*self.cart_icon).click()

    def is_cart_page_loaded(self):
        return self.driver.find_element(*self.cart_title).text == "Your Cart"

    def is_product_present_in_cart(self):
        element = self.driver.find_elements(*self.cart_item)
        return len(element)>0

    def remove_product(self):
        return self.driver.find_element(*self.remove_button).click() =="0"

    def is_product_in_cart(self):
        self.driver.find_elements(*self.cart_badge)
