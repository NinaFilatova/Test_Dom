from model.contact import Contact
from random import randrange

def test_modify_contact_lastname(app):
    old_contacts = app.contact.get_contact_list()
    if app.contact.count() == 0:
        app.contact.creation(Contact(firstname="test", lastname="test"))
    index = randrange(len(old_contacts))
    contact = Contact(lastname="New contact")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
#

#def test_modify_contact_notes(app):
 #   old_contacts = app.contact.get_contact_list
  #  if app.contact.count() == 0:
   #     app.contact.creation(Contact(firstname="test", middlename="test"))
    #app.contact.modify_first_contact(Contact(middlename="New contact"))
    #new_contacts = app.contact.get_contact_list
    #assert len(old_contacts) == len(new_contacts)
    #app.contact.delete_first_contact()
