import allure
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait as wait
from selenium.webdriver.remote.webdriver import WebDriver, WebElement
from selenium.webdriver.support.ui import Select

Locator = tuple[By, str]


class BasePage:
    def __init__(self, driver: WebDriver) -> None:
        """
        Initialize the BasePage with a WebDriver instance.
        :param driver: Selenium WebDriver instance.
        """
        self.driver = driver

    # --- Common locators ---
    HOME_SLIDER = (By.XPATH, "//div[@id='slider-carousel']")
    HEADER_HOME = (By.XPATH, "//ul//a[@href='/']")
    HEADER_PRODUCTS = (By.XPATH, "//ul//a[@href='/products']")
    HEADER_CART = (By.XPATH, "//ul//a[@href='/view_cart']")
    HEADER_SIGNUP_LOGIN = (By.XPATH, "//ul//a[@href='/login']")
    HEADER_LOGOUT = (By.XPATH, "//ul//a[@href='/logout']")
    CONTACT_US = (By.XPATH, "//ul//a[@href='/contact_us']")
    COOKIE_ACCEPT_BUTTON = (By.XPATH,
                            "//button[contains(@class, 'fc-cta-consent') and contains(@class, 'fc-primary-button')]")

    # --- Navigation ---
    @allure.step("Open page: {url}")
    def open(self, url: str) -> None:
        """Opens the page at the given URL."""
        self.driver.get(url)
        self.close_cookie_banner()

    @allure.step("Click on the menu item in the header: {locator}")
    def click_header_menu(self, locator: Locator) -> None:
        """Clicks on a menu item in the header by locator."""
        self.element_is_clickable(locator).click()

    # --- Universal element methods ---
    @allure.step('Find a visible element')
    def element_is_visible(self, locator: Locator, timeout: int = 5) -> WebElement:
        """Wait until the element is visible on the page."""
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step('Find visible elements')
    def elements_are_visible(self, locator: Locator, timeout: int = 5) -> list[WebElement]:
        """Wait until all elements are visible on the page."""
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    @allure.step('Find a present element')
    def element_is_present(self, locator: Locator, timeout: int = 5) -> WebElement:
        """Wait until the element is present in the DOM (may not be visible)."""
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    @allure.step('Find present elements')
    def elements_are_present(self, locator: Locator, timeout: int = 5) -> list[WebElement]:
        """Wait until all elements are present in the DOM (may not be visible)."""
        return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    @allure.step('Find a not visible element')
    def element_is_not_visible(self, locator: Locator, timeout: int = 5) -> bool:
        """Wait until the element is not visible on the page."""
        return wait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    @allure.step('Find clickable element')
    def element_is_clickable(self, locator: Locator, timeout: int = 5) -> WebElement:
        """Wait until the element is clickable."""
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    @allure.step("Check if element is visible: {locator}")
    def is_visible(self, locator: Locator, timeout: int = 5) -> bool:
        """Return True if element is visible, else False."""
        try:
            wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            return True
        except:
            return False

    @allure.step("Close cookie consent banner by clicking 'Accept'")
    def close_cookie_banner(self) -> None:
        """Close cookie banner if the accept button is clickable."""
        try:
            btn = self.element_is_clickable(self.COOKIE_ACCEPT_BUTTON, timeout=5)
            btn.click()
        except TimeoutException:
            pass

    @allure.step("Select by value from dropdown: {value}")
    def select_by_value(self, locator: Locator, value: str):
        """Select option from dropdown using its value attribute."""
        element = self.element_is_visible(locator)
        Select(element).select_by_value(value)

    @allure.step("Select by visible text from dropdown: {text}")
    def select_by_visible_text(self, locator: Locator, text: str):
        """Select option from dropdown using its visible text."""
        element = self.element_is_visible(locator)
        Select(element).select_by_visible_text(text)

    @allure.step('Move cursor to element')
    def action_move_to_element(self, element):
        action = ActionChains(self.driver)
        action.move_to_element(element)
        action.perform()
