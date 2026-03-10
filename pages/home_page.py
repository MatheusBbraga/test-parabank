from pages.base_page import BasePage

class HomePage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.welcome_message = page.get_by_role("heading", name="Accounts Overview")
        self.logout_button = page.locator('a[href="logout.htm"]')
        self.success_message = page.get_by_text(
            "Your account was created successfully. You are now logged in."
        )

    def logout(self):
        self.logout_button.wait_for(state="visible")
        self.logout_button.click()
        # espera redirecionar para a tela de login
        self.page.wait_for_url("**/index.htm")

