from model.user import User
import re

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

    def open_by_index(self, index):
        wd = self.app.wd
        self.open_homepage()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def fill_user_form(self, user):
        wd = self.app.wd
        self.change_field_value("firstname", user.firstname)
        self.change_field_value("lastname", user.lastname)
        self.change_field_value("company", user.company)
        self.change_field_value("address", user.address)
        self.change_field_value("home", user.home)
        self.change_field_value("work", user.work)
        self.change_field_value("mobile", user.mobile)
        self.change_field_value("phone2", user.phone2)
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
                last_name = td[1].text
                first_name = td[2].text
                address = td[3].text
                all_emails = td[4].text
                all_phones = td[5].text
                self.user_cache.append(User(id=id, lastname=last_name, firstname=first_name,
                                            address=address, all_emails_from_home_page=all_emails, all_phones_from_home_page=all_phones))
        return list(self.user_cache)

    def get_user_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_homepage()
        self.select_user_by_index(index, "edit")
        id = wd.find_element_by_name("id").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        home = wd.find_element_by_name("home").get_attribute("value")
        work = wd.find_element_by_name("work").get_attribute("value")
        mobile = wd.find_element_by_name("mobile").get_attribute("value")
        phone2 = wd.find_element_by_name("phone2").get_attribute("value")
        return User(id=id, lastname=lastname, firstname=firstname, address=address,
                    email=email, email2=email2, email3=email3,
                    home=home, mobile=mobile, work=work, phone2=phone2)

    def get_users_from_view_page(self, index):
        wd = self.app.wd
        self.open_homepage()
        self.open_by_index(index)
        text = wd.find_element_by_id("content").text
        home = re.search("H: (.*)", text).group(1)
        work = re.search("W: (.*)", text).group(1)
        mobile = re.search("M: (.*)", text).group(1)
        phone2 = re.search("P: (.*)", text).group(1)
        return User(home=home, mobile=mobile, work=work, phone2=phone2)