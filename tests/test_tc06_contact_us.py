import os
import pytest
import allure
from pages.home_page import HomePage
from pages.contact_us_page import ContactUsPage
from selenium.webdriver.chrome.webdriver import WebDriver



class TestContactUs:

    def test_contact_us_form(self, driver: WebDriver):
        home = HomePage(driver)
        contact = ContactUsPage(driver)

        # 1-2. Open home page
        home.open()
        # 3. Verify home page is visible
        assert home.is_home_page(), "Home page is not visible"
        # 4. Click 'Contact Us'
        home.click_header_menu(home.CONTACT_US)
        # 5. Verify 'GET IN TOUCH' header is visible
        assert contact.is_get_in_touch_visible(), "'GET IN TOUCH' is not visible"

        # 6-7. Fill form + upload file
        file_path = os.path.abspath("files/test_file.txt")
        contact.fill_contact_form(
            name="Andrii",
            email="andrii@example.com",
            subject="Test Subject",
            message="Test Message",
            file_path=file_path
        )

        # 8-9. Submit and accept alert
        contact.click_submit()
        contact.accept_alert()

        # 10. Verify success message
        assert contact.is_success_message_visible(), "Success message not visible"

        # 11. Click 'Home' and verify
        contact.click_home_button()
        assert home.is_home_page(), "Home page is not visible after clicking Home"

