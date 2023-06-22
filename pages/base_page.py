from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementNotVisibleException

class BasePage:


    def __init__(self, driver, url, timeout=3):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def element_is_clickable(self, locator, timeout=4):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def element_is_present(self, locator, timeout=4):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def elements_are_present(self, locator, timeout=4):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    def try_to_fill_fild(self, locator, person_data):
        try:
            self.element_is_present(locator).send_keys(person_data)
        except TimeoutException:
            return False
        return True

    def try_to_click_button(self, locator):
        try:
            self.element_is_present(locator)
            self.element_is_clickable(locator).click()
        except TimeoutException or ElementNotVisibleException:
            return False
        return True

    def try_to_get_data(self, locator):
        try:
            actual_data = self.element_is_present(locator).text.split(':')[1]
        except TimeoutException:
            return False
        return actual_data

    def try_check_element_is_present(self, locator):
        try:
            self.element_is_present(locator)
        except TimeoutException:
            return False
        return True
