import allure
from pages.base_page import BasePage
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from generator.generator import generated_person


class SignupPage(BasePage):
    URL = "https://automationexercise.com/signup"

    # --- Locators ---
    TITLE_MR = (By.ID, "id_gender1")
    TITLE_MRS = (By.ID, "id_gender2")
    NAME = (By.ID, "name")
    EMAIL = (By.ID, "email")
    PASSWORD = (By.ID, "password")
    DAY = (By.ID, "days")
    MONTH = (By.ID, "months")
    YEAR = (By.ID, "years")
    NEWSLETTER_CHECKBOX = (By.ID, "newsletter")
    OFFERS_CHECKBOX = (By.ID, "optin")

    FIRST_NAME = (By.ID, "first_name")
    LAST_NAME = (By.ID, "last_name")
    COMPANY = (By.ID, "company")
    ADDRESS1 = (By.ID, "address1")
    ADDRESS2 = (By.ID, "address2")
    COUNTRY = (By.ID, "country")
    STATE = (By.ID, "state")
    CITY = (By.ID, "city")
    ZIPCODE = (By.ID, "zipcode")
    MOBILE_NUMBER = (By.ID, "mobile_number")

    CREATE_ACCOUNT_BUTTON = (By.XPATH, "//button[@data-qa='create-account']")
    ACCOUNT_CREATED_HEADER = (By.XPATH, "//h2/b[contains(text(),'Account Created!')]")
    CONTINUE_BUTTON = (By.XPATH, "//a[@data-qa='continue-button']")
    HEADER_LOGGED_IN_AS = (By.XPATH, "//a[contains(text(), 'Logged in as')]")

    def __init__(self, driver: WebDriver):
        """Initialize LoginPage with a WebDriver instance."""
        super().__init__(driver)

    @allure.step("Open Login page")
    def open(self) -> None:
        """Open the login page URL."""
        super().open(self.URL)

    def fill_registration_form(self):
        person = next(generated_person())
        password = person.password
        first_name = person.first_name
        last_name = person.last_name
        company = person.company
        address = person.address
        address2 = person.address2
        country = person.country
        state = person.state
        city = person.city
        zipcode = person.zipcode
        mobile = person.mobile
        day = person.day
        month = person.month
        year = person.year
        gender = person.gender
        if person.gender == "mr":
            self.element_is_clickable(self.TITLE_MR).click()
        else:
            self.element_is_clickable(self.TITLE_MRS).click()
        self.element_is_visible(self.PASSWORD).send_keys(password)
        self.element_is_visible(self.FIRST_NAME).send_keys(first_name)
        self.element_is_visible(self.LAST_NAME).send_keys(last_name)
        self.element_is_visible(self.COMPANY).send_keys(company)
        self.element_is_visible(self.ADDRESS1).send_keys(address)
        self.element_is_visible(self.ADDRESS2).send_keys(address2)
        self.select_by_value(self.COUNTRY, country)
        self.element_is_visible(self.STATE).send_keys(state)
        self.element_is_visible(self.CITY).send_keys(city)
        self.element_is_visible(self.ZIPCODE).send_keys(zipcode)
        self.element_is_visible(self.MOBILE_NUMBER).send_keys(mobile)
        self.select_by_value(self.DAY, day)
        self.select_by_value(self.MONTH, month)
        self.select_by_value(self.YEAR, year)
        self.element_is_visible(self.NEWSLETTER_CHECKBOX).click()
        self.element_is_visible(self.OFFERS_CHECKBOX).click()
        self.element_is_visible(self.CREATE_ACCOUNT_BUTTON).click()

    @allure.step("Check if 'ACCOUNT CREATED!' message is visible")
    def is_account_created(self) -> bool:
        """Return True if 'ACCOUNT CREATED!' confirmation message is visible."""
        return self.is_visible(self.ACCOUNT_CREATED_HEADER)

    @allure.step("Check if 'Logged in as username' is visible")
    def is_logged_in_as_visible(self) -> bool:
        """Return True if 'Logged in as username' header is visible in the page header."""
        return self.is_visible(self.HEADER_LOGGED_IN_AS)

    @allure.step("Click 'Continue' button after account creation")
    def click_continue_button(self) -> None:
        """Click the 'Continue' button after successful account creation."""
        self.element_is_clickable(self.CONTINUE_BUTTON).click()















