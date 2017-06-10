from model.contact import Contact


def test_modify_contact_firstname(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(firstname="New contact"))
    app.session.logout()

def test_modify_contact_middlename(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(middlename="New contact"))
    app.session.logout()

def test_modify_contact_lastname(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(lastname="New contact"))
    app.session.logout()

def test_modify_contact_nickname(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(nickname="New contact"))
    app.session.logout()

def test_modify_contact_title(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(title="New contact"))
    app.session.logout()

def test_modify_contact_company(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(company="New contact"))
    app.session.logout()

def test_modify_contact_address(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(address="New contact"))
    app.session.logout()

def test_modify_contact_home(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(home="New contact"))
    app.session.logout()

def test_modify_contact_mobile(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(mobile="New contact"))
    app.session.logout()

def test_modify_contact_work(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(work="New contact"))
    app.session.logout()

def test_modify_contact_fax(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(fax="New contact"))
    app.session.logout()

def test_modify_contact_email(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(email="New contact"))
    app.session.logout()


def test_modify_contact_email2(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(email2="New contact"))
    app.session.logout()

def test_modify_contact_email3(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(email3="New contact"))
    app.session.logout()

def test_modify_contact_homepage(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(homepage="New contact"))
    app.session.logout()

def test_modify_contact_byear(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(byear="New contact"))
    app.session.logout()

def test_modify_contact_ayear(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(ayear="New contact"))
    app.session.logout()

def test_modify_contact_address2(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(address2="New contact"))
    app.session.logout()

def test_modify_contact_phone2(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(phone2="New contact"))
    app.session.logout()

def test_modify_contact_notes(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(notes="New contact"))
    app.session.logout()