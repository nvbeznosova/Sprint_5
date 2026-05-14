import os
from locators.personal_account_locators import PersonalAccountLocators

TEST_EMAIL = os.environ.get("TEST_EMAIL")
TEST_PASSWORD = os.environ.get("TEST_PASSWORD")

def test_redirect_to_personal_account(driver):
    driver.get("https://stellarburgers.education-services.ru/login")
    driver.find_element(*PersonalAccountLocators.EMAIL_INPUT).send_keys(TEST_EMAIL)
    driver.find_element(*PersonalAccountLocators.PASSWORD_INPUT).send_keys(TEST_PASSWORD)
    driver.find_element(*PersonalAccountLocators.LOGIN_BUTTON).click()
    driver.find_element(*PersonalAccountLocators.PERSONAL_ACCOUNT_BUTTON).click()
    assert "account" in driver.current_url

def test_logout_from_personal_account(driver):
    driver.get("https://stellarburgers.education-services.ru/login")
    driver.find_element(*PersonalAccountLocators.EMAIL_INPUT).send_keys(TEST_EMAIL)
    driver.find_element(*PersonalAccountLocators.PASSWORD_INPUT).send_keys(TEST_PASSWORD)
    driver.find_element(*PersonalAccountLocators.LOGIN_BUTTON).click()
    driver.find_element(*PersonalAccountLocators.LOGOUT_BUTTON).click()
    assert "login" in driver.current_url