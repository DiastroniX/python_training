# -*- coding: utf-8 -

from model.user import User


def test_edit_first_user(app):
    if app.user.count() == 0:
        app.user.create(User(firstname="test"))
    old_users = app.user.get_users_list()
    user = User(firstname="Krolik",
                                  lastname="Ivanovich",
                                  company="Trololosik",
                                  address2="Kakoi-to")
    user.id = old_users[0].id
    app.user.edit_first(user)
    assert len(old_users) == app.user.count()
    new_users = app.user.get_users_list()
    old_users[0] = user
    assert sorted(old_users, key=User.id_or_max) == sorted(new_users, key=User.id_or_max)