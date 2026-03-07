from model.contact import Contact

def test_edit_first_contact_to_empty(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(first_name='', middle_name='', last_name='', home='', email='', company='', title='', address=''))
    app.session.logout()

def test_edit_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(first_name='LN', last_name="LN", home="HOME", email="EMAIL@"))
    app.session.logout()

