import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from pages.basket_page import BasketPage 
from pages.main_page import MainPage
from pages.login_page import LoginPage  # ДОБАВЛЯЕМ импорт LoginPage

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()  # просто переход без возврата
    login_page = LoginPage(browser, browser.current_url)  # ЯВНО создаем LoginPage
    login_page.should_be_login_page()

def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = MainPage(browser, "http://selenium1py.pythonanywhere.com/")
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_basket_empty()