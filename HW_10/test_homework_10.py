import allure
from allure_commons.types import Severity
from selene import browser, have


@allure.tag("Web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "Valera")
@allure.feature("Issue")
@allure.story("Неавторизованный пользователь")
@allure.link("https://github.com/Deus1986/HW3", name="Testing")
def test_hw_10():
    browser.open("/")
    browser.element("#issues-tab").click()
    browser.element("#issue_1_link").should(have.text("home_work_10"))


@allure.tag("Web")
@allure.severity(Severity.BLOCKER)
@allure.label("owner", "Volodya", "Semen")
@allure.feature("killer feature")
@allure.story("Неавторизованный пользователь")
@allure.link("https://github.com/Deus1986/HW3", name="Testing")
def test_hw_10_with_allure_step():
    with allure.step("Открыть браузер"):
        browser.open("/")

    with allure.step("Нажать на Issue"):
        browser.element("#issues-tab").click()

    with allure.step("Проверить, что значение issue содержит текст 'home_work_10'"):
        browser.element("#issue_1_link").should(have.text("home_work_10"))


@allure.tag("Web")
@allure.severity(Severity.BLOCKER)
@allure.label("owner", "Eduard")
@allure.feature("Feature 1")
@allure.story("Неавторизованный пользователь")
@allure.link("https://github.com/Deus1986/HW3", name="Testing")
def test_hw_10_with_allure_decorator():
    browser_open()
    click_issue()
    should_have_text()


@allure.step("Открыть браузер")
def browser_open():
    browser.open("/")


@allure.step("Нажать на Issue")
def click_issue():
    browser.element("#issues-tab").click()


@allure.step("Проверить, что значение issue содержит текст 'home_work_10'")
def should_have_text():
    browser.element("#issue_1_link").should(have.text("home_work_10"))
