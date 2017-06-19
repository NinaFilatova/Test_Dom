from model.contact import Contact

def test_add_test(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="eyuyh", middlename="jknnijmn", lastname="akjkjkkjkj", nickname="asdad",
                      title="Rjhghg", company="kjhjkhksjdf", address="sfdlkjfkjkj",
                      home="sdfsfsd", mobile="sdfsdfsd", work="fsdfffffffffffffffff", fax="fsdfsdfsfds",
                      email="fsdfdsfds", email2="fsdfsdfd", email3="fdsfsdfs", homepage="adfsadf",
                      byear="4323",
                      ayear="rwew", address2="rqwgxdgddgsgsg", phone2="dgsgsdgds", notes="gfdfgfd")
    app.contact.creation(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
