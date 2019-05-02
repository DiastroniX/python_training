# -*- coding: utf-8 -

from model.user import User


def test_edit_first_user(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.user.edit_first(User(firstname="Krolik",
                                  lastname="Ivanovich",
                                  company="Trololosik",
                                  address="Luna_Avenue_1",
                                  home="15",
                                  email="pishimne@pomada.lol",
                                  address2="Kakoi-to"))
    app.user.return_to_homepage()
    app.session.logout()