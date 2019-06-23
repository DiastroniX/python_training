from model.user import User
from model.group import Group
import random
import allure


def test_add_contact_to_group(app, orm):
    with allure.step('Checking group and user count'):
        if len(orm.get_user_list()) == 0:
            app.user.create(User(firstname="test"))
        if len(orm.get_group_list()) == 0:
            app.group.create(Group(name="test"))
    with allure.step('Given a group list, user list and choosing random for both'):
        user_list = orm.get_user_list()
        user = random.choice(user_list)
        group_list = orm.get_group_list()
        group = random.choice(group_list)
    with allure.step('Checking if user %s not in the group %s ' % (user, group)):
        if user in orm.get_users_not_in_group(group):
            app.user.add_to_group(user.id, group.id)
    with allure.step('When I remove a user %s from the group %s' % (user, group)):
        app.user.delete_from_group(user.id, group)
    with allure.step('Then a %s user not in %s group' % (user, group)):
        assert user in orm.get_users_not_in_group(group)