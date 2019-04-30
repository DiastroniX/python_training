# -*- coding: utf-8 -*-
from model.user import User


def test_add_user(app):
        app.open_home_page()
        app.session.login(username="admin", password="secret")
        app.user.create(User(firstname="Barsik",
                             lastname="Petrovich",
                             company="Zmeeust",
                             address="Mars avenue",
                             home="777",
                             email="nepishimne@trololo.urr",
                             address2="Moy address USSR"))
        app.user.return_to_homepage()
        app.session.logout()