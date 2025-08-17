import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.signup_page import SignupPage
from selenium.webdriver.chrome.webdriver import WebDriver


class TestLoginPage:

    def test_correct_login_user(self, driver: WebDriver):
        home = HomePage(driver)
        login = LoginPage(driver)
        signup = SignupPage(driver)

        # 1-2. Launch browser and navigate to home page
        home.open()

        # 3. Verify that home page is visible
        assert home.is_home_page(), "Home page is not visible"
        assert home.is_home_url(), "Home url is incorrect"

        # 4. Click on 'Signup / Login'
        home.click_header_menu(home.HEADER_SIGNUP_LOGIN)

        # 5. Verify 'Login to your account' is visible
        assert login.is_login_header_visible(), "'Login to your account' header is not visible"

        # 6. Enter correct email address and password
        login.fill_login_form("and@ex.com", "123")

        # 7. Click 'login' button
        login.click_login_button()

        # 8. Verify 'Logged in as username'
        assert signup.is_logged_in_as_visible(), "'Logged in as username' is not visible"

        # 9. Click 'Delete Account'
        login.click_delete_account()

        # 10. Verify 'ACCOUNT DELETED!' and click continue
        assert login.is_account_deleted_visible(), "'Account Deleted!' message is not visible"
        signup.click_continue_button()









