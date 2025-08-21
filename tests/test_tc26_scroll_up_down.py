import pytest
import allure
from selenium.webdriver.remote.webdriver import WebDriver
from pages.home_page import HomePage

class TestScrollUpDown:

    def test_scroll_up_down(self, driver: WebDriver):
        home = HomePage(driver)

        # 1-2. Open home page
        home.open()
        # 3. Verify home page is visible
        assert home.is_home_page(), "Home page is not visible"
        # 4. Scroll down to bottom
        home.scroll_to_bottom()
        # 5. Verify 'SUBSCRIPTION' is visible
        assert home.is_subscription_visible(), "'SUBSCRIPTION' is not visible at bottom"
        # 6. Scroll up to top
        home.scroll_to_top()
        # 7. Verify top text is visible
        assert home.is_full_fledged_text_visible(), "'Full-Fledged practice website...' text is not visible at top"
