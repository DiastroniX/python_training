# -*- coding: utf-8 -
from model.user import User


def test_delete_first_user(app):
    if app.user.count() == 0:
        app.user.create(User(firstname="test"))
    app.user.delete_first_user()