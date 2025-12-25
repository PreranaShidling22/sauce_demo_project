from Pages.login_page import LoginPage
from Pages.inventory_page import InventoryPage
from Pages.cart_page import CartPage


def test_open_cart(driver):
    login = LoginPage(driver)
    login.open()
    login.login("standard_user","secret_sauce")

    inventory = InventoryPage(driver)
    inventory.is_inventory_page_loaded()
    inventory.add_backpack_to_cart()

    cart = CartPage(driver)
    cart.open_cart()
    assert "cart.html" in driver.current_url
    driver.close()

def test_is_cart_page_loaded(driver):
    login = LoginPage(driver)
    login.open()
    login.login("standard_user","secret_sauce")

    inventory = InventoryPage(driver)
    inventory.is_inventory_page_loaded()
    inventory.add_backpack_to_cart()
    cart = CartPage(driver)
    cart.open_cart()

    cart.is_cart_page_loaded()
    assert cart.is_cart_page_loaded()
    driver.close()
def test_is_product_present_in_cart(driver):
    login = LoginPage(driver)
    login.open()
    login.login("standard_user","secret_sauce")

    inventory = InventoryPage(driver)
    inventory.is_inventory_page_loaded()
    inventory.add_backpack_to_cart()
    cart = CartPage(driver)
    cart.open_cart()
    cart.is_product_present_in_cart()
    assert cart.is_product_present_in_cart()
    driver.close()

def test_remove_product_in_cart(driver):
    login = LoginPage(driver)
    login.open()
    login.login("standard_user","secret_sauce")
    inventory = InventoryPage(driver)
    inventory.is_inventory_page_loaded()
    inventory.add_backpack_to_cart()
    cart = CartPage(driver)
    cart.open_cart()
    cart.is_product_present_in_cart()
    cart.remove_product()
    assert not cart.is_product_present_in_cart()
    driver.close()

def test_is_product_in_cart(driver):
    login = LoginPage(driver)
    login.open()
    login.login("standard_user","secret_sauce")
    inventory = InventoryPage(driver)
    inventory.is_inventory_page_loaded()
    inventory.add_backpack_to_cart()
    cart = CartPage(driver)
    cart.open_cart()

    assert cart.is_product_present_in_cart()
    driver.close()