# -*- coding: utf-8 -
from model.user import User
import random


def test_edit_some_user(app, db, check_ui):
    if len(db.get_user_list()) == 0:
        app.user.create(User(firstname="test"))
    user_replacement = User(firstname="Krolik",
                                  lastname="Ivanovich",
                                  company="Trololosik",
                                  address2="Kakoi-to")
    old_users = db.get_user_list()
    user = random.choice(old_users)
    app.user.edit_by_id(user.id, user_replacement)
    new_users = db.get_user_list()
    assert len(old_users) == len(new_users)
    if check_ui:
        assert sorted(new_users, key=User.id_or_max) == sorted(app.user.get_users_list(), key=User.id_or_max)