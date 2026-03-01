# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application
from model.contact import Contact

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
    app.session.login("admin", "secret")
    app.create_contact(Contact(first_name='1', last_name="sdtgvbd", home="24532462456", email="fdger5ty4wt2@"))
    app.session.logout()