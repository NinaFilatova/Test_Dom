# -*- coding: utf-8 -*-

from model.group import Group

def test_dom_test(app):
      old_groups = app.group.get_group_list
      app.group.create(Group(name="YJdfz uheggf", header="Yjdfz uheggf", footer="YJdfz uheggf"))
      new_groups = app.group.get_group_list
      assert len(old_groups) + 1 == len(new_groups)


def test_dom_empty_test(app):
      old_groups = app.group.get_group_list
      app.group.create(Group(name="", header="", footer=""))
      new_groups = app.group.get_group_list
      assert len(old_groups) + 1 == len(new_groups)