# -*- coding: utf-8 -*-

from model.group import Group


def test_dom_test(app):
      app.group.create(Group(name="YJdfz uheggf", header="Yjdfz uheggf", footer="YJdfz uheggf"))
      app.session.logout()

def test_dom_empty_test(app):
      app.group.create(Group(name="", header="", footer=""))