# -*- coding: utf-8 -
from model.user import User
import random


def test_delete_some_user(app, db, check_ui):
    if len(db.get_user_list()) == 0:
        app.user.create(User(firstname="test"))
    old_users = db.get_user_list()
    user = random.choice(old_users)
    app.user.delete_by_id(user.id)
    new_users = db.get_user_list()
    assert len(old_users) - 1 == len(new_users)
    old_users.remove(user)
    assert old_users == new_users
    if check_ui:
        assert sorted(new_users, key=User.id_or_max) == sorted(app.user.get_users_list(), key=User.id_or_max)