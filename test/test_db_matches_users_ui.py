from model.user import User
import allure


def test_user_list(app, db):
    with allure.step('Given a user list from ui'):
        ui_list = app.user.get_users_list()
    with allure.step('Given a user list from db'):
        def clean(user):
            return User(id=user.id, lastname=user.lastname.strip(), firstname=user.firstname.strip())
    db_list = map(clean, db.get_user_list())
    with allure.step('Then the UI user list is equal to the DB user list'):
        assert sorted(ui_list, key=User.id_or_max) == sorted(db_list, key=User.id_or_max)