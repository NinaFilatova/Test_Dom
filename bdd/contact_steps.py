from pytest_bdd import given, when, then
from model.contact import Contact
import random


@given('a contact list')
def contact_list(db):
    return db.get_contact_list()


@given('a contact with <firstname>, <middlename> , <lastname>, <address>, <email> and <homepage>')
def new_contact(firstname, middlename, lastname, address, email, homepage):
    return Contact(firstname=firstname, middlename=middlename, lastname=lastname, address=address, email=email,
                        homepage=homepage)


@when('I add the contact to the list')
def add_new_contact(app, new_contact):
    app.group.add_new_address_form(new_contact)


@then('the new contact list is equal to the old list with added contact')
def verify_added_contact(db, contact_list, new_contact):
    old_list = contact_list
    new_list = db.get_contact_list()
    old_list.append(new_contact)
    assert sorted(new_list, key=Contact.id_or_max) == sorted(new_list, key=Contact.id_or_max)


@given('a non-empty contact list')
def non_empty_contact_list(app, db):
    if len(db.get_contact_list()) == 0:
        app.group.add_new_address_form(Contact(firstname="for_delete", middlename="for_delete",
                                                    lastname="for_delete", nickname="for_delete",
                                                    company="for_delete", address="for_delete"))
    return db.get_contact_list()


@given('a random contact from the list')
def random_contact(non_empty_contact_list):
    return random.choice(non_empty_contact_list)


@when('I delete the contact from the list')
def delete_contact(app, random_contact):
    app.group.delete_some_contact_by_id(random_contact.id)


@then('the new contact list is equal to the old list without deleted contact')
def verify_deleted_contact(db, non_empty_contact_list, random_contact):
    old_contacts = non_empty_contact_list
    old_contacts.remove(random_contact)
    new__contacts = db.get_contact_list()
    assert old_contacts == new__contacts


@given('a modify data with <firstname>, <middlename> , <lastname>, <address>, <email> and <homepage>')
def modify_data(firstname, middlename, lastname, address, email, homepage):
    return Contact(firstname=firstname, middlename=middlename, lastname=lastname,
                        address=address, email=email, homepage=homepage)


@when('I modify the contact from the list')
def modify_contact(app, random_contact, modify_data):
    #contact = modify_data
    app.contact.modify_some_contact_by_id(modify_data, random_contact.id)


@then('the modified contact list is equal to the old list with modified contact')
def verify_modified_contact(db, non_empty_contact_list, random_contact, modify_data):
    old_list = non_empty_contact_list
    contact = modify_data
    cont = random_contact
    contact.id = cont.id
    old_list.remove(cont)
    old_list.append(contact)
    new_list = db.get_contact_list()
    assert sorted(new_list, key=Contact.id_or_max) == sorted(old_list, key=Contact.id_or_max)