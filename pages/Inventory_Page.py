from playwright.sync_api import Page

class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.item_container = page.locator(".inventory_item")
        self.item_name = page.locator(".inventory_item_name")
        self.item_price = page.locator(".inventory_item_price")
        self.sort_select = page.locator("[data-test='product-sort-container']")
        self.cart_button = page.locator("[data-test='shopping-cart-link']")
        self.cart_count = page.locator("[data-test='shopping-cart-badge']")
        self.side_menu = page.locator("#react-burger-menu-btn")

    def add_item(self, name: str):
        formatted = name.lower().replace(" ", "-")
        self.page.locator(f"[data-test='add-to-cart-{formatted}']").click()


    def goto(self):
        self.page.goto("https://www.saucedemo.com/inventory.html")

    def get_item_names(self):
        names = self.item_name.all()
        result = []
        for name in names:
            result.append(name.inner_text())
        return result
    
    def get_item_prices(self):
        prices = self.item_price.all()
        result = []
        for price in prices:
            text = price.inner_text()
            text = text.lstrip("$")
            text = float(text)
            result.append(text)
        return result
