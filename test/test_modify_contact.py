from model.contact import Contact

def test_modify_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.creation(Contact(firstname="test", middlename="test", lastname="test", nickname="test",
                                 title="test", company="test", address="test",
                                 home="test", mobile="test", work="test", fax="test",
                                 email="test", email2="test", email3="test", homepage="test", byear="test",
                                 ayear="test", address2="test", phone2="test", notes="test"))
        app.contact.init_add_creation()
    app.contact.modify_first_contact(Contact(firstname="New contact"))
    app.contact.delete_first_contact()

def test_modify_contact_notes(app):
    if app.contact.count() == 0:
        app.contact.creation(Contact(firstname="test", middlename="test", lastname="test", nickname="test",
                                     title="test", company="test", address="test",
                                     home="test", mobile="test", work="test", fax="test",
                                     email="test", email2="test", email3="test", homepage="test", byear="test",
                                     ayear="test", address2="test", phone2="test", notes="test"))
        app.contact.init_add_creation()
    app.contact.modify_first_contact(Contact(notes="New contact"))
