from pytest_playwright.pytest_playwright import page

from pages.base_page import BasePage


class LoginPage(BasePage):

    URL = "https://parabank.parasoft.com/parabank/index.htm"

    def __init__(self, page):
        super().__init__(page)

        self.username = page.locator('input[name="username"]')
        self.password = page.locator('input[name="password"]')
        self.login_button = page.locator('input[value="Log In"]')
        self.error_message = page.locator("p.error")

    def navigate(self):
        super().navigate(self.URL)

    def login(self, username, password):
        self.username.fill(username)
        self.password.fill(password)
        self.login_button.click()
