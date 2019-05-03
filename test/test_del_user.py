# -*- coding: utf-8 -


def test_delete_first_user(app):
    app.user.delete_first_user()