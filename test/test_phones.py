import re
import allure


def test_phones_on_home_page(app):
    with allure.step('Given a phone list from homepage and edit page'):
        user_from_home_page = app.user.get_users_list()[0]
        user_from_edit_page = app.user.get_user_info_from_edit_page(0)
    with allure.step('Then the phone list from homepage is equal to the phone from edit page'):
        assert user_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(user_from_edit_page)

def test_phones_on_view_page(app):
    with allure.step('Given a phone list from viewpage and editpage '):
        user_from_view_page = app.user.get_users_from_view_page(0)
        user_from_edit_page = app.user.get_user_info_from_edit_page(0)
    with allure.step('Then the phone list from viewpage is equal to the phone from edit page'):
        assert user_from_view_page.home == user_from_edit_page.home
        assert user_from_view_page.mobile == user_from_edit_page.mobile
        assert user_from_view_page.work == user_from_edit_page.work
        assert user_from_view_page.phone2 == user_from_edit_page.phone2

def clear(s):
    return re.sub("[() -]]", "", s)

def merge_phones_like_on_home_page(user):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                        [user.home, user.mobile, user.work, user.phone2]))))