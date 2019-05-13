# -*- coding: utf-8 -
from model.user import User


def test_delete_first_user(app):
    if app.user.count() == 0:
        app.user.create(User(firstname="test"))
    old_users = app.user.get_users_list()
    app.user.delete_first_user()
    new_users = app.user.get_users_list()
    assert len(old_users) - 1 == len(new_users)
    old_users[0:1] = []
    assert old_users == new_users