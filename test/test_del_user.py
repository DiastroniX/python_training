# -*- coding: utf-8 -
from model.user import User
from random import randrange


def test_delete_some_user(app):
    if app.user.count() == 0:
        app.user.create(User(firstname="test"))
    old_users = app.user.get_users_list()
    index = randrange(len(old_users))
    app.user.delete_by_index(index)
    assert len(old_users) - 1 == app.user.count()
    new_users = app.user.get_users_list()
    old_users[index:index+1] = []
    assert old_users == new_users