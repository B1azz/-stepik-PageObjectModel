from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_cart(self):
        assert self.is_element_present(*ProductPageLocators.ADD_BUTTON), "Add button is not presented"
        self.click_button(*ProductPageLocators.ADD_BUTTON)

    def product_name_is_correct(self):
        assert_text = self.element_text(*ProductPageLocators.PRODUCT_NAME) + " has been added to your basket."
        assert assert_text == self.element_text(*ProductPageLocators.ADDED_PRODUCT), \
            "Product name not correct"

    def price_is_correct(self):
        assert_text = "Your basket total is now " + self.element_text(*ProductPageLocators.PRODUCT_PRICE)
        assert assert_text == self.element_text(*ProductPageLocators.CART_PRICE), \
            "Price is not correct"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ADDED_PRODUCT), \
            "Success message is presented, but should not be"

    def success_message_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.ADDED_PRODUCT), \
            "Success_message is not disappeared"

