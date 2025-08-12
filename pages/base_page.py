import allure
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver

    # Common logo locator
    LOGO = (By.XPATH, "//div[@class='logo pull-left']")

    # Common header locators
    HEADER_HOME = (By.LINK_TEXT, "Home")
    HEADER_PRODUCTS = (By.LINK_TEXT, "Products")
    HEADER_CART = (By.LINK_TEXT, "Cart")
    HEADER_SIGNUP_LOGIN = (By.LINK_TEXT, "Signup / Login")
    HEADER_LOGOUT = (By.LINK_TEXT, "Logout")
    HEADER_DELETE_ACCOUNT = (By.LINK_TEXT, "Delete Account")

    @allure.step("Open page: {url}")
    def open(self, url: str) -> None:
        """Opens the page at the given URL.
        :param url: Page URL"""
        self.driver.get(url)

    @allure.step("Click on the menu item in the header: {locator}")
    def click_header_menu(self, locator) -> None:
        """Clicks on a menu item in the header by locator.
        :param locator: item locator (By, value)"""
        self.driver.find_element(*locator).click()

    @allure.step("Check that the logo is displayed")
    def is_logo_visible(self) -> bool:
        """Checks if the site logo is visible.
        :return: True if the logo is visible, False if not"""
        return self.driver.find_element(*self.LOGO).is_displayed()

    def is_signup_login_visible(self) -> bool:
        """Check if 'Signup / Login' menu item is visible."""
        try:
            return self.driver.find_element(*self.HEADER_SIGNUP_LOGIN).is_displayed()
        except NoSuchElementException:
            return False

    def is_logout_visible(self) -> bool:
        """Check if 'Logout' menu item is visible."""
        try:
            return self.driver.find_element(*self.HEADER_LOGOUT).is_displayed()
        except NoSuchElementException:
            return False





