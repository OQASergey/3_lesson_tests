import pytest
from selene import browser

def test_start():
    browser.open('http://shop.bugred.ru/')

def test_reg_valid():
    browser.open('http://shop.bugred.ru/user/register/index')
    browser.element('[id=exampleInputName]').type("Test_name")
    browser.element('[id=exampleInputEmail1]').type('test_name@mail.ru')
