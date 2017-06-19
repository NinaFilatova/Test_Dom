from model.contact import Contact

def test_modify_contact_middlename(app):
    old_contacts = app.contact.get_contact_list()
    if app.contact.count() == 0:
        app.contact.creation(Contact(firstname="test", middlename="test"))
    contact = Contact(middlename="New contact")
    contact.id = old_contacts[0].id
    app.contact.modify_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    app.contact.delete_first_contact()

#def test_modify_contact_notes(app):
 #   old_contacts = app.contact.get_contact_list
  #  if app.contact.count() == 0:
   #     app.contact.creation(Contact(firstname="test", middlename="test"))
    #app.contact.modify_first_contact(Contact(middlename="New contact"))
    #new_contacts = app.contact.get_contact_list
    #assert len(old_contacts) == len(new_contacts)
    #app.contact.delete_first_contact()
