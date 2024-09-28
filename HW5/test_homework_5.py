import os

from selene import browser, be, have, command


def test_hw_5():
    browser.open("")
    browser.element('#firstName').should(be.blank).type('Semen')
    browser.element('#lastName').should(be.blank).type('Shpak')
    browser.element('#userEmail').should(be.blank).type('ShpakS@mail.ru')
    browser.all('#genterWrapper>.col-md-9>.custom-radio').should(have.size(3))
    browser.all('#genterWrapper>.col-md-9>.custom-radio')[0].click()
    browser.element('#userNumber').should(be.blank).type('9543231207')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click().element('//option[@value="11"]').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('//option[@value="1986"]').perform(command.js.scroll_into_view).click()
    browser.element('.react-datepicker__day--004').click()
    browser.element('#subjectsInput').should(be.blank).type('c')
    browser.element('//div[text()="Chemistry"]').click()
    browser.element('#subjectsInput').should(be.blank).type('e')
    browser.element('//div[text()="English"]').click()
    browser.all('#hobbiesWrapper>.col-md-9>.custom-checkbox').wait.for_(have.size(3))
    browser.all('#hobbiesWrapper>.col-md-9>.custom-checkbox')[0].click()
    browser.all('#hobbiesWrapper>.col-md-9>.custom-checkbox')[1].click()
    browser.element('//input[@type="file"]').type(os.path.abspath(os.path.join(os.getcwd())) + '//photo1.jpg')
    browser.element('//textarea[@class="form-control"]').type('Ленинградская область, Гатчина, бульвар Авиаторов, 9')
    browser.element('#submit').perform(command.js.scroll_into_view)
    browser.element('//div[text()="Select State"]').click()
    browser.all('//div[@id="state"]//div[@class=" css-11unzgr"]//div[@class]').should(have.size(4))
    browser.element('#react-select-3-option-2').click()
    browser.element('//div[text()="Select City"]').click()
    browser.all('//div[@id="city"]//div[@class=" css-11unzgr"]//div[@class]').should(have.size(2))
    browser.element('#react-select-4-option-0').click()
    browser.element('#submit').click()
    browser.all('//tr//td[2]').should(have.exact_texts("Semen Shpak", "ShpakS@mail.ru", "Male", "9543231207",
                                                       "04 December,1986", "Chemistry, English", "Sports, Reading",
                                                       "photo1.jpg", "Ленинградская область, Гатчина, бульвар "
                                                                     "Авиаторов, 9", "Haryana Karnal"))
