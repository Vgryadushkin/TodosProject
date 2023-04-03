# from selene import have
#
# from selene.support.shared import browser
#
# from selene.support.shared.jquery_style import s, ss
#
# # Given
# browser.open('https://duckduckgo.com/')
#
# # When
# s('[name="q"]').type('it step').press_enter()
# # browser.all('[id="r1-0""]').click()
# ss('[data-testid="result-title-a"]').first.click()
#
# s('.menu__link').click()
#
# step_mentions = s('body:').element_by_text('step').count
# assert step_mentions > 0

# Then
# browser.all('[href="/yashaka/selene"]').should(have.size(3))

import re
from selene.support.jquery_style_selectors import s, ss
from selene.support.shared import browser


def test_step_on_dou_selene():
    # Go to duckduckgo.com and search for "itstep"
    browser.open('https://duckduckgo.com/')
    s('[name="q"]').type('itstep').press_enter()

    # Click on the first result
    s('#r1-0 > div.ikg2IXiCD14iVX7AdZo1 > h2 > a').click()

    # Click on the "Про Академію" link
    s('#academy_app > header > div.header__bottom > nav > ul > li:nth-child(1) > a').click()

    # Підрахувати кількість збігів на сторінці
    page_text = s('#academy_app')

    page_text = browser.driver.page_source.lower()
    count = page_text.count('step')
    print('Слово step повторяется на этой странице:', count, 'раз')