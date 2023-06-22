import time
from selenium.webdriver.common.by import By
from pages.elements_page import TextBoxPage


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





