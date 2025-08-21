import allure
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class CheckoutPage(BasePage):
    URL = "https://automationexercise.com/checkout"

    # --- Locators ---
    ADDRESS_DETAILS = (By.XPATH, "//h2[contains(text(), 'Address Details')]")
    REVIEW_ORDER = (By.XPATH, "//h2[contains(text(), 'Review Your Order')]")
    COMMENT_TEXTAREA = (By.XPATH, "//textarea[@name='message']")
    PLACE_ORDER_BUTTON = (By.XPATH, "//a[@href='/payment']")
    TOTAL_AMOUNT = (By.XPATH, "//tr[.//b[text()='Total Amount']]//p[@class='cart_total_price']")

    def __init__(self, driver: WebDriver):
        """Initialize LoginPage with a WebDriver instance."""
        super().__init__(driver)

    @allure.step("Open Login page")
    def open(self) -> None:
        """Open the login page URL."""
        super().open(self.URL)

    @allure.step("Verify address and order review are visible")
    def is_address_and_review_visible(self) -> bool:
        return self.is_visible(self.ADDRESS_DETAILS) and self.is_visible(self.REVIEW_ORDER)

    @allure.step("Enter comment for the order")
    def enter_comment(self, text: str) -> None:
        self.element_is_visible(self.COMMENT_TEXTAREA).send_keys(text)

    @allure.step("Click 'Place Order' button")
    def click_place_order(self) -> None:
        self.element_is_clickable(self.PLACE_ORDER_BUTTON).click()

    @allure.step("Get total amount from checkout page")
    def get_total_amount(self) -> str:
        """Return the total amount text (e.g., 'Rs. 1400')."""
        return self.element_is_visible(self.TOTAL_AMOUNT).text

