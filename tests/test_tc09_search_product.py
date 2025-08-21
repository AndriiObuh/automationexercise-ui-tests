import allure
import pytest
from pages.products_page import ProductsPage
from pages.home_page import HomePage
from selenium.webdriver.chrome.webdriver import WebDriver


class TestSearchProduct:

    @pytest.mark.xfail(reason="Expected bug: search returns unrelated products", strict=False)
    def test_search_product(self, driver: WebDriver):
        home = HomePage(driver)
        products = ProductsPage(driver)

        # 1-2. Launch browser and navigate to home page
        home.open()
        # 3. Verify that home page is visible
        assert home.is_home_page(), "Home page is not visible"
        assert home.is_home_url(), "Home url is incorrect"
        # 4-5. Click on 'Products' button and verify user is navigated to ALL PRODUCTS page successfully
        home.click_header_menu(home.HEADER_PRODUCTS)
        assert products.is_products_title_visible(), "'ALL PRODUCTS' is not visible"
        # 6. Enter product name in search input and click search button
        products.enter_search_text("dress")
        products.click_search_button()
        # 7. Verify 'SEARCHED PRODUCTS' is visible
        assert products.is_searched_products_title_visible(), "'SEARCHED PRODUCTS' is not visible"
        # 8. Verify all the products related to search are visible
        mismatches = products.verify_products_match_query("dress")
        if mismatches:
            # This will fail, but marked as xfail
            allure.attach(
                "\n".join(mismatches),
                name="Products not matching search query",
                attachment_type=allure.attachment_type.TEXT
            )
        assert not mismatches, f"The following products do not match search query 'dress': {mismatches}"




