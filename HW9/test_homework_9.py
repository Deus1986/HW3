from HW3.data.users import user_semen
from HW3.pages.registration_page import RegistrationPage


def test_hw_5():
    registration_page = RegistrationPage()
    registration_page.open_page()
    registration_page.fill_name(user_semen.name)
    registration_page.fill_lastname(user_semen.last_name)
    registration_page.fill_user_email(user_semen.email)
    registration_page.choose_gender(user_semen.gender)
    registration_page.fill_user_number(user_semen.number)
    registration_page.choose_day_birthday(user_semen.birthday)
    registration_page.choose_subject('c', 'Chemistry')
    registration_page.choose_subject('e', 'English')
    registration_page.choose_hobby('Sports')
    registration_page.choose_hobby('Reading')
    registration_page.load_photo('//photo1.jpg')
    registration_page.fill_address(user_semen.current_address)
    registration_page.scroll_to_element('#submit')
    registration_page.select_state("Haryana")
    registration_page.select_city("Karnal")
    registration_page.click_submit()
    registration_page.should_have_registered(user_semen.name + " " + user_semen.last_name,
                                             user_semen.email, user_semen.gender, user_semen.number,
                                             user_semen.birthday, "Chemistry, English",
                                             "Sports, Reading", "photo1.jpg",
                                             user_semen.current_address, "Haryana Karnal")
