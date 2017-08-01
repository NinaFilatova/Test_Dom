from pytest_bdd import scenario
from .contact_steps import *


@scenario('contact.feature', 'Add new contact')
def test_add_new_contact():
    pass


@scenario('contact.feature', 'Delete a contact')
def test_delete_contact():
    pass


@scenario('contact.feature', 'Modify a contact')
def test_modify_contact():
    pass