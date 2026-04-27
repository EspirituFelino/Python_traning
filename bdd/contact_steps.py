import random

from pytest_bdd import given, when, then, parsers

from model.contact import Contact


@given(parsers.parse('a contact list'), target_fixture='contact_list')
def contact_list(db):
    return db.get_contact_list()

@given(parsers.parse('a contact with {first_name}, {last_name}, {workphone}, {email}, {address}'),
       target_fixture='new_contact')
def new_contact(first_name, last_name, workphone, email, address):
    return Contact(first_name=first_name, last_name=last_name, workphone=workphone,
                   email=email, address=address)

@given(parsers.parse('a non-empty contact list'), target_fixture='non_empty_contact_list')
def non_empty_contact_list(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(first_name="Burn", last_name="After", address='Read'))
    return db.get_contact_list()

@given(parsers.parse('a random contact from the list'), target_fixture='random_contact')
def random_contact(non_empty_contact_list):
    return random.choice(non_empty_contact_list)

@when(parsers.parse('I add the contact to the list'))
def add_contact(new_contact, app):
    app.contact.create(new_contact)

@when(parsers.parse('I delete the contact from the list'))
def delete_contact(app, random_contact):
    app.contact.delete_contact_by_id(random_contact.id)

@when(parsers.parse('I modify random contact with the contacts attributes'))
def modify_contact(new_contact, random_contact, app):
    app.contact.edit_contact_by_id(contact=new_contact, id=random_contact.id)

@then(parsers.parse('the new contact list is equal to the old contact list with the added contact'))
def verify_contact_list(new_contact, contact_list, db, app, check_ui):
    old_contacts = contact_list
    new_contacts = db.get_contact_list()
    old_contacts.append(new_contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)

@then(parsers.parse('the new contact list is equal old contact list without deleted contact'))
def verify_contact_list_after_delete(non_empty_contact_list, random_contact,
                                     app, db, check_ui):
    old_contacts = non_empty_contact_list
    new_contacts = db.get_contact_list()
    old_contacts.remove(random_contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)


@then(parsers.parse('the new contact list is equal to the old contact list with replaced contact'))
def verify_contact_list_after_modify(non_empty_contact_list, random_contact,
                                     new_contact, app, db, check_ui):
    old_contacts = non_empty_contact_list
    new_contacts = db.get_contact_list()
    new_contact.id = random_contact.id
    old_contacts[old_contacts.index(random_contact)] = new_contact
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
