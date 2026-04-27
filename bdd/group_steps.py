import random

from pytest_bdd import given, when, then, parsers

from model.group import Group


@given(parsers.parse("a group list"), target_fixture="group_list")
def group_list(db):
    return db.get_group_list()

@given(parsers.parse("a group with {name}, {header}, {footer}"), target_fixture="new_group")
def new_group(name, header, footer):
    return Group(name=name, header=header, footer=footer)


@when(parsers.parse("I add the group to the list"))
def add_new_group(app, new_group):
    app.group.create(new_group)

@then(parsers.parse("the new group list is equal to the old list with the added group"))
def verify_group_list(group_list, new_group, db):
    old_groups = group_list
    new_groups = db.get_group_list()
    old_groups.append(new_group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

@given(parsers.parse("a non-empty group list"), target_fixture="non_empty_group_list")
def non_empty_group_list(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test", header="test", footer="test"))
    return db.get_group_list()

@given(parsers.parse("a random group from the list"), target_fixture="random_group")
def random_group(non_empty_group_list):
    return random.choice(non_empty_group_list)

@when(parsers.parse('I delete the group from the list'))
def delete_group(app, random_group):
    app.group.delete_group_by_id(random_group.id)

@then(parsers.parse('the new group list is equal old group list without the deleted group'))
def verify_group_list_after_delete(app, db, check_ui, non_empty_group_list, random_group):
    old_groups = non_empty_group_list
    new_groups = db.get_group_list()
    old_groups.remove(random_group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


