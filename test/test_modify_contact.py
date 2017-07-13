from model.contact import Contact
import random

def test_modify_contact_firstname(app,db,check_ui):
    if len (db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    newcontact = Contact(firstname="Julia")
    newcontact.id = contact.id
    newcontact.firstname = contact.firstname
    app.contact.modify_contact_by_id(contact.id,newcontact)
    new_contacts = db.get_contact_list()
    old_contacts.remove(contact)
    old_contacts.append(newcontact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max()) == sorted(app.contact.get_contact_list(),
                                                                   key=Contact.id_or_max())
#

#def test_modify_contact_notes(app):
 #   old_contacts = app.contact.get_contact_list
  #  if app.contact.count() == 0:
   #     app.contact.creation(Contact(firstname="test", middlename="test"))
    #app.contact.modify_first_contact(Contact(middlename="New contact"))
    #new_contacts = app.contact.get_contact_list
    #assert len(old_contacts) == len(new_contacts)
    #app.contact.delete_first_contact()
