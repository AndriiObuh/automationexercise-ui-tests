import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.remote.webdriver import WebDriver


class HomePage(BasePage):
    URL = "https://automationexercise.com/"

    # --- Locators ---
    FULL_FLEDGED_TEXT = (By.XPATH, "//h2[contains(text(), 'Full-Fledged practice website for Automation Engineers')]")
    SUBSCRIPTION_HEADER = (By.XPATH, "//h2[contains(text(),'Subscription')]")

    def __init__(self, driver: WebDriver):
        """Initialize HomePage with a WebDriver instance."""
        super().__init__(driver)

    @allure.step("Open Home Page")
    def open(self) -> None:
        """Open the home page URL in the browser."""
        super().open(self.URL)

    @allure.step("Check if home page is visible")
    def is_home_page(self) -> bool:
        """Return True if home page is visible (specific element is present)."""
        return self.is_visible(self.HOME_SLIDER)

    @allure.step("Check if current URL is the home page URL")
    def is_home_url(self) -> bool:
        """
        Verify that the current page URL matches the home page URL.
        :return: True if the current URL is the home page URL, False otherwise.
        """
        return self.driver.current_url == self.URL

    @allure.step("Scroll to bottom of the page")
    def scroll_to_bottom(self) -> None:
        """Scroll the page all the way down."""
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    @allure.step("Scroll to top of the page")
    def scroll_to_top(self) -> None:
        """Scroll the page all the way up."""
        self.driver.execute_script("window.scrollTo(0, 0);")

    @allure.step("Check if 'Full-Fledged practice website...' text is visible")
    def is_full_fledged_text_visible(self) -> bool:
        """Return True if the top page text is visible."""
        return self.is_visible(self.FULL_FLEDGED_TEXT)

    @allure.step("Check if 'SUBSCRIPTION' header is visible")
    def is_subscription_visible(self) -> bool:
        """Return True if the 'SUBSCRIPTION' section is visible at the bottom."""
        return self.is_visible(self.SUBSCRIPTION_HEADER)




