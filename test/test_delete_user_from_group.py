from model.user import User
from model.group import Group
import random


def test_add_contact_to_group(app, orm):
    if len(orm.get_user_list()) == 0:
        app.user.create(User(firstname="test"))
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    user_list = orm.get_user_list()
    user = random.choice(user_list)
    group_list = orm.get_group_list()
    group = random.choice(group_list)
    if user in orm.get_users_not_in_group(group):
        app.user.add_to_group(user.id, group.id)
    app.user.delete_from_group(user.id, group)
    assert user in orm.get_users_not_in_group(group)