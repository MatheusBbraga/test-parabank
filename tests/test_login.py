from pages.login_page import LoginPage
import pytest
from playwright.sync_api import expect


@pytest.mark.login
def test_login_sucesso(page, user_data):
    from pages.login_page import LoginPage

    login_page = LoginPage(page)

    login_page.navigate()
    login_page.login(user_data["username_input"], user_data["password_input"])


@pytest.mark.login
def test_campos_obrigatorios_nao_informados(page):

    login_page = LoginPage(page)

    login_page.navigate()

    login_page.login("", "")

    expect(login_page.error_message).to_have_text(
        "Please enter a username and password."
    )
