from selene import browser
from selene.support.conditions import have
from selene.support.jquery_style_selectors import s, ss

browser.config.hold_browser_open = True
browser.open('http://todomvc.com/examples/emberjs/')

s('#new-todo').type('Dima').press_enter()
s('#new-todo').type('Max').press_enter()
s('#new-todo').type('Evgen').press_enter()
s('#new-todo').type('Alina').press_enter()
s('#new-todo').type('Valik').press_enter()

ss('#todo-list>li').should(have.exact_texts('Dima', 'Max', 'Evgen', 'Alina', 'Valik'))





















# from selene import have
# from selene.support.shared import browser
#
#
# def test_complete_todo():
#     browser.open('http://todomvc.com/examples/emberjs/')
#
#     browser.element('#new-todo').type('a').press_enter()
#     browser.element('#new-todo').type('b').press_enter()
#     browser.element('#new-todo').type('c').press_enter()
#     browser.all('#todo-list>li').should(have.exact_texts('a', 'b', 'c'))
#
#     browser.element('#todo-list>li:nth-of-type(2) .toggle').click()
#     browser.all('#todo-list>li.completed').should(have.texts('b'))
#     browser.all('#todo-list>li:not(.completed)').should(have.exact_texts('a', 'c'))