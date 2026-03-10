import pytest
from playwright.sync_api import expect
from pages.register_page import RegisterPage
from pages.home_page import HomePage


@pytest.mark.register
def test_register_sucesso(page, user_register):

    register_page = RegisterPage(page)
    home_page = HomePage(page)

    register_page.navigate()

    register_page.register(user_register)

    expect(home_page.success_message).to_be_visible()

    home_page.logout()
    