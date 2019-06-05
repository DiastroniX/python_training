from model.user import User

def test_user_list(app, db):
    ui_list = app.user.get_users_list()
    def clean(user):
        return User(id=user.id, lastname=user.lastname.strip(), firstname=user.firstname.strip())
    db_list = map(clean, db.get_user_list())
    assert sorted(ui_list, key=User.id_or_max) == sorted(db_list, key=User.id_or_max)