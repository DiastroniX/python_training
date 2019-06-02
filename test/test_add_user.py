# -*- coding: utf-8 -*-

from model.user import User


def test_add_user(app, db, json_users):
    user = json_users
    old_users = db.get_user_list()
    app.user.create(user)
    new_users = db.get_user_list()
    old_users.append(user)
    assert sorted(old_users, key=User.id_or_max) == sorted(new_users, key=User.id_or_max)