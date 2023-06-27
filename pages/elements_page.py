import random
import time

from selenium.webdriver.common.by import By

from data.generator import generator_person
from data.locators import ElementsPagelocators, CheckBoxPageLocators
from pages.base_page import BasePage


class TextBoxPage(BasePage):

    locator = ElementsPagelocators


    def check_filled_form(self, data):
        actual_full_name = self.try_to_get_data(self.locator.CREATED_FULL_NAME)
        assert actual_full_name == data[0], f'Ожидаемый результат: {data[0]} не ' \
                                            f'соответствует фактическому {actual_full_name}'
        actual_email = self.try_to_get_data(self.locator.CREATED_EMAIL)
        assert actual_email == data[1], f'Ожидаемый результат: {data[1]} не ' \
                                            f'соответствует фактическому {actual_email}'
        actual_current_address = self.try_to_get_data(self.locator.CREATED_CURRENT_ADDRESS)
        assert actual_current_address == data[2], f'Ожидаемый результат: {data[2]} не ' \
                                            f'соответствует фактическому {actual_current_address}'
        actual_permanent_address = self.try_to_get_data(self.locator.CREATED_PERMANENT_ADDRESS)
        assert actual_permanent_address == data[3], f'Ожидаемый результат: {data[3]} не ' \
                                            f'соответствует фактическому {actual_permanent_address}'

    def check_result_with_incorrect_email(self):
        assert self.try_check_element_is_present(self.locator.EMAIL_INCORRECT) == True, "Отсутствует проверка " \
                                                                                        "правильности ввода EMAIL"

    def click_button(self):
        assert self.try_to_click_button(self.locator.SUBMIT_BUTTON), 'Кнопка Submit не представлена или не кликабельна'

    def fill_form(self):
        person_info = next(generator_person())
        assert self.try_to_fill_fild(self.locator.FULL_NAME, person_info.full_name), "Поле Full name не представлено " \
                                                                                     "(не найдено)"
        assert self.try_to_fill_fild(self.locator.EMAIL, person_info.email), "Поле Email не представлено " \
                                                                             "(не найдено)"
        assert self.try_to_fill_fild(self.locator.CURRENT_ADDRESS,
                                     person_info.current_address), "Поле Current address не представлено (не найдено)"
        assert self.try_to_fill_fild(self.locator.PERMANENT_ADDRESS,
                                 person_info.permanent_address), "Поле Permanent address не представлено (не найдено) "
        return person_info.full_name, person_info.email, person_info.current_address, person_info.permanent_address

    def fill_form_incorrect_email(self):
        person_info = next(generator_person())
        assert self.try_to_fill_fild(self.locator.FULL_NAME, person_info.full_name), "Поле Full name не представлено " \
                                                                                     "(не найдено)"
        assert self.try_to_fill_fild(self.locator.EMAIL, time.time()), "Поле Email не представлено " \
                                                                             "(не найдено)"
        assert self.try_to_fill_fild(self.locator.CURRENT_ADDRESS,
                                     person_info.current_address), "Поле Current address не представлено (не найдено)"
        assert self.try_to_fill_fild(self.locator.PERMANENT_ADDRESS,
                                 person_info.permanent_address), "Поле Permanent address не представлено (не найдено) "
        return person_info.full_name, person_info.email, person_info.current_address, person_info.permanent_address



class CheckBoxPage(BasePage):
    locator = CheckBoxPageLocators

    def expand_element(self):
        assert self.try_to_click_button(self.locator.PLUS_BUTTON), 'Кнопка ПЛЮС (развернуть) не представлена ' \
                                                                   'или не кликабельна'

    def collapse_element(self):
        assert self.try_to_click_button(self.locator.MINUS_BUTTON), 'Кнопка ПЛЮС (развернуть) не представлена ' \
                                                                   'или не кликабельна'

    def click_checkboxes_random(self):
        item_list = self.elements_are_present(self.locator.ITEM_LIST)

        random_value = random.randint(1, len(item_list))
        for box in range (0, random_value):
            item = item_list[random.randint(1, len(item_list))-1]
            self.go_to_element(item)
            item.click()

    def get_clicked_checkboxes(self):
        item_list = self.elements_are_present(self.locator.CHECKED_ITEM)
        data = []

        for box in item_list:
            clicked_title_item = \
            box.find_element(By.XPATH, self.locator.TITLE_ITEM).text.lower().replace(" ", "").split(".")[0]
            data.append(clicked_title_item)

        return data

    def get_presented_itens(self):
        item_list = self.elements_are_present(self.locator.RESULT_ITEM)
        data = []

        for box in item_list:
            data.append(box.text.lower())

        return data

    def compare_result(self, clicked_items, presented_item):
        assert clicked_items == presented_item, "Откликаннвый список не совбадает с представленным"









