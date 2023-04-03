from todomvc_testing.Model import todos




def test_e2e():
    todos.given_opened('11', '22', '33', '44')
    todos.should_be('11', '22', '33', '44')
    todos.toggle('22')
    todos.toggle('22')
    todos.toggle('33')

    todos.should_be_completed('33')
#
#     s('[href="#/active"]').click()
#     ss('#todo-list>li').should(have.exact_texts('11', '22', '44'))
#     s('[href="#/completed"]').click()
#     ss('#todo-list>li').should(have.exact_texts('33'))
#     ss('#todo-list>li').element_by(have.exact_text('33')).hover().element('.destroy').click()
#     ss('#todo-list>li').should(have.size(0))
#     s('[href="#/"]').click()
#     ss('#todo-list>li').element_by(have.exact_text('22')).double_click()
#     ss('#todo-list>li').element_by(have.css_class('editing')).element('.edit')\
#         .perform(command.js.set_value('11223344')).press_enter()
#     s("#toggle-all").click()
#     ss('#todo-list>li').element_by(have.exact_text('11')).element('.toggle').click()
#     browser.element('#clear-completed').click()
#     ss('#todo-list>li').should(have.size(1))
#     sleep(3)
#
#
#     # ss('#todo-list>li').element_by(have.exact_text('22')).double_click()
#
# # import pytest
# # from Full_setup_tests_todomvc.helpers.allure.gherkin import when, given, then
# # from Full_setup_tests_todomvc.helpers.pytest.skip import pending
#

#
#
# def test_add_first_todo():
#     todos.open()
#
#     todos.should_be_empty()
#
#     todos.add('a')
#
#     todos.should_be('a')
#     todos.should_be_items_left(1)
#
#
# def test_add_todos():
#     todos.open()
#
#     todos.should_be_empty()
#
#     todos.add('a', 'b', 'c')
#
#     todos.should_be('a', 'b', 'c')
#     todos.should_be_items_left(3)
#
#
# def test_edit():
#     todos.given_opened('a', 'b', 'c')
#
#     todos.edit('a', 'a edited')
#
#     todos.should_be('a edited', 'b', 'c')
#     todos.should_be_items_left(3)
#
#
# def test_edit_by_focus_change():
#     todos.given_opened('a', 'b', 'c')
#
#     todos.edit_by_focus_change('b', 'b edited')
#
#     todos.should_be('a', 'b edited', 'c')
#     todos.should_be_items_left(3)
#
#
# def test_cancel_edit():
#     todos.given_opened('a', 'b', 'c')
#
#     todos.cancel_edit('c', 'to be canceled')
#
#     todos.should_be('a', 'b', 'c')
#     todos.should_be_items_left(3)
#
#
# def test_complete():
#     todos.given_opened('a', 'b', 'c')
#
#     todos.toggle('a')
#
#     todos.should_be_completed('a')
#     todos.should_be_active('b', 'c')
#     todos.should_be_items_left(2)
#
#
# def test_activate():
#     todos.given_opened('a', 'b', 'c')
#     todos.toggle('b')
#
#     todos.toggle('b')
#
#     todos.should_be_active('a', 'b', 'c')
#     todos.should_be_completed()
#     todos.should_be_items_left(3)
#
#
# def test_complete_all():
#     todos.given_opened('a', 'b', 'c')
#
#     todos.toggle_all()
#
#     todos.should_be_completed('a', 'b', 'c')
#     todos.should_be_active()
#     todos.should_be_items_left(0)
#
#
# def test_activate_all():
#     todos.given_opened('a', 'b', 'c')
#     todos.toggle_all()
#
#     todos.toggle_all()
#
#     todos.should_be_active('a', 'b', 'c')
#     todos.should_be_completed()
#     todos.should_be_items_left(3)
#
#
# def test_clear_completed():
#     todos.given_opened('a', 'b', 'c', 'd', 'e')
#     todos.toggle('d')
#     todos.toggle('e')
#
#     todos.clear_completed()
#
#     todos.should_be('a', 'b', 'c')
#     todos.should_be_items_left(3)
#
#
# def test_delete():
#     todos.given_opened('a', 'b', 'c')
#
#     todos.delete('a')
#
#     todos.should_be('b', 'c')
#     todos.should_be_items_left(2)
#
#
# def test_delete_last_todo():
#     todos.given_opened('a')
#
#     todos.delete('a')
#
#     todos.should_be_empty()