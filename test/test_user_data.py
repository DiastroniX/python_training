import re
from random import randrange
from model.user import User

def test_data_on_home_page(app):
    if app.user.count() == 0:
        app.user.create(User(firstname="test"))
    index = randrange(len(app.user.get_users_list()))
    user_from_home_page = app.user.get_users_list()[index]
    user_from_edit_page = app.user.get_user_info_from_edit_page(index)
    assert user_from_home_page.lastname == user_from_edit_page.lastname
    assert user_from_home_page.firstname == user_from_edit_page.firstname
    assert user_from_home_page.address == user_from_edit_page.address
    assert user_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(user_from_edit_page)
    assert user_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(user_from_edit_page)


def clear(s):
    return re.sub("[() -]]", "", s)

def merge_phones_like_on_home_page(user):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                        [user.home, user.mobile, user.work, user.phone2]))))

def merge_emails_like_on_home_page(user):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [user.email, user.email2, user.email3]))))