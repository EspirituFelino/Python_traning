import random
from model.contact import Contact
from model.group import Group


def test_add_contact_in_group(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    group = random.choice(db.get_group_list())
    if len(db.get_contacts_not_in_group(group)) == 0:
        app.contact.create(Contact(first_name="test"))
    contact = random.choice(db.get_contacts_not_in_group(group))
    app.contact.add_contact_in_group(contact, group)
    assert contact in db.get_contacts_in_group(group)
