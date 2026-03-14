from model.contact import Contact

def test_edit_first_contact_to_empty(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="test"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(first_name='', middle_name='', last_name='', home='', email='', company='', title='', address='')
    contact.id = old_contacts[0].id
    app.contact.edit_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

# def test_edit_first_contact(app):
#     if app.contact.count() == 0:
#         app.contact.create(Contact(first_name="test"))
#     app.contact.edit_first_contact(Contact(first_name='LN', last_name="LN", home="HOME", email="EMAIL@"))

