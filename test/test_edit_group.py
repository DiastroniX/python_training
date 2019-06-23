# -*- coding: utf-8 -*-
from model.group import Group
import random
import allure


def test_edit_group_name(app, db, check_ui):
    with allure.step('Checking count group'):
        if len(db.get_group_list()) == 0:
            app.group.create(Group(name="test"))
    with allure.step('Given a group list and group to modify'):
        old_groups = db.get_group_list()
        group = random.choice(old_groups)
    with allure.step('When I change a group info to %s' % group):
        app.group.edit_group_by_id(group.id, group)
    with allure.step('Then the new group list is equal to the old list with new group info'):
        new_groups = db.get_group_list()
        assert len(old_groups) == len(new_groups)
        if check_ui:
            assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)