import pytest
from pages.login_page import LoginPage
from selenium.webdriver.chrome.webdriver import WebDriver


class TestLoginPage:

    def test_login_positive(self, driver):
        page = LoginPage(driver)
        page.open()
        page.fill_login_form(email="and@ex.com", password="123")
        page.click_login_button()

        # Verification — for example, URL or absence of error message
        assert not page.is_login_error_visible(), "Login error should NOT be visible"
        assert page.is_visible(page.HEADER_LOGOUT), "Logout button should be visible after login"
        assert page.is_visible(page.HEADER_DELETE_ACCOUNT), "Delete Account button should be visible after login"

    def test_login_negative(self, driver):
        page = LoginPage(driver)
        page.open()
        page.fill_login_form(email="wrong@example.com", password="badpass")
        page.click_login_button()

        # Verify that the login error message is displayed
        assert page.is_login_error_visible(), "Login error should be visible"

    def test_signup_positive(self, driver):
        page = LoginPage(driver)
        page.open()
        page.fill_signup_form()
        page.click_signup_button()

        # Navigate to account information page (signup success)
        assert page.is_signup_success_visible(), "Signup success message should be visible"

    def test_signup_negative(self, driver):
        page = LoginPage(driver)
        page.open()
        # Known existing email
        page.fill_signup_form(name="Existing User", email="and@ex.com")
        page.click_signup_button()

        assert page.is_signup_error_visible(), "Signup error message should be visible"