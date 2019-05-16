from model.user import User

class UserHelper:

    def __init__(self, app):
        self.app = app

    def create(self, new_user_data):
        wd = self.app.wd
        self.open_homepage()
        # init add new user
        wd.find_element_by_link_text("add new").click()
        # fill user form
        self.fill_user_form(new_user_data)
        # submit form
        wd.find_element_by_xpath("//input[21]").click()
        self.return_to_homepage()

    def delete_first_user(self):
        wd = self.app.wd
        self.open_homepage()
        # select first user
        wd.find_element_by_name("selected[]").click()
        # click delete button
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # accept delete user
        wd.switch_to_alert().accept()
        # wait message
        wd.find_elements_by_css_selector("div.msgbox")
        self.return_to_homepage()

    def edit_first(self, new_user_data):
        wd = self.app.wd
        self.open_homepage()
        # push edit button on first user
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        # fill new data
        self.fill_user_form(new_user_data)
        # update form button
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
        self.return_to_homepage()

    def fill_user_form(self, user):
        wd = self.app.wd
        self.change_field_value("firstname", user.firstname)
        self.change_field_value("lastname", user.lastname)
        self.change_field_value("company", user.company)
        self.change_field_value("address", user.address)
        self.change_field_value("home", user.home)
        self.change_field_value("email", user.email)
        self.change_field_value("address2", user.address2)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def return_to_homepage(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/") and len(wd.find_elements_by_name("searchstring")) > 0):
            wd.find_element_by_link_text("home").click()

    def open_homepage(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/") and len(wd.find_elements_by_name("searchstring")) > 0):
            wd.find_element_by_link_text("home").click()

    def count(self):
        wd = self.app.wd
        self.open_homepage()
        return len(wd.find_elements_by_name("selected[]"))

    def get_users_list(self):
        wd = self.app.wd
        self.open_homepage()
        users = []
        for element in wd.find_elements_by_name("entry"):
            td = element.find_elements_by_tag_name("td")
            id = td[0].find_element_by_name("selected[]").get_attribute("value")
            first_name = td[2].text
            last_name = td[1].text
            users.append(User(firstname=first_name, lastname=last_name, id=id))
        return users