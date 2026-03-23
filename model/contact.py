import re
from sys import maxsize


class Contact:

    def __init__(self, first_name=None, middle_name=None, last_name=None, homephone=None,
                 email=None, email2=None, email3=None, company=None, title=None, address=None, id=None, phones=None,
                 workphone=None, mobilephone=None, secondaryphone=None,
                 all_phones_from_homepage=None, all_emails_from_homepage=None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homephone = homephone
        self.company = company
        self.title = title
        self.address = address
        self.middle_name = middle_name
        self.phones = phones
        self.id = id
        self.workphone = workphone
        self.mobilephone = mobilephone
        self.secondaryphone = secondaryphone
        self.all_phones_from_homepage = all_phones_from_homepage
        self.all_emails_from_homepage = all_emails_from_homepage


    def __repr__(self):
        return f'{self.id}: {self.first_name} {self.last_name}'

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.first_name == other.first_name and self.last_name == other.last_name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
    def clear_like_homepage(self,s):
        return re.sub("[() -]", "", s)

    def merge_phones_like_homepage(self):
        return "\n".join(filter(lambda x: x != '',
                                map(lambda x: self.clear_like_homepage(x),
                                    filter(lambda x: x is not None,
                                           [self.homephone, self.mobilephone, self.workphone, self.secondaryphone]))))

    def merge_emails_like_homepage(self):
        return "\n".join(filter(lambda x: x != '',
                                    filter(lambda x: x is not None,
                                           [self.email, self.email2, self.email3])))
