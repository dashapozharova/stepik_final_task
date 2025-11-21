from .base_page import BasePage
from .locators import ProductPageLocators
import math
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductPage(BasePage):
    def add_to_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        basket_button.click()
    
    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
    
    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
    
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
    
    def should_be_product_added_to_basket(self):
        # Только проверка, без добавления в корзину
        product_name = self.get_product_name()
        message_element = WebDriverWait(self.browser, 15).until(
            EC.presence_of_element_located(ProductPageLocators.SUCCESS_MESSAGE_PRODUCT_NAME)
        )
        message_product_name = message_element.text
        assert product_name == message_product_name, f"Product name doesn't match. Expected: '{product_name}', got: '{message_product_name}'"
    
    def should_be_basket_total_equal_to_product_price(self):
        # Только проверка, без добавления в корзину
        product_price = self.get_product_price()
        basket_element = WebDriverWait(self.browser, 15).until(
            EC.presence_of_element_located(ProductPageLocators.BASKET_TOTAL_PRICE)
        )
        basket_total_price = basket_element.text
        assert product_price == basket_total_price, f"Product price doesn't match basket total. Expected: '{product_price}', got: '{basket_total_price}'"
    
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE_PRODUCT_NAME), \
            "Success message is presented, but should not be"

    def should_be_success_message_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE_PRODUCT_NAME), \
            "Success message is not disappeared, but should be"