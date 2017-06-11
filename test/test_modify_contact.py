from model.contact import Contact

def test_modify_contact_firstname(app):
    app.contact.modify_first_contact(Contact(firstname="New contact"))

def test_modify_contact_middlename(app):
    app.contact.modify_first_contact(Contact(middlename="New contact"))

def test_modify_contact_lastname(app):
    app.contact.modify_first_contact(Contact(lastname="New contact"))

def test_modify_contact_nickname(app):
    app.contact.modify_first_contact(Contact(nickname="New contact"))

def test_modify_contact_title(app):
    app.contact.modify_first_contact(Contact(title="New contact"))

def test_modify_contact_company(app):
    app.contact.modify_first_contact(Contact(company="New contact"))

def test_modify_contact_address(app):
    app.contact.modify_first_contact(Contact(address="New contact"))

def test_modify_contact_home(app):
    app.contact.modify_first_contact(Contact(home="New contact"))

def test_modify_contact_mobile(app):
    app.contact.modify_first_contact(Contact(mobile="New contact"))

def test_modify_contact_work(app):
    app.contact.modify_first_contact(Contact(work="New contact"))

def test_modify_contact_fax(app):
    app.contact.modify_first_contact(Contact(fax="New contact"))

def test_modify_contact_email(app):
    app.contact.modify_first_contact(Contact(email="New contact"))

def test_modify_contact_email2(app):
    app.contact.modify_first_contact(Contact(email2="New contact"))

def test_modify_contact_email3(app):
    app.contact.modify_first_contact(Contact(email3="New contact"))

def test_modify_contact_homepage(app):
    app.contact.modify_first_contact(Contact(homepage="New contact"))

def test_modify_contact_byear(app):
    app.contact.modify_first_contact(Contact(byear="New contact"))

def test_modify_contact_ayear(app):
    app.contact.modify_first_contact(Contact(ayear="New contact"))

def test_modify_contact_address2(app):
    app.contact.modify_first_contact(Contact(address2="New contact"))

def test_modify_contact_phone2(app):
    app.contact.modify_first_contact(Contact(phone2="New contact"))

def test_modify_contact_notes(app):
    app.contact.modify_first_contact(Contact(notes="New contact"))
