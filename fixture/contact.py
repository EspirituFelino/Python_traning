from model.contact import Contact


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
        self.contacts_cache = None

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.app.return_home_page()
        self.select_contact_by_index(index)
        #delete contact
        wd.find_element_by_name("delete").click()
        self.app.return_home_page()
        self.contacts_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def edit_contact_by_index(self, contact, index):
        wd = self.app.wd
        self.app.return_home_page()
        self.init_edit_contact_by_index(index)
        self.fill_contact_form(contact)
        #submit changes
        wd.find_element_by_name("update").click()
        self.app.return_home_page()
        self.contacts_cache = None

    def edit_first_contact(self):
            self.edit_contact_by_index(0)

    def init_edit_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()

    def count(self):
        wd = self.app.wd
        self.app.return_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contacts_cache = None

    def get_contact_list(self):
        if self.contacts_cache is None:
            wd = self.app.wd
            self.app.return_home_page()
            self.contacts_cache = []
            for element in wd.find_elements_by_css_selector("tr[name='entry']"):
                columns = element.find_elements_by_css_selector("td")
                id = columns[0].find_element_by_name("selected[]").get_attribute("value")
                last_name = columns[1].text
                first_name = columns[2].text
                address = columns[3].text
                email = columns[4].text
                phones = columns[5].text
                self.contacts_cache.append(Contact(first_name = first_name, last_name = last_name, id = id, email = email, phones = phones, address = address))
        return self.contacts_cache
