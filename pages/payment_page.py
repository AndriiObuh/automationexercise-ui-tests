import allure
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from generator.generator import generator_cart_detail


class PaymentPage(BasePage):
    URL = "https://automationexercise.com/payment"

    # --- Locators ---
    NAME_ON_CARD = (By.XPATH, "//input[@name='name_on_card']")
    CARD_NUMBER = (By.XPATH, "//input[@name='card_number']")
    CVC = (By.XPATH, "//input[@name='cvc']")
    EXPIRY_MONTH = (By.XPATH, "//input[@name='expiry_month']")
    EXPIRY_YEAR = (By.XPATH, "//input[@name='expiry_year']")
    PAY_AND_CONFIRM_BUTTON = (By.XPATH, "//button[@id='submit']")
    SUCCESS_MESSAGE = (By.XPATH, "//p[contains(text(), 'Congratulations! Your order has been confirmed!')]")

    def __init__(self, driver: WebDriver):
        """Initialize LoginPage with a WebDriver instance."""
        super().__init__(driver)

    @allure.step("Open Login page")
    def open(self) -> None:
        """Open the login page URL."""
        super().open(self.URL)

    @allure.step("Fill payment form")
    def fill_payment_form(self):
        payment_cart = next(generator_cart_detail())
        name = payment_cart.name
        number = payment_cart.number
        cvc = payment_cart.cvc
        month = payment_cart.month
        year = payment_cart.year
        self.element_is_visible(self.NAME_ON_CARD).send_keys(name)
        self.element_is_visible(self.CARD_NUMBER).send_keys(number)
        self.element_is_visible(self.CVC).send_keys(cvc)
        self.element_is_visible(self.EXPIRY_MONTH).send_keys(month)
        self.element_is_visible(self.EXPIRY_YEAR).send_keys(year)

    @allure.step("Click 'Pay and Confirm Order'")
    def click_pay_and_confirm(self):
        self.element_is_clickable(self.PAY_AND_CONFIRM_BUTTON).click()

    @allure.step("Check if success message is visible")
    def is_success_message_visible(self) -> bool:
        return self.is_visible(self.SUCCESS_MESSAGE)