import pytest
from pages.home_page import HomePage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from selenium.webdriver.chrome.webdriver import WebDriver


class TestAddProductsInCart:

    def test_add_products_in_cart(self, driver: WebDriver):
        home = HomePage(driver)
        products = ProductsPage(driver)
        cart = CartPage(driver)

        # 1-2. Launch browser and navigate to home page
        home.open()
        # 3. Verify that home page is visible
        assert home.is_home_page(), "Home page is not visible"
        assert home.is_home_url(), "Home url is incorrect"
        # 4. Click on 'Products'
        home.click_header_menu(home.HEADER_PRODUCTS)
        # 5. Hover over first product and click 'Add to cart'
        products.add_product_to_cart(1)
        # 6. Click 'Continue Shopping' button
        products.click_continue_shopping_button()
        # 7. Hover over second product and click 'Add to cart'
        products.add_product_to_cart(2)
        # 8. Click 'View Cart' button
        products.click_view_cart_button()
        # 9. Verify both products are added to Cart
        assert cart.get_products_count() == 2, "Incorrect number of products in the cart"
        # 10. Verify their prices, quantity and total price
        expected_products = [
            {"name": "Blue Top", "price": "Rs. 500", "quantity": "1", "total": "Rs. 500"},
            {"name": "Men Tshirt", "price": "Rs. 400", "quantity": "1", "total": "Rs. 400"},
        ]
        for index, expected in enumerate(expected_products):
            actual = cart.get_product_in_cart(index)
            assert actual["name"] == expected["name"], f"Expected name {expected['name']}, got {actual['name']}"
            assert actual["price"] == expected["price"], f"Expected price {expected['price']}, got {actual['price']}"
            assert actual["quantity"] == expected["quantity"], f"Expected quantity {expected['quantity']}, got {actual['quantity']}"
            assert actual["total"] == expected["total"], f"Expected total {expected['total']}, got {actual['total']}"






