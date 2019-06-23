from model.user import User
from model.group import Group
import random
import allure

def test_add_user_to_group(app, orm):
    with allure.step('Check group and contact'):
        if len(orm.get_user_list()) == 0:
            app.user.create(User(firstname="test"))
        if len(orm.get_group_list()) == 0:
            app.group.create(Group(name="test"))
    with allure.step('Given a user list'):
        user_list = orm.get_user_list()
    with allure.step('Getting a random user from list'):
        user = random.choice(user_list)
    with allure.step('Given a group list'):
        group_list = orm.get_group_list()
    with allure.step('Getting a random group from list'):
        group = random.choice(group_list)
    with allure.step('When I add a contact %s to the group %s' % (user, group)):
        app.user.add_to_group(user.id, group.id)
    with allure.step('Then the new user in the group'):
        assert user in orm.get_users_in_group(group)