import random
from model.contact import Contact
from model.group import Group


def test_delete_contact_from_group(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test"))
    if len(db.get_contacts_with_groups()) == 0:
        contact = random.choice(db.get_contact_list())
        group = random.choice(db.get_group_list())
        app.contact.add_contact_in_group(contact, group)
    else:
        contact = random.choice(db.get_contacts_with_groups())
        group = random.choice(contact.groups)
    app.contact.delete_contact_from_group(contact, group)
    assert contact not in db.get_contacts_in_group(group)
