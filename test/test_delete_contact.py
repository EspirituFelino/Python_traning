import random
from model.contact import Contact

def test_delete_some_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(first_name="test"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    new_contacts = db.get_contact_list()
    old_contacts.remove(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

    # def test_delete_first_contact(app):
    # if app.contact.count() == 0:
    #     app.contact.create(Contact(first_name="test"))
    # old_contacts = app.contact.get_contact_list()
    # app.contact.delete_first_contact()
    # new_contacts = app.contact.get_contact_list()
    # assert len(old_contacts) - 1 == len(new_contacts)
    # old_contacts[0:1] = []
    # assert old_contacts == new_contacts