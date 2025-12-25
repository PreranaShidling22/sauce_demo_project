import time

from Pages.login_page import LoginPage
from Pages.inventory_page import InventoryPage

def test_inventory_page_loaded(driver):
    login = LoginPage(driver)
    login.open()
    login.login("standard_user", "secret_sauce")

    inventory = InventoryPage(driver)

    assert inventory.is_inventory_page_loaded()
    print("Inventory Page Loaded")
    driver.close()

def test_add_backpack_to_cart(driver):
    login = LoginPage(driver)
    login.open()
    login.login("standard_user", "secret_sauce")
    inventory = InventoryPage(driver)
    inventory.add_backpack_to_cart()

    assert inventory.get_cart_count() == "1"
    driver.close()
def test_get_cart_count(driver):
    login = LoginPage(driver)
    login.open()
    login.login("standard_user", "secret_sauce")
    inventory = InventoryPage(driver)
    inventory.add_backpack_to_cart()
    inventory.get_cart_count()
    assert inventory.get_cart_count() == "1"
    driver.close()


