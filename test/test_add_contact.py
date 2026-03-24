# -*- coding: utf-8 -*-
import pytest
from fixture.application import random_string
from model.contact import Contact

test_data=[
    Contact(first_name=first_name, middle_name=middle_name, last_name=last_name,
            nickname=nickname, title=title, company=company, address=address,
            homephone=homephone, mobilephone=mobilephone, workphone=workphone,
            email=email, email2=email2, email3=email3, homepage=homepage)
    for first_name in ["", random_string('first name', 10)]
    for middle_name in [random_string('middle name', 10)]
    for last_name in ["", random_string('last name', 10)]
    for nickname in [random_string('nickname', 10)]
    for title in [random_string('title', 10)]
    for company in [random_string('company', 10)]
    for address in ["", random_string('address', 10)]
    for homephone in ["", random_string('home phone', 10)]
    for mobilephone in [random_string('mobilephone', 10)]
    for workphone in [random_string('workphone', 10)]
    for email in [random_string('email', 10)]
    for email2 in [random_string('email2', 10)]
    for email3 in [random_string('email3', 10)]
    for homepage in [random_string('homepage', 10)]
]

@pytest.mark.parametrize("contact", test_data, ids=[repr(x) for x in test_data])

def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)