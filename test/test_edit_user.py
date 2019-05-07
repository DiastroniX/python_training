# -*- coding: utf-8 -

from model.user import User


def test_edit_first_user(app):
    if app.user.count() == 0:
        app.user.create(User(firstname="test"))
    app.user.edit_first(User(firstname="Krolik",
                                  lastname="Ivanovich",
                                  company="Trololosik",
                                  address2="Kakoi-to"))