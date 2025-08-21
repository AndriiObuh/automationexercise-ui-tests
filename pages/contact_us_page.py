import allure
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.common.exceptions import NoAlertPresentException


class ContactUsPage(BasePage):
    URL = "https://automationexercise.com/contact_us"

    # --- Locators ---
    GET_IN_TOUCH_HEADER = (By.XPATH, "//h2[contains(text(),'Get In Touch')]")
    NAME_INPUT = (By.XPATH, "//input[@name='name']")
    EMAIL_INPUT = (By.XPATH, "//input[@name='email']")
    SUBJECT_INPUT = (By.XPATH, "//input[@name='subject']")
    MESSAGE_TEXTAREA = (By.XPATH, "//textarea[@name='message']")
    UPLOAD_FILE_INPUT = (By.XPATH, "//input[@type='file']")
    SUBMIT_BUTTON = (By.XPATH, "//input[@type='submit']")
    SUCCESS_MESSAGE = (By.XPATH, "//div[@class='status alert alert-success']")

    HOME_BUTTON = (By.XPATH, "//a[@href='/']")

    def __init__(self, driver: WebDriver):
        """Initialize LoginPage with a WebDriver instance."""
        super().__init__(driver)

    @allure.step("Open Login page")
    def open(self) -> None:
        """Open the login page URL."""
        super().open(self.URL)

    @allure.step("Verify 'Get In Touch' header is visible")
    def is_get_in_touch_visible(self) -> bool:
        return self.is_visible(self.GET_IN_TOUCH_HEADER)

    @allure.step("Fill contact form")
    def fill_contact_form(self, name: str, email: str, subject: str, message: str, file_path: str = None):
        """Fill contact form fields and optionally upload a file."""
        self.element_is_visible(self.NAME_INPUT).send_keys(name)
        self.element_is_visible(self.EMAIL_INPUT).send_keys(email)
        self.element_is_visible(self.SUBJECT_INPUT).send_keys(subject)
        self.element_is_visible(self.MESSAGE_TEXTAREA).send_keys(message)
        if file_path:
            self.element_is_visible(self.UPLOAD_FILE_INPUT).send_keys(file_path)

    @allure.step("Click Submit button")
    def click_submit(self):
        """Click the Submit button on the contact form."""
        self.element_is_clickable(self.SUBMIT_BUTTON).click()

    @allure.step("Accept alert")
    def accept_alert(self):
        """Accept the browser alert after form submission."""
        try:
            alert = self.driver.switch_to.alert
            alert.accept()
        except NoAlertPresentException:
            raise AssertionError("Expected alert, but none appeared")

    @allure.step("Click Home button")
    def click_home_button(self):
        """Click the Home button to return to the main page."""
        self.element_is_clickable(self.HOME_BUTTON).click()

    def is_success_message_visible(self) -> bool:
        """Return True if success message is visible after form submission."""
        return self.is_visible(self.SUCCESS_MESSAGE)


