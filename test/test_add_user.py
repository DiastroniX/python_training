# -*- coding: utf-8 -*-
import pytest
from model.user import User
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_user(app):
        app.open_home_page()
        app.session.login(username="admin", password="secret")
        app.create_new_user(User(firstname="Barsik",
                                        lastname="Petrovich",
                                        company="Zmeeust",
                                        address="Mars avenue",
                                        home="777",
                                        email="nepishimne@trololo.urr",
                                        address2="Moy address USSR"))
        app.return_to_homepage()
        app.session.logout()
