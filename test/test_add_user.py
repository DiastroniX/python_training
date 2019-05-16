# -*- coding: utf-8 -*-
from model.user import User


def test_add_user(app):
    old_users = app.user.get_users_list()
    user =  User(firstname="Barsik",
                lastname="Petrovich",
                company="Zmeeust",
                address="Mars avenue",
                home="777",
                email="nepishimne@trololo.urr",
                address2="Moy address USSR")
    app.user.create(user)
    assert len(old_users) + 1 == app.user.count()
    new_users = app.user.get_users_list()
    old_users.append(user)
    assert sorted(old_users, key=User.id_or_max) == sorted(new_users, key=User.id_or_max)