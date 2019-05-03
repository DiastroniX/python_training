# -*- coding: utf-8 -*-

from model.group import Group


def test_edit_first_group_name(app):
    app.group.edit_first(Group(name="nichego"))


def test_edit_first_group_header(app):
    app.group.edit_first(Group(header="tak"))


def test_edit_first_group_footer(app):
    app.group.edit_first(Group(footer="byvaet :)"))