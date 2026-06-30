from playwright.sync_api import Page

class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page
        self.first_name = page.locator('[data-test="firstName"]')
        self.last_name = page.locator('[data-test="lastName"]')
        self.zip_code = page.locator('[data-test="postalCode"]')
        self.continue_button = page.locator('[data-test="continue"]')
        self.error = page.locator('[data-test="error"]')
        self.finish_button = page.locator('[data-test="finish"]')
        self.confirmation_message = page.locator('[data-test="complete-text"]')

    def fill_form(self, first, last, zip_code):
        self.first_name.fill(first)
        self.last_name.fill(last)
        self.zip_code.fill(zip_code)
        self.continue_button.click()

    def get_error_message(self):
        return self.error.inner_text()
    
    def finish(self):
        self.finish_button.click()

    def order_confirmation(self):
        return self.confirmation_message.is_visible()