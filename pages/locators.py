from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.XPATH, "//span[@class='btn-group']/a")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")


class ProductPageLocators():
    ADD_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    ADDED_PRODUCT = (By.XPATH, "//div[@class='alertinner '][1]")
    PRODUCT_NAME = (By.TAG_NAME, "h1")
    PRODUCT_PRICE = (By.XPATH, "//p[@class='price_color']")
    CART_PRICE = (By.XPATH, "//div[@class='alertinner ']/p")


class BasketPageLocators():
    EMPTY_TEXT = (By.XPATH, "//*[@id='content_inner']/p")
    SOME_ITEM = (By.XPATH, "//div[@class='basket-items']")
