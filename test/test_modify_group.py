from model.group import Group


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.modify_first_group(Group(name="New group"))
    app.group.delete_first_group()

def test_modify_group_footer(app):
    if app.group.count() == 0:
        app.group.create(Group(footer="test"))
    app.group.modify_first_group(Group(footer="New footer"))
    app.group.delete_first_group()

def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(header="test"))
    app.group.modify_first_group(Group(header="New footer"))
    app.group.delete_first_group()
