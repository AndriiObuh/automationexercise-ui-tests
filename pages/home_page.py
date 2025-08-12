import allure
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver


class HomePage(BasePage):
    URL = "https://automationexercise.com"

    def __init__(self, driver: WebDriver):
        """Initialize HomePage with a WebDriver instance.
        :param driver: Selenium WebDriver instance"""
        super().__init__(driver)

    def open(self) -> None:
        """Open the home page URL in the browser."""
        super().open(self.URL)

    @allure.step("Click the 'Home' menu item")
    def click_home(self) -> None:
        """
        Click the 'Home' link in the header menu.
        """
        self.click_header_menu(self.HEADER_HOME)








