

class UserHelper:

    def __init__(self, app):
        self.app = app

    def create(self, user):
        wd = self.app.wd
        # init add new user
        wd.find_element_by_link_text("add new").click()
        # fill user form
        self.fill_user_data(user)
        # submit form
        wd.find_element_by_xpath("//input[21]").click()

    def delete_first_user(self):
        wd = self.app.wd
        # select first user
        wd.find_element_by_name("selected[]").click()
        # click delete button
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # accept delete user
        wd.switch_to_alert().accept()
        # wait message
        wd.find_elements_by_css_selector("div.msgbox")

    def edit_first(self, user):
        wd = self.app.wd
        # push edit button on first user
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        # fill new data
        self.fill_user_data(user)
        # update form button
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()

    def fill_user_data(self, user):
        wd = self.app.wd
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(user.firstname)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(user.lastname)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(user.company)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(user.address)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(user.home)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(user.email)
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(user.address2)

    def return_to_homepage(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()