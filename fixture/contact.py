class ContactHelper:

    def __init__(self, app):
        self.app = app

    def fill_contact_form(self, contact):
        wd = self.app.wd
        #fill contact form
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.first_name)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.last_name)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.home)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email)

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