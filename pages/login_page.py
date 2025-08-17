import allure
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from generator.generator import generated_person


class LoginPage(BasePage):
    URL = "https://automationexercise.com/login"

    # --- Common locators ---
    LOGIN_EMAIL = (By.XPATH, "//input[@data-qa='login-email']")
    LOGIN_PASSWORD = (By.XPATH, "//input[@data-qa='login-password']")
    LOGIN_BUTTON = (By.XPATH, "//button[@data-qa='login-button']")
    LOGIN_ERROR = (By.XPATH, "//p[contains(text(),'incorrect')]")
    LOGIN_HEADER = (By.XPATH, "//h2[contains(text(),'Login to your account')]")

    SIGNUP_NAME = (By.XPATH, "//input[@data-qa='signup-name']")
    SIGNUP_EMAIL = (By.XPATH, "//input[@data-qa='signup-email']")
    SIGNUP_BUTTON = (By.XPATH, "//button[@data-qa='signup-button']")
    SIGNUP_ERROR = (By.XPATH, "//p[contains(text(),'already')]")
    SIGNUP_HEADER = (By.XPATH, "//h2[contains(text(),'New User Signup!')]")
    ENTER_ACCOUNT_INFO_HEADER = (By.XPATH, "//h2//b[contains(text(), 'Enter Account Information')]")

    DELETE_ACCOUNT = (By.XPATH, "//ul//a[@href='/delete_account']")
    ACCOUNT_DELETED = (By.XPATH, "//h2//b[contains(text(),'Account Deleted!')]")
    HEADER_LOGGED_IN_AS = (By.XPATH, "//a[contains(text(), 'Logged in as')]")


    def __init__(self, driver: WebDriver):
        """Initialize LoginPage with a WebDriver instance."""
        super().__init__(driver)

    @allure.step("Open Login page")
    def open(self) -> None:
        """Open the login page URL."""
        super().open(self.URL)

    # --- Signup methods ---
    @allure.step("Fill signup form with name and email")
    def fill_signup_form(self, name: str = None, email: str = None) -> None:
        """Fill signup name and email fields.
        If name or email are not provided, generate them automatically.
        """
        if name is None or email is None:
            person = next(generated_person())
            if name is None:
                name = person.name
            if email is None:
                email = person.email

        self.element_is_visible(self.SIGNUP_NAME).send_keys(name)
        self.element_is_visible(self.SIGNUP_EMAIL).send_keys(email)

    @allure.step("Click signup button")
    def click_signup_button(self) -> None:
        """Click signup button."""
        self.element_is_clickable(self.SIGNUP_BUTTON).click()

    @allure.step("Check signup error visible")
    def is_signup_error_visible(self) -> bool:
        """Return True if signup error is visible."""
        return self.is_visible(self.SIGNUP_ERROR)

    @allure.step("Check signup header visible")
    def is_signup_header_visible(self) -> bool:
        """Return True if signup header is visible."""
        return self.is_visible(self.SIGNUP_HEADER)

    @allure.step("Check signup success visible")
    def is_signup_success_visible(self) -> bool:
        return self.is_visible(self.ENTER_ACCOUNT_INFO_HEADER)


    # --- Login methods ---
    @allure.step("Fill login form")
    def fill_login_form(self, email: str, password: str) -> None:
        """Fill login email and password."""
        self.element_is_visible(self.LOGIN_EMAIL).send_keys(email)
        self.element_is_visible(self.LOGIN_PASSWORD).send_keys(password)

    @allure.step("Click login button")
    def click_login_button(self) -> None:
        """Click login button."""
        self.element_is_clickable(self.LOGIN_BUTTON).click()

    @allure.step("Check login error visible")
    def is_login_error_visible(self) -> bool:
        """Return True if login error is visible."""
        return self.is_visible(self.LOGIN_ERROR)

    @allure.step("Check if 'Login to your account' is visible")
    def is_login_header_visible(self) -> bool:
        """Return True if 'Login to your account' is visible."""
        return self.is_visible(self.LOGIN_HEADER)

    @allure.step("Check if 'Logged in as username' is visible")
    def is_logged_in_as_visible(self) -> bool:
        """Return True if 'Logged in as username' is visible."""
        return self.is_visible(self.HEADER_LOGGED_IN_AS)

    # --- Delete Account methods ---
    @allure.step("Click 'Delete Account' button")
    def click_delete_account(self) -> None:
        """Click the 'Delete Account' button in the header."""
        self.element_is_clickable(self.DELETE_ACCOUNT).click()

    @allure.step("Check if 'ACCOUNT DELETED!' message is visible")
    def is_account_deleted_visible(self) -> bool:
        """Return True if 'ACCOUNT DELETED!' confirmation is visible."""
        return self.is_visible(self.ACCOUNT_DELETED)

