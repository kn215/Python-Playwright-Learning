from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from playwright.sync_api import expect

def test_get_item_names(page):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(page)

    names = inventory_page.get_item_names()

    assert len(names) == 6

def test_get_item_prices(page):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(page)

    prices = inventory_page.get_item_prices()

    assert len(prices) == 6
    assert all(isinstance(p, float) for p in prices)

def test_add_item(page):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(page)
    
    inventory_page.add_item("Sauce Labs Backpack")
    
    page.wait_for_timeout(2000)

    expect(inventory_page.cart_count).to_have_text("1")