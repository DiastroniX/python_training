import re

def test_phones_on_home_page(app):
    user_from_home_page = app.user.get_users_list()[0]
    user_from_edit_page = app.user.get_user_info_from_edit_page(0)
    assert user_from_home_page.home == clear(user_from_edit_page.home)
    assert user_from_home_page.work == clear(user_from_edit_page.work)
    assert user_from_home_page.mobile == clear(user_from_edit_page.mobile)
    assert user_from_home_page.phone2 == clear(user_from_edit_page.phone2)

def test_phones_on_view_page(app):
    user_from_view_page = app.user.get_users_from_view_page(0)
    user_from_edit_page = app.user.get_user_info_from_edit_page(0)
    assert user_from_view_page.home == user_from_edit_page.home
    assert user_from_view_page.work == user_from_edit_page.work
    assert user_from_view_page.mobile == user_from_edit_page.mobile
    assert user_from_view_page.phone2 == user_from_edit_page.phone2

def clear(s):
    return re.sub("[() -]]", "", s)