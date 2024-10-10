import re
from selene import browser, be, command, have
from HW3.resources import resource_path


class RegistrationPage:
    def __init__(self):
        # попробовать для себя
        self.last_name = browser.element('#lastName')

    def open_page(self):
        browser.open("")
        browser.driver.execute_script("$('#fixedban').remove()")
        browser.driver.execute_script("$('footer').remove()")

    def fill_name(self, value):
        browser.element('#firstName').should(be.blank).type(value)

    def fill_lastname(self, value):
        self.last_name.should(be.blank).type(value)

    def fill_user_email(self, email_address):
        browser.element('#userEmail').should(be.blank).type(email_address)

    def choose_gender(self, value):
        browser.element(f'//label[text() = "{value}"]').click()

    def fill_user_number(self, value):
        browser.element('#userNumber').should(be.blank).type(value)

    def choose_day_birthday(self, value):
        birthday = re.split(",|\s", value)
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').click().element(f'//option[text()= "{birthday[1]}"]').click()
        browser.element('.react-datepicker__year-select').click()
        browser.element(f'//option[@value="{birthday[2]}"]').perform(command.js.scroll_into_view).click()
        browser.element(f'.react-datepicker__day--0{birthday[0]}').click()

    def choose_subject(self, first_letter_of_subject, subject_name):
        browser.element('#subjectsInput').should(be.blank).type(first_letter_of_subject)
        browser.element(f'//div[text()="{subject_name}"]').click()

    def choose_hobby(self, value):
        browser.element(f'//label[text()="{value}"]').click()

    def load_photo(self, photo_path):
        browser.element('//input[@type="file"]').type(resource_path(photo_path))

    def fill_address(self, value):
        browser.element('//textarea[@class="form-control"]').type(value)

    def scroll_to_element(self, locator):
        browser.element(locator).perform(command.js.scroll_into_view)

    def select_state(self, value):
        browser.element('//div[text()="Select State"]').click()
        browser.all('//div[@id="state"]//div[@class=" css-11unzgr"]//div[@class]').should(have.size(4))
        browser.element(f'//div[text() = "{value}"]').click()

    def select_city(self, value):
        browser.element('//div[text()="Select City"]').click()
        browser.all('//div[@id="city"]//div[@class=" css-11unzgr"]//div[@class]').should(have.size(2))
        browser.element(f'//div[text() = "{value}"]').click()

    def click_submit(self):
        browser.element('#submit').click()

    def should_have_registered(self, student_name, student_email, student_gender, student_number, student_birthday,
                               student_subjects, student_hobbies, student_photo, student_current_address,
                               student_state_and_city):
        browser.all('//tr//td[2]').should(
            have.exact_texts(student_name, student_email, student_gender, student_number, student_birthday,
                             student_subjects, student_hobbies, student_photo, student_current_address,
                             student_state_and_city))
