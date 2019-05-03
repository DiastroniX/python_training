# -*- coding: utf-8 -*-

from model.group import Group


def test_edit_first_group_name(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first(Group(name="nichego"))
    app.session.logout()

def test_edit_first_group_header(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first(Group(header="tak"))
    app.session.logout()

def test_edit_first_group_footer(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first(Group(footer="byvaet :)"))
    app.session.logout()