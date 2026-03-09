class ContactHelper:

    def __init__(self, app):
        self.app = app

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.app.change_field_value("firstname", contact.first_name)
        self.app.change_field_value("middlename", contact.middle_name)
        self.app.change_field_value("lastname", contact.last_name)
        self.app.change_field_value("title", contact.title)
        self.app.change_field_value("company", contact.company)
        self.app.change_field_value("address", contact.address)
        self.app.change_field_value("home", contact.home)
        self.app.change_field_value("email", contact.email)


    def create(self, contact):
        wd = self.app.wd
        self.app.return_home_page()
        #init contact creation
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        #submit contact
        wd.find_element_by_xpath("//input[19]").click()
        self.app.return_home_page()

    def delete_first_contact(self):
        wd = self.app.wd
        self.app.return_home_page()
        #select first contact
        wd.find_element_by_name("selected[]").click()
        #delete contact
        wd.find_element_by_name("delete").click()
        self.app.return_home_page()

    def edit_first_contact(self, contact):
        wd = self.app.wd
        self.app.return_home_page()
        #init edit first contact
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.fill_contact_form(contact)
        #submit changes
        wd.find_element_by_name("update").click()
        self.app.return_home_page()

    def count(self):
        wd = self.app.wd
        self.app.return_home_page()
        return len(wd.find_elements_by_name("selected[]"))