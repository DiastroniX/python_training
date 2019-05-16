# -*- coding: utf-8 -
from model.user import User
from random import randrange


def test_edit_some_user(app):
    if app.user.count() == 0:
        app.user.create(User(firstname="test"))
    old_users = app.user.get_users_list()
    index = randrange(len(old_users))
    user = User(firstname="Krolik",
                                  lastname="Ivanovich",
                                  company="Trololosik",
                                  address2="Kakoi-to")
    user.id = old_users[index].id
    app.user.edit_by_index(index, user)
    assert len(old_users) == app.user.count()
    new_users = app.user.get_users_list()
    old_users[index] = user
    assert sorted(old_users, key=User.id_or_max) == sorted(new_users, key=User.id_or_max)