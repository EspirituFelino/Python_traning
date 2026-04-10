from random import randrange
from model.contact import Contact


def test_contact_info_from_home_page(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(first_name='Test', last_name='Test'))
    contacts_from_home_page = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    contacts_from_db = sorted(db.get_contact_list(), key=Contact.id_or_max)
    for i in range(len(contacts_from_home_page)):
        assert contacts_from_home_page[i].first_name == contacts_from_db[i].first_name
        assert contacts_from_home_page[i].last_name == contacts_from_db[i].last_name
        assert contacts_from_home_page[i].address == contacts_from_db[i].address_like_homepage()
        assert contacts_from_home_page[i].all_phones_from_homepage == contacts_from_db[i].merge_phones_like_homepage()
        assert contacts_from_home_page[i].all_emails_from_homepage == contacts_from_db[i].merge_emails_like_homepage()
