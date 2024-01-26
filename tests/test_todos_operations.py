from selene import browser, have, be
# from pythonProject1.conditions import match


def test_complete_todo():

    browser.open('/')
    browser.element('.new-todo').should(be.blank)
    browser.element('.new-todo').type('a').press_enter()
    browser.element('.new-todo').type('b').press_enter()
    browser.element('.new-todo').type('c').press_enter()
    browser.all('.todo-list>li').with_(timeout=4.0).should(have.size(3))
