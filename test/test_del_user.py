# -*- coding: utf-8 -
from model.user import User
import random
import allure


def test_delete_some_user(app, db, check_ui):
    with allure.step('Checking count user'):
        if len(db.get_user_list()) == 0:
            app.user.create(User(firstname="test"))
    with allure.step('Given a user list and choosing user to delete'):
        old_users = db.get_user_list()
        user = random.choice(old_users)
    with allure.step('When I delete a user %s from the list' % user):
        app.user.delete_by_id(user.id)
    with allure.step('Then the new user list is equal to the old list without the deleted user'):
        new_users = db.get_user_list()
        assert len(old_users) - 1 == len(new_users)
        old_users.remove(user)
        assert old_users == new_users
        if check_ui:
            assert sorted(new_users, key=User.id_or_max) == sorted(app.user.get_users_list(), key=User.id_or_max)