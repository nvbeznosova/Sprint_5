from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.constructor_page_locators import ConstructorPageLocators

def test_constructor_tabs(driver):
    driver.get("https://stellarburgers.education-services.ru/")
    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable(ConstructorPageLocators.BUNS_TAB)).click()
    wait.until(EC.element_to_be_clickable(ConstructorPageLocators.SAUCES_TAB)).click()
    wait.until(EC.element_to_be_clickable(ConstructorPageLocators.FILLINGS_TAB)).click() 