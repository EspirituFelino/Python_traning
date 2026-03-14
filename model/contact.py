from sys import maxsize


class Contact:

    def __init__(self, first_name=None, middle_name=None, last_name=None, home=None, email=None, company=None, title=None, address=None, id=None, phones=None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.home = home
        self.company = company
        self.title = title
        self.address = address
        self.middle_name = middle_name
        self.phones = phones
        self.id = id

    def __repr__(self):
        return f'{self.id}: {self.first_name} {self.last_name}'

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.first_name == other.first_name and self.last_name == other.last_name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize