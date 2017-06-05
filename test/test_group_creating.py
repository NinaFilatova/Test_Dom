# -*- coding: utf-8 -*-

from model.group import Group


def test_dom_test(app):
      app.session.login(username="admin", password="secret")
      app.group.create(Group(name="YJdfz uheggf", header="Yjdfz uheggf", footer="YJdfz uheggf"))
      app.session.logout()

