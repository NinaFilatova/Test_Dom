import pytest

from fixture.supplement import Supplement
from model.contact import Contact
@pytest.fixture

def app(request):
    fixture = Supplement()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_delete_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.delete_first_contact()
    app.session.logout()
