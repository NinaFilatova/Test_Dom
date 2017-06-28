from model.contact import Contact
import pytest
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.digits + " " *10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Contact(firstname="", lastname="", home="", mobile="", email="", address2="")] + [
    Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 10), lastname=random_string("lastname", 10),
                    nickname=random_string("nickname", 10), company=random_string("company", 10),
                    address=random_string("address", 10), home=random_string("home", 10),
                    mobile=random_string("mobile", 10), work=random_string("work", 10),
                    fax=random_string("fax", 10), email=random_string("email", 10), email2=random_string("email2", 10),
                    email3=random_string("email3", 10), address2=random_string("address2", 10),
                    notes=random_string("notes", 10), homepage=random_string("homepage", 10), phone2=random_string("phone2", 10))
    for i in range(5)
]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_test(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.creation(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
