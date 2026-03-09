# -*- coding: utf-8 -*-
from model.group import Group


def test_edit_first_group_name(app):
    app.group.edit_first_group(Group(name="New group"))

def test_edit_first_group(app):
    app.group.edit_first_group(Group(name="NAME1", header="HEADER2", footer="FOOTER3"))

def test_edit_first_group_header(app):
    app.group.edit_first_group(Group(header="NG"))

def test_edit_first_group_to_empty(app):
    app.group.edit_first_group(Group(name="", header="", footer=""))
