# -*- coding: utf-8 -*-
from model.user import User
import allure


def test_add_user(app, db, json_users):
    user = json_users
    with allure.step('Given a contact list'):
        old_users = db.get_user_list()
    with allure.step('When I add a user %s to the list' % user):
        app.user.create(user)
    with allure.step('Then the new user list is equal to the old list with the added user'):
        new_users = db.get_user_list()
        old_users.append(user)
        assert sorted(old_users, key=User.id_or_max) == sorted(new_users, key=User.id_or_max)