# -*- coding: utf-8 -*-

from model.group import Group


def test_edit_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first(Group(name="nichego", header="tak", footer="byvaet :)"))
    app.session.logout()