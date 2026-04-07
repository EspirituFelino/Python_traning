from model.group import Group


def test_group_list_equal(app, db):
    web_list = app.group.get_group_list()
    def clean(group):
        return Group(id=group.id, name=group.name.strip())
    db_list = map(clean, db.get_group_list())
    assert sorted(web_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)