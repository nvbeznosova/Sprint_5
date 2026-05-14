from locators.login_page_locators import LoginPageLocators

def test_login_main_page(driver):
    driver.get("https://stellarburgers.education-services.ru/")
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON_MAIN).click()