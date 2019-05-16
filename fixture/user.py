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
        self.user_cache = None

    def delete_first(self):
        self.delete_by_index(0)

    def delete_by_index(self, index):
        wd = self.app.wd
        self.open_homepage()
        # select user with delete parameter
        self.select_user_by_index(index, 'delete')
        # click delete button
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # accept delete user
        wd.switch_to_alert().accept()
        # wait message
        wd.find_elements_by_css_selector("div.msgbox")
        self.return_to_homepage()
        self.user_cache = None

    def edit_first(self):
        wd = self.app.wd
        self.edit_by_index(0)

    def edit_by_index(self, index, new_user_data):
        wd = self.app.wd
        self.open_homepage()
        # select user with edit parameter
        self.select_user_by_index(index, "edit")
        # fill new data
        self.fill_user_form(new_user_data)
        # update form button
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
        self.return_to_homepage()
        self.user_cache = None

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

    def select_first_user(self, find_type_marker):
        wd = self.app.wd
        if find_type_marker == 'edit':
            wd.find_element_by_xpath("//img[@alt='Edit']").click()
        elif find_type_marker == 'delete':
            wd.find_element_by_name("selected[]").click()

    def select_user_by_index(self, index, find_type_marker):
        wd = self.app.wd
        if find_type_marker == 'edit':
            wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
        elif find_type_marker == 'delete':
            wd.find_elements_by_name("selected[]")[index].click()

    def count(self):
        wd = self.app.wd
        self.open_homepage()
        return len(wd.find_elements_by_name("selected[]"))

    user_cache = None

    def get_users_list(self):
        if self.user_cache is None:
            wd = self.app.wd
            self.open_homepage()
            self.user_cache = []
            for element in wd.find_elements_by_name("entry"):
                td = element.find_elements_by_tag_name("td")
                id = td[0].find_element_by_name("selected[]").get_attribute("value")
                first_name = td[2].text
                last_name = td[1].text
                self.user_cache.append(User(firstname=first_name, lastname=last_name, id=id))
        return list(self.user_cache)