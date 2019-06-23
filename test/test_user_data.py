import re
from model.user import User
import allure


def test_data_on_home_page(app, db):
    with allure.step('Checking user count'):
        if app.user.count() == 0:
            app.user.create(User(firstname="test"))
    with allure.step('Given a user list from UI and DB'):
        users_from_home_page = app.user.get_users_list()
        users_from_db = db.get_user_list()
    with allure.step('Then the user list from UI is equal to the user list from DB'):
        assert len(users_from_home_page) == len(users_from_db)
        users_from_home_page = sorted(users_from_home_page, key=User.id_or_max)
        users_from_db = sorted(users_from_db, key=User.id_or_max)
        for i in range(len(users_from_db)):
            compare(users_from_home_page[i], users_from_db[i])

def compare(users_from_home_page, users_from_db):
    assert users_from_home_page.address == users_from_db.address
    assert users_from_home_page.firstname == users_from_db.firstname
    assert users_from_home_page.lastname == users_from_db.lastname
    assert users_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(users_from_db)
    assert users_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(users_from_db)


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