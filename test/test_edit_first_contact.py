from model.contact import Contact

def test_edit_first_contact_to_empty(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact())
    app.session.logout()

def test_edit_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(company='FN', title="LN", address="HOME"))
    app.session.logout()

