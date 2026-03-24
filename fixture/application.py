import random
import string
from selenium import webdriver
from fixture.contact import ContactHelper
from fixture.group import GroupHelper
from fixture.session import SessionHelper


class Application:
    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(0.3)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def destroy(self):
        self.wd.quit()

    def return_home_page(self):
        if not self.wd.current_url == "http://localhost/addressbook/":
            self.wd.find_element_by_link_text("home").click()

    def open_home_page(self):
        if not self.wd.current_url == "http://localhost/addressbook/":
            self.wd.get("http://localhost/addressbook/")

    def change_field_value(self, field_name, text):
        wd = self.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + ''.join([random.choice(symbols) for i in range(random.randrange(maxlen))])