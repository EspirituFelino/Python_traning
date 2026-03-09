from model.contact import Contact

def test_edit_first_contact_to_empty(app):
    app.contact.edit_first_contact(Contact(first_name='', middle_name='', last_name='', home='', email='', company='', title='', address=''))

def test_edit_first_contact(app):
    app.contact.edit_first_contact(Contact(first_name='LN', last_name="LN", home="HOME", email="EMAIL@"))

