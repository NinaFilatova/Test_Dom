from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.creation(Contact(firstname="test", middlename="test", lastname="test", nickname="test",
                                 title="test", company="test", address="test",
                                 home="test", mobile="test", work="test", fax="test",
                                 email="test", email2="test", email3="test", homepage="test", byear="test",
                                 ayear="test", address2="test", phone2="test", notes="test"))
        app.contact.init_add_creation()
    app.contact.delete_first_contact()
