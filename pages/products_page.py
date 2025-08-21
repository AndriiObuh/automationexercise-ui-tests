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
    PRODUCTS_TITLE = (By.XPATH, "//h2[contains(text(),'All Products')]")

    # --- Search ---
    SEARCH_INPUT = (By.ID, "search_product")
    SEARCH_BUTTON = (By.ID, "submit_search")
    SEARCHED_PRODUCTS_TITLE = (By.XPATH, "//h2[contains(text(),'Searched Products')]")
    SEARCHED_PRODUCTS_LIST = (By.CSS_SELECTOR, ".features_items .product-image-wrapper")
    PRODUCT_NAMES = (By.CSS_SELECTOR, ".features_items .productinfo p")


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

    @allure.step("Check if 'ALL PRODUCTS' is visible")
    def is_products_title_visible(self) -> bool:
        """Return True if 'ALL PRODUCTS' is visible."""
        return self.is_visible(self.PRODUCTS_TITLE)

    @allure.step("Enter search query: {query}")
    def enter_search_text(self, query: str) -> None:
        """Type query into search input."""
        field = self.element_is_visible(self.SEARCH_INPUT)
        field.clear()
        field.send_keys(query)

    @allure.step("Click 'Search' button")
    def click_search_button(self) -> None:
        """Click the search button."""
        self.element_is_clickable(self.SEARCH_BUTTON).click()

    # @allure.step("Search product by name: {query}")
    # def search_product(self, query: str) -> None:
    #     """Enter query and submit search."""
    #     self.enter_search_text(query)
    #     self.click_search_button()

    @allure.step("Get product names from search results")
    def get_searched_product_names(self) -> list[str]:
        """Return list of product names from results."""
        elements = self.elements_are_visible(self.PRODUCT_NAMES)
        return [el.text.strip() for el in elements]

    @allure.step("Check if 'SEARCHED PRODUCTS' is visible")
    def is_searched_products_title_visible(self) -> bool:
        """Return True if 'SEARCHED PRODUCTS' is visible."""
        return self.is_visible(self.SEARCHED_PRODUCTS_TITLE)

    @allure.step("Verify products match search query: {query}")
    def verify_products_match_query(self, query: str) -> list[str]:
        """Return list of product names that do NOT match the query."""
        product_names = self.get_searched_product_names()
        mismatches = [name for name in product_names if query.lower() not in name.lower()]
        return mismatches




