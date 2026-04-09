import random
from model.contact import Contact

def test_edit_some_contact_to_empty(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(first_name="test"))
    old_contacts = db.get_contact_list()
    old_contact = random.choice(old_contacts)
    new_contact = Contact(id=old_contact.id, first_name='FN', middle_name='MN', last_name='LN', homephone='HP', email='EM', company='Cj', title='T', address='AD')
    app.contact.edit_contact_by_id(new_contact, old_contact.id)
    new_contacts = db.get_contact_list()
    old_contacts[old_contacts.index(old_contact)] = new_contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),)

# def test_edit_first_contact(app):
#     if app.contact.count() == 0:
#         app.contact.create(Contact(first_name="test"))
#     app.contact.edit_first_contact(Contact(first_name='LN', last_name="LN", home="HOME", email="EMAIL@"))

