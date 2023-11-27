from selene import browser
from selene import have

browser.config.timeout = 10

def test_start():
    browser.open('http://shop.bugred.ru/')

def test_login_valid():
    browser.open('http://shop.bugred.ru/user/login/index')
    browser.element('[name="email"]').type('test@mail.com')
    browser.element('[name="password"]').type('1')
    browser.element('[name="_csrf"]').click()

def test_login_valid_check():
    browser.element('[id="navbarDropdown2"]').should(have.text("Test"))