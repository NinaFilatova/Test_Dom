from model.contact import Contact

def test_add_test(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="eyuyh", lastname="jknnijmn")
    app.contact.creation(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
