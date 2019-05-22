from sys import maxsize


class User:

    def __init__(self, firstname=None, lastname=None, company=None, address=None,
                        home=None, work=None, mobile=None, phone2=None, email=None, email2=None, email3=None,
                        address2=None, id=None, all_emails_from_home_page=None,  all_phones_from_home_page=None):
        self.firstname = firstname
        self.lastname = lastname
        self.company = company
        self.address = address
        self.home = home
        self.work = work
        self.mobile = mobile
        self.phone2 = phone2
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.address2 = address2
        self.id = id
        self.all_emails_from_home_page = all_emails_from_home_page
        self.all_phones_from_home_page = all_phones_from_home_page

    def __repr__(self):
        return "%s:%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s" % (self.id, self.firstname, self.company, self.address, self.home,
                                self.work, self.mobile, self.phone2, self.email, self.email2,
                                self.email3, self.address2)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and \
        (self.firstname is None or other.firstname is None or self.firstname == other.firstname) and \
        (self.lastname is None or other.lastname is None or self.lastname == other.lastname)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize