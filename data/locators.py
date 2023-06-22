from selenium.webdriver.common.by import By


class ElementsPagelocators:
    """__________________________________________
                ЛОКАТОРЫ ДЛЯ TextBox
        _________________________________________"""

    TEXT_BOX = (By.XPATH, "//span[contains(text(), 'Text Box')]")

    FULL_NAME = (By.CSS_SELECTOR, "input[id='userName']")
    EMAIL = (By.CSS_SELECTOR, "input[id='userEmail']")
    EMAIL_INCORRECT = (By.XPATH, "//form[@id='userForm']/div[2]//input[contains(@class, 'field-error')]")
    CURRENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='currentAddress']")
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='permanentAddress']")

    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[id='submit']")

    CREATED_FULL_NAME = (By.CSS_SELECTOR, "#output #name")
    CREATED_EMAIL = (By.CSS_SELECTOR, "#output #email")
    CREATED_CURRENT_ADDRESS = (By.CSS_SELECTOR, "#output #currentAddress")
    CREATED_PERMANENT_ADDRESS = (By.CSS_SELECTOR, "#output #permanentAddress")

    """__________________________________________
                ЛОКАТОРЫ ДЛЯ CheckBox
        _________________________________________"""

    PLUS_BUTTON = (By.CSS_SELECTOR, ".rct-option-expand-all")
    MINUS_BUTTON = (By.CSS_SELECTOR, ".rct-option-collapse-all")