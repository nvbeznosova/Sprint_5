import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from locators.registration_page_locators import RegistrationPageLocators
from utils import generate_email, generate_password

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()

def test_successful_registration(driver):
    email = generate_email()
    password = generate_password()

    driver.get("https://stellarburgers.education-services.ru/register")
    driver.find_element(*RegistrationPageLocators.NAME_INPUT).send_keys("Nadia Beznosova")
    driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()

    assert "login" in driver.current_url

def test_invalid_password_registration(driver):
    email = generate_email()

    driver.get("https://stellarburgers.education-services.ru/register")
    driver.find_element(*RegistrationPageLocators.NAME_INPUT).send_keys("Nadia Beznosova")
    driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys("123")  # слишком короткий пароль
    driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()

    assert driver.find_element(*RegistrationPageLocators.ERROR_MESSAGE).is_displayed()


 