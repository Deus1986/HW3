import pytest
from selene import browser, be, command, have


class RegistrationPage:
    def __init__(self):
        pass

    def open_page(self):
        browser.open("/")
        browser.driver.execute_script("$('#fixedban').remove()")
        browser.driver.execute_script("$('footer').remove()")

    def fill_fully_name(self, value):
        browser.element('#userName').should(be.blank).type(value)

    def fill_user_email(self, email_address):
        browser.element('#userEmail').should(be.blank).type(email_address)

    def fill_current_address(self, value):
        browser.element('//textarea[@id="currentAddress"]').type(value)

    def fill_permanent_address(self, value):
        browser.element('//textarea[@id="permanentAddress"]').type(value)

    def scroll_to_element(self):
        browser.element('#permanentAddress').perform(command.js.scroll_into_view)

    def click_submit(self):
        browser.element('#submit').click()

    def should_have_registered(self, user_data, user_enum):
        for i in range(len(user_data)):
            browser.element(f"#output > div.border > #{user_enum(i).name}").should(have.text(user_data[f'{i}']))
