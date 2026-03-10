import pytest
from faker import Faker

pytest_plugins = ("pytest_playwright",)

fake = Faker("la")

@pytest.fixture
def user_data():
    return {
        "username_input": "teste",
        "password_input": "testet123"
    }

@pytest.fixture
def user_register():
    password = fake.password(length=8)
    return {
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "address": fake.street_address(),
        "city": fake.city(),
        "state": fake.state_abbr(),
        "zip": fake.postcode(),
        "phone": fake.phone_number(),
        "ssn": fake.ssn(),
        "username": fake.user_name(),
        "password": password
    }

@pytest.fixture(scope="module")
def page(browser, browser_context_args):
    context = browser.new_context(**browser_context_args)
    page = context.new_page()
    yield page
    context.close()
