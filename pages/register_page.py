from pages.base_page import BasePage


class RegisterPage(BasePage):

    URL = "https://parabank.parasoft.com/parabank/register.htm"

    def __init__(self, page):
        super().__init__(page)

        self.first_name = page.locator('input[name="customer.firstName"]')
        self.last_name = page.locator('input[name="customer.lastName"]')
        self.address = page.locator('input[name="customer.address.street"]')
        self.city = page.locator('input[name="customer.address.city"]')
        self.state = page.locator('input[name="customer.address.state"]')
        self.zip = page.locator('input[name="customer.address.zipCode"]')
        self.phone = page.locator('input[name="customer.phoneNumber"]')
        self.ssn = page.locator('input[name="customer.ssn"]')
        self.username = page.locator('input[name="customer.username"]')
        self.password = page.locator('input[name="customer.password"]')
        self.confirm_password = page.locator('input[name="repeatedPassword"]')
        self.register_button = page.locator('input[value="Register"]')

    def navigate(self):
        super().navigate(self.URL)

    def register(self, user):

        self.first_name.fill(user["first_name"])
        self.last_name.fill(user["last_name"])
        self.address.fill(user["address"])
        self.city.fill(user["city"])
        self.state.fill(user["state"])
        self.zip.fill(user["zip"])
        self.phone.fill(user["phone"])
        self.ssn.fill(user["ssn"])
        self.username.fill(user["username"])
        self.password.fill(user["password"])
        self.confirm_password.fill(user["password"])

        self.register_button.click()