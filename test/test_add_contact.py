# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.session.login("admin", "secret")
    app.contact.create(Contact(first_name='1', last_name="sdtgvbd", home="24532462456", email="fdger5ty4wt2@"))
    app.session.logout()