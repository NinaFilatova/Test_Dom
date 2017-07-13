from model.group import Group
import random

def test_modify_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    newgroup = Group(name="New group")
    newgroup.id = group.id
    app.group.modify_group_by_id(group.id, newgroup)
    assert len(old_groups) == app.group.count()
    new_groups = db.get_group_list()
    old_groups.remove(group)
    old_groups.append(newgroup)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max()) == sorted(app.group.get_group_list(),
                                                                       key=Group.id_or_max())

#def test_modify_group_footer(app):
 #   if app.group.count() == 0:
  #      app.group.create(Group(footer="test"))
   # old_groups = app.group.get_group_list()
    #app.group.modify_first_group(Group(footer="New footer"))
    #new_groups = app.group.get_group_list()
    #assert len(old_groups) == len(new_groups)
    #app.group.delete_first_group()

#def test_modify_group_header(app):
 #   if app.group.count() == 0:
  #      app.group.create(Group(header="test"))
   # old_groups = app.group.get_group_list()
    #app.group.modify_first_group(Group(header="New header"))
    #new_groups = app.group.get_group_list()
    #assert len(old_groups) == len(new_groups)
    #app.group.delete_first_group()
