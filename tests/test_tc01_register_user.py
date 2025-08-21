import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.signup_page import SignupPage
from selenium.webdriver.chrome.webdriver import WebDriver


class TestSignupPage:

    def test_register_user(self, driver: WebDriver, person_data):
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

        # 5. Verify 'New User Signup!' is visible
        assert login.is_signup_header_visible(), "'New User Signup!' header is not visible"

        # 6. Enter name and email
        login.fill_signup_form(person_data.name, person_data.email)

        # 7. Click 'Signup' button
        login.click_signup_button()

        # 8. Verify 'ENTER ACCOUNT INFORMATION' is visible
        assert login.is_signup_success_visible(), "'Enter Account Information' header is not visible"

        # 9-12. Fill all account details on SignupPage
        signup.fill_registration_form(person_data)

        # 13-14. Click 'Create Account' and verify 'ACCOUNT CREATED!'
        assert signup.is_account_created(), "'Account Created!' header is not visible"

        # 15. Click 'Continue' button
        signup.click_continue_button()

        # 16. Verify 'Logged in as username'
        assert signup.is_logged_in_as_visible(), "'Logged in as username' is not visible"

        # 17. Click 'Delete Account'
        login.click_delete_account()

        # 18. Verify 'ACCOUNT DELETED!' and click continue
        assert login.is_account_deleted_visible(), "'Account Deleted!' message is not visible"
        signup.click_continue_button()










