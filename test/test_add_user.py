# -*- coding: utf-8 -*-

from model.user import User
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [User(firstname="",
                lastname="",
                company="",
                address="",
                home="",
                work="",
                mobile="",
                phone2="",
                email="",
                email2="",
                email3="",
                address2="")] + [
    User(firstname=random_string("firstname", 12), lastname=random_string("lastname", 12), company=random_string("company", 15),
         address=random_string("address", 30), home=random_string("hometel", 15), work=random_string("worktel", 10),
         mobile=random_string("mobiletel", 10), phone2=random_string("phone2tel", 10), email=random_string("email@", 10),
         email2=random_string("email2@", 10), email3=random_string("email3@", 10), address2=random_string("address2", 20),)
    for i in range(5)
]

@pytest.mark.parametrize("user", testdata, ids=[repr(x) for x in testdata])
def test_add_user(app, user):
    old_users = app.user.get_users_list()
    app.user.create(user)
    assert len(old_users) + 1 == app.user.count()
    new_users = app.user.get_users_list()
    old_users.append(user)
    assert sorted(old_users, key=User.id_or_max) == sorted(new_users, key=User.id_or_max)