from random import randrange
from model.contact import Contact

def test_edit_some_contact_to_empty(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="test"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(first_name='', middle_name='', last_name='', home='', email='', company='', title='', address='')
    index = randrange(len(old_contacts))
    contact.id = old_contacts[index].id
    app.contact.edit_contact_by_index(contact, index)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

# def test_edit_first_contact(app):
#     if app.contact.count() == 0:
#         app.contact.create(Contact(first_name="test"))
#     app.contact.edit_first_contact(Contact(first_name='LN', last_name="LN", home="HOME", email="EMAIL@"))

