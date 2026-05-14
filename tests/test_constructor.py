import pytest
from locators.constructor_page_locators import ConstructorPageLocators

def test_constructor_tabs(driver):
    driver.get("https://stellarburgers.education-services.ru/")
    driver.find_element(*ConstructorPageLocators.BUNS_TAB).click()
    driver.find_element(*ConstructorPageLocators.SAUCES_TAB).click()
    driver.find_element(*ConstructorPageLocators.FILLINGS_TAB).click()