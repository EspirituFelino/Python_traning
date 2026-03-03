# -*- coding: utf-8 -*-
from model.group import Group


def test_edit_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name="NAME1", header="HEADER2", footer="FOOTER3"))
    app.session.logout()

def test_edit_first_group_to_empty(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name="", header="", footer=""))
    app.session.logout()