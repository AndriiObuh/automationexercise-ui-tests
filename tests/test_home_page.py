import pytest
from pages.home_page import HomePage
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver


class TestHomePage:

    def test_open_home_page(self, driver: WebDriver):
        """Open home page and verify URL, logo and menu state for logged out user. """
        home_page = HomePage(driver)
        home_page.open()

        # Check current URL is home page
        assert driver.current_url == home_page.URL, "URL is not the home page URL"

        # Check logo is visible
        assert home_page.is_logo_visible(), "Logo is not visible on home page"

        # Check 'Signup / Login' menu is visible
        assert home_page.is_signup_login_visible(), "'Signup / Login' menu item is not visible"

    def test_click_home_menu(self, driver):
        """Click the Home menu and verify the page is the home page."""
        home_page = HomePage(driver)
        home_page.open()
        home_page.click_home()

        # Verify URL is home page
        assert driver.current_url == home_page.URL, "URL after clicking Home is not the home page URL"

        # Verify 'Signup / Login' menu is still visible
        assert home_page.is_signup_login_visible(), "'Signup / Login' menu item is not visible after clicking Home"




