from model.contact import Contact

def test_add_test(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Ivan", middlename="O", lastname="Ivanov", nickname="hhhh",
                    company="Nike", address="oo gg", home="1111111", mobile="890909090909",
                   work="", fax="", email="ggggg@mail.com", email2="2ggggg@mail.com",
                    email3="3ggggg@mail.com", address2="gg oo", notes="",
                     homepage="", phone2="")
    app.contact.creation(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
