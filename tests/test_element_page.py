import time
from selenium.webdriver.common.by import By
from pages.elements_page import TextBoxPage, CheckBoxPage


class TestTextBox:

    class Test_ElementTextBox:
        url = 'https://demoqa.com/text-box'


        def test_text_box(self, driver):
            textbox_page = TextBoxPage(driver, self.url)
            textbox_page.open()
            filled_form_data = textbox_page.fill_form()
            textbox_page.click_button()
            textbox_page.check_filled_form(filled_form_data)


        def test_incorrect_email(self, driver):
            textbox_page = TextBoxPage(driver,self.url)
            textbox_page.open()
            textbox_page.fill_form_incorrect_email()
            textbox_page.click_button()
            textbox_page.check_result_with_incorrect_email()

        class Test_ElementCheckBox:
            url = 'https://demoqa.com/checkbox'

            def test_plus_and_minus_work(self, driver):
                checkbox_page = CheckBoxPage(driver, self.url)
                checkbox_page.open()
                checkbox_page.expand_element()
                checkbox_page.collapse_element()

            def test_checkboxes_work_correct(self, driver):
                checkbox_page = CheckBoxPage(driver, self.url)
                checkbox_page.open()
                checkbox_page.expand_element()
                checkbox_page.click_checkboxes_random()
                checkbox_page.get_clicked_checkboxes()
                clicked_items = checkbox_page.get_clicked_checkboxes()
                presented_item = checkbox_page.get_presented_itens()
                checkbox_page.compare_result(clicked_items, presented_item)






