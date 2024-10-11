from selene import browser, have

from HW3.data.users import User, UserData
from HW3.pages.registration_page import RegistrationPage


def test_registration_page():
    registration_page = RegistrationPage()
    registration_page.open_page()
    registration_page.fill_fully_name(User.user_semen["0"])
    registration_page.fill_user_email(User.user_semen["1"])
    registration_page.fill_current_address(User.user_semen["2"])
    registration_page.fill_permanent_address(User.user_semen["3"])
    registration_page.click_submit()
    registration_page.scroll_to_element()
    registration_page.should_have_registered(User.user_semen, UserData)
