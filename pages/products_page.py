import allure
from selenium.common import ElementClickInterceptedException

from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class ProductsPage(BasePage):

    URL = "https://automationexercise.com/products"

    # --- Locators ---
    PRODUCT_CONTAINER = (By.XPATH, "//div[@class='product-image-wrapper']")
    ADD_TO_CART_BUTTON = (By.XPATH, ".//div[@class='overlay-content']//a[contains(@class,'add-to-cart')]")
    CONTINUE_SHOPPING_BUTTON = (By.XPATH, "//button[@class='btn btn-success close-modal btn-block']")
    VIEW_CART_BUTTON = (By.XPATH, "//div[@class='modal-content']//a[@href='/view_cart']")

    def __init__(self, driver: WebDriver):
        """Initialize LoginPage with a WebDriver instance."""
        super().__init__(driver)

    @allure.step("Open Login page")
    def open(self) -> None:
        """Open the login page URL."""
        super().open(self.URL)

    @allure.step("Hover over product #{index} and click 'Add to cart'")
    def add_product_to_cart(self, index: int):
        """
        Hover over a product by its 1-based index and click 'Add to cart'.

        :param index: Product number on the page (starting from 1)
        """
        products = self.elements_are_visible(self.PRODUCT_CONTAINER)
        product = products[index - 1] # counts from 1 in the test case
        self.action_move_to_element(product)
        add_button = product.find_element(
            By.XPATH, ".//div[@class='overlay-content']//a[contains(@class,'add-to-cart')]"
        )
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", add_button)

        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(add_button))
        try:
            add_button.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", add_button)

    @allure.step("Click 'Continue Shopping' button")
    def click_continue_shopping_button(self):
        """Click the 'Continue Shopping' button in the modal window."""
        self.element_is_clickable(self.CONTINUE_SHOPPING_BUTTON).click()
        WebDriverWait(self.driver, 5).until(EC.invisibility_of_element_located(self.CONTINUE_SHOPPING_BUTTON))

    @allure.step("Click 'View Cart' button")
    def click_view_cart_button(self):
        """Click the 'Continue Shopping' button in the modal window."""
        self.element_is_clickable(self.VIEW_CART_BUTTON).click()




