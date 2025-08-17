import allure
from pages.base_page import BasePage
from selenium.webdriver.remote.webdriver import WebDriver


class HomePage(BasePage):
    URL = "https://automationexercise.com/"

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




