from pony.orm import *
from datetime import datetime
from model.group import Group
from model.user import User


class ORMFixture:

    db = Database()

    class ORMGroup(db.Entity):
        _table_ = "group_list"
        id = PrimaryKey(int, column="group_id")
        name = Optional(str, column="group_name")
        header = Optional(str, column="group_header")
        footer = Optional(str, column="group_footer")
        users = Set(lambda: ORMFixture.ORMUser, table="address_in_groups", column="id", reverse="groups", lazy=True)

    class ORMUser(db.Entity):
        _table_ = "addressbook"
        id = PrimaryKey(int, column="id")
        address = Optional(str, column="address")
        address2 = Optional(str, column="address2")
        company =Optional(str, column="company")
        email = Optional(str, column="email")
        email2 = Optional(str, column="email2")
        email3 = Optional(str, column="email3")
        firstname = Optional(str, column="firstname")
        home = Optional(str, column="home")
        lastname = Optional(str, column="lastname")
        mobile = Optional(str, column="mobile")
        phone2 = Optional(str, column="phone2")
        work = Optional(str, column="work")
        deprecated = Optional(datetime, column="deprecated")
        groups = Set(lambda: ORMFixture.ORMGroup, table="address_in_groups", column="group_id", reverse="users", lazy=True)

    def __init__(self, host, name, user, password):
        self.db.bind("mysql", host=host, database=name, user=user, password=password, autocommit=True) # working without decoders
        self.db.generate_mapping()

    def convert_groups_to_model(self, groups):
        def convert(group):
            return Group(id=str(group.id), name=group.name, header=group.header, footer=group.footer)
        return list(map(convert, groups))

    def convert_users_to_model(self, users):
        def convert(user):
            return User(id=str(user.id), address=user.address, address2=user.address2, company=user.company, email=user.email,
                                email2=user.email2, email3=user.email3, firstname=user.firstname, home=user.home,
                                lastname=user.lastname, mobile=user.mobile, phone2=user.phone2, work=user.work)
        return list(map(convert, users))


    @db_session
    def get_group_list(self):
       return self.convert_groups_to_model(select(g for g in ORMFixture.ORMGroup))

    @db_session
    def get_user_list(self):
       return self.convert_users_to_model(select(c for c in ORMFixture.ORMUser if c.deprecated is None))

    @db_session
    def get_users_in_group(self, group):
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id == group.id))[0]
        return self.convert_users_to_model(orm_group.users)

    @db_session
    def get_users_not_in_group(self, group):
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id == group.id))[0]
        return self.convert_users_to_model(
            select(c for c in ORMFixture.ORMUser if c.deprecated is None and orm_group not in c.groups))
