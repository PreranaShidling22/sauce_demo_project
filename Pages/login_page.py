from selenium.webdriver.common.by import By
import time

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    username = (By.ID, "user-name")
    password = (By.ID, "password")
    login_btn = (By.ID, "login-button")

    def open(self):
        self.driver.get("https://www.saucedemo.com/")

    def login(self, user, pwd):
        self.driver.find_element(*self.username).send_keys(user)
        self.driver.find_element(*self.password).send_keys(pwd)
        time.sleep(5)
        self.driver.find_element(*self.login_btn).click()
        time.sleep(5)
        print("login button clicked")
