from sys import maxsize


class User:

    def __init__(self, firstname=None, lastname=None, company=None, address=None,
                        home=None, work=None, mobile=None, phone2=None, email=None,
                        address2=None, id=None, all_phones_from_home_page=None):
        self.firstname = firstname
        self.lastname = lastname
        self.company = company
        self.address = address
        self.home = home
        self.work = work
        self.mobile = mobile
        self.phone2 = phone2
        self.email = email
        self.address2 = address2
        self.id = id
        self.all_phones_from_home_page = all_phones_from_home_page

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and \
        (self.firstname is None or other.firstname is None or self.firstname == other.firstname) and \
        (self.lastname is None or other.lastname is None or self.lastname == other.lastname)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize