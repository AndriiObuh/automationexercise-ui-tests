from itertools import product

import allure
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class CartPage(BasePage):

    URL = "https://automationexercise.com/view_cart"

    # --- Locators ---
    CART_TABLE = (By.XPATH, "//table[@id='cart_info_table']")
    CART_ROWS = (By.XPATH, "//div[@class='table-responsive cart_info']//tbody/tr")
    PRODUCT_NAME = (By.XPATH, ".//td[@class='cart_description']/h4/a")
    PRODUCT_PRICE = (By.XPATH, ".//td[@class='cart_price']/p")
    PRODUCT_QUANTITY = (By.XPATH, ".//td[@class='cart_quantity']/button")
    PRODUCT_TOTAL = (By.XPATH, ".//td[@class='cart_total']/p")

    def __init__(self, driver: WebDriver):
        """Initialize LoginPage with a WebDriver instance."""
        super().__init__(driver)

    @allure.step("Open Login page")
    def open(self) -> None:
        """Open the login page URL."""
        super().open(self.URL)


    @allure.step("Get all products in the cart")
    def get_products(self):
        """Returns a list of WebElements representing all product rows in the cart."""
        return self.elements_are_visible(self.CART_ROWS)

    @allure.step("Get product details by row element")
    def get_product_details(self, product_row):
        """
        Extracts product name, price, quantity and total from a product row.

        :param product_row: WebElement representing a row in the cart
        :return: dict with keys 'name', 'price', 'quantity', 'total'
        """
        name = product_row.find_element(*self.PRODUCT_NAME).text.strip()
        price = product_row.find_element(*self.PRODUCT_PRICE).text.strip()
        quantity = product_row.find_element(*self.PRODUCT_QUANTITY).text.strip()
        total = product_row.find_element(*self.PRODUCT_TOTAL).text.strip()
        return {
            'name': name,
            'price': price,
            'quantity': quantity,
            'total': total
        }

    @allure.step("Get number of products in cart")
    def get_products_count(self) -> int:
        """Return the number of products currently in the cart."""
        return len(self.get_products())

    @allure.step("Get product details from cart by index")
    def get_product_in_cart(self, index: int) -> dict:
        """
        Returns details of a product at a given index in the cart.

        :param index: 0-based index of product row
        :return: dict with keys: name, price, quantity, total
        """
        products = self.get_products()
        products_detail = self.get_product_details(products[index])
        return products_detail






