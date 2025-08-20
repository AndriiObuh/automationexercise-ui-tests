import allure
import pytest
from pages.home_page import HomePage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.login_page import LoginPage
from pages.signup_page import SignupPage
from pages.checkout_page import CheckoutPage
from pages.payment_page import PaymentPage
from selenium.webdriver.chrome.webdriver import WebDriver


class TestPlaceOrderAndRegisterWhileCheckout:

    def test_place_order_register_while_checkout(self, driver: WebDriver):
        home = HomePage(driver)
        login = LoginPage(driver)
        signup = SignupPage(driver)
        products = ProductsPage(driver)
        cart = CartPage(driver)
        payment = PaymentPage(driver)
        checkout = CheckoutPage(driver)

        # 1-2. Launch browser and navigate to home page
        home.open()
        # 3. Verify that home page is visible
        assert home.is_home_page(), "Home page is not visible"
        assert home.is_home_url(), "Home url is incorrect"
        # 4–5: Add products and go to Cart
        home.click_header_menu(home.HEADER_PRODUCTS)
        products.add_product_to_cart(1)
        products.click_view_cart_button()
        # 6. Verify that cart page is displayed
        assert cart.get_products_count() > 0, "Cart is empty"
        # 7-8 Click 'Proceed To Checkout' and 'Register / Login' buttons
        cart.click_proceed_to_checkout()
        cart.click_register_login()
        # 9–11: Signup and account creation
        login.fill_signup_form()
        login.click_signup_button()
        signup.fill_registration_form()
        assert signup.is_account_created(), "'Account Created!' header is not visible"
        signup.click_continue_button()
        assert signup.is_logged_in_as_visible(), "'Logged in as username' is not visible"
        # 12.Click 'Cart' button
        home.click_header_menu(home.HEADER_CART)
        # 13. Click 'Proceed To Checkout' button
        cart.click_proceed_to_checkout()
        # 14. Verify Address Details and Review Your Order
        checkout.is_address_and_review_visible(), "Address Details and Review Your Order are not visible"
        # 15. Enter description in comment text area and click 'Place Order'
        checkout.enter_comment("My comment")
        checkout.click_place_order()
        # 16-17. Enter payment details and click 'Pay and Confirm Order' button
        payment.fill_payment_form()
        payment.click_pay_and_confirm()
        #18. Verify success message 'Your order has been placed successfully!'
        payment.is_success_message_visible(), "Success message 'Your order has been placed successfully!' is not visible"
        #19-20. Click 'Delete Account' button and verify 'ACCOUNT DELETED!' and click 'Continue' button
        login.click_delete_account()
        assert login.is_account_deleted_visible(), "'Account Deleted!' message is not visible"
        signup.click_continue_button()















