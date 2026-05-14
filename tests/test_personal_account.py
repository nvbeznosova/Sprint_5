import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.personal_account_locators import PersonalAccountLocators

TEST_EMAIL = os.environ.get("TEST_EMAIL")
TEST_PASSWORD = os.environ.get("TEST_PASSWORD")

def test_redirect_to_personal_account(driver):
    driver.get("https://stellarburgers.education-services.ru/login")
    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable(PersonalAccountLocators.EMAIL_INPUT)).send_keys(TEST_EMAIL)
    wait.until(EC.element_to_be_clickable(PersonalAccountLocators.PASSWORD_INPUT)).send_keys(TEST_PASSWORD)
    wait.until(EC.element_to_be_clickable(PersonalAccountLocators.LOGIN_BUTTON)).click()
    wait.until(EC.element_to_be_clickable(PersonalAccountLocators.PERSONAL_ACCOUNT_BUTTON)).click()
    assert "account" in driver.current_url

def test_logout_from_personal_account(driver):
    driver.get("https://stellarburgers.education-services.ru/login")
    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable(PersonalAccountLocators.EMAIL_INPUT)).send_keys(TEST_EMAIL)
    wait.until(EC.element_to_be_clickable(PersonalAccountLocators.PASSWORD_INPUT)).send_keys(TEST_PASSWORD)
    wait.until(EC.element_to_be_clickable(PersonalAccountLocators.LOGIN_BUTTON)).click()
    wait.until(EC.element_to_be_clickable(PersonalAccountLocators.LOGOUT_BUTTON)).click()
    assert "login" in driver.current_url 