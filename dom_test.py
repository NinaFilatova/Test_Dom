# -*- coding: utf-8 -*-

import pytest
from group import Group
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_dom_test(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="YJdfz uheggf", header="Yjdfz uheggf", footer="YJdfz uheggf"))
    app.logout()

