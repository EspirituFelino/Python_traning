import re

from model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.app.change_field_value("firstname", contact.first_name)
        self.app.change_field_value("middlename", contact.middle_name)
        self.app.change_field_value("lastname", contact.last_name)
        self.app.change_field_value("nickname", contact.nickname)
        self.app.change_field_value("title", contact.title)
        self.app.change_field_value("company", contact.company)
        self.app.change_field_value("address", contact.address)
        self.app.change_field_value("home", contact.homephone)
        self.app.change_field_value("mobile", contact.mobilephone)
        self.app.change_field_value("work", contact.workphone)
        self.app.change_field_value("email", contact.email)
        self.app.change_field_value("email2", contact.email2)
        self.app.change_field_value("email3", contact.email3)
        self.app.change_field_value("homepage", contact.homepage)


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
                emails = columns[4].text
                phones = columns[5].text
                self.contacts_cache.append(Contact(first_name = first_name, last_name = last_name,
                                                   id = id, all_emails_from_homepage = emails,
                                                   all_phones_from_homepage = phones,
                                                   address = address))
        return self.contacts_cache

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.app.return_home_page()
        self.init_edit_contact_by_index(index)
        first_name = wd.find_element_by_name("firstname").get_attribute("value")
        last_name = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        # secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        return Contact(first_name=first_name, last_name=last_name, id=id,
                       homephone=homephone, workphone=workphone, mobilephone=mobilephone,
                       address=address, email=email, email2=email2, email3=email3)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.app.return_home_page()
        self.open_contact_page_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        return Contact(homephone=homephone, workphone=workphone, mobilephone=mobilephone)

    def open_contact_page_by_index(self, index):
        wd = self.app.wd
        self.app.return_home_page()
        wd.find_elements_by_xpath("//img[@alt='Details']")[index].click()
