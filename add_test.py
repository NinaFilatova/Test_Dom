# -*- coding: utf-8 -*-
import pytest
from  add import Add
from supplement import Supplement


@pytest.fixture
def app(request):
    fixture = Supplement()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_test(app):
    app.login(username="admin", password="secret")
    app.Init_add_creation(Add(firstname="eyuyh", middlename="jknnijmn", lastname="akjkjkkjkj", nickname="asdad",
                               title="Rjhghg", company="kjhjkhksjdf", address="sfdlkjfkjkj",
                               home="sdfsfsd", mobile="sdfsdfsd", work="fsdfffffffffffffffff", fax="fsdfsdfsfds",
                               email="fsdfdsfds", email2="fsdfsdfd", email3="fdsfsdfs", homepage="adfsadf", byear="4323",
                               ayear="rwew", address2="rqwgxdgddgsgsg", phone2="dgsgsdgds", notes="gfdfgfd"))
    app.init_add_creation()
    app.logout()
