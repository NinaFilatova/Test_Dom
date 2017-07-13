from model.contact import Contact
from model.group import Group
import random


def test_add_contact_to_group(app, db, orm):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="fsff", middlename="fsf", lastname="fsdf", nickname="sdff", title="dsfdsf",
                                   company="fsfdfdf",
                                   address="4242", home="3424", mobile="2344", work="4234",
                                   fax="43244", email="434234", email2="3424", email3="4234", homepage="423424",
                                   byear="1199",
                                   ayear="2423", address2="324eeee", phone2="324rew",
                                   notes="324erwsd"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="new_name", header="new_header", footer="new_footer"))
    old_contacts = db.get_contact_list()
    groups = db.get_group_list()
    contact = random.choice(old_contacts)
    group = random.choice(groups)
    if contact in orm.get_contacts_in_group(group):
        app.contact.delete_contact_from_group(contact.id, group.id)
    app.contact.add_contact_to_group(contact.id, group.id)
    assert contact in orm.get_contacts_in_group(group)
    assert contact not in orm.get_contacts_not_in_group(group)