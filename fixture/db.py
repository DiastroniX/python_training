from model.group import Group
from model.user import User
import pymysql.cursors


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT group_id, group_name, group_header, group_footer FROM group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_user_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT address, address2, company, email, email2, email3, firstname, home, id, lastname, mobile, phone2, work FROM addressbook WHERE deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (address, address2, company, email, email2, email3, firstname, home, id, lastname, mobile, phone2, work) = row
                list.append(User(address=address, address2=address2, company=company, email=email,
                                email2=email2, email3=email3, firstname=firstname, home=home, id=str(id),
                                lastname=lastname, mobile=mobile, phone2=phone2, work=work))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()