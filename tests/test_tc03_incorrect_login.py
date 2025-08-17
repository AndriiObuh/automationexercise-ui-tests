import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from selenium.webdriver.chrome.webdriver import WebDriver


class TestLoginPage:

    def test_incorrect_login(self, driver: WebDriver):
        home = HomePage(driver)
        login = LoginPage(driver)

        # 1-2. Launch browser and navigate to home page
        home.open()

        # 3. Verify that home page is visible
        assert home.is_home_page(), "Home page is not visible"
        assert home.is_home_url(), "Home url is incorrect"

        # 4. Click on 'Signup / Login'
        home.click_header_menu(home.HEADER_SIGNUP_LOGIN)

        # 5. Verify 'Login to your account' is visible
        assert login.is_login_header_visible(), "'Login to your account' header is not visible"

        # 6. Enter incorrect email address and password
        login.fill_login_form("and@ex123.com", "123777")

        # 7. Click 'login' button
        login.click_login_button()

        # 8. Verify error 'Your email or password is incorrect!' is visible
        assert login.is_login_error_visible(), "'Your email or password is incorrect!' is not visible"