from model.contact import Contact
class ContactHelper:

    def __init__(self, app):
        self.app = app

    def delete_first_contact(self):
        # open_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/index.php")):
            wd.get("https://localhost/addressbook/addressbook/index.php")
        self.select_first_contact()
        # submit deletion
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.select_first_contact()
        # open modification form
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        # fill add form
        self.fill_add_form(new_contact_data)
        # submit modification
        wd.find_element_by_name("update").click()

    def creation(self, add):
        wd = self.app.wd
        # init add creation
        wd.find_element_by_link_text("add new").click()
        self.fill_add_form(add)

    def fill_add_form(self, add):
        wd = self.app.wd
        self.change_field_value("firstname", add.firstname)
        self.change_field_value("middlename", add.middlename)
        self.change_field_value("lastname", add.lastname)
        self.change_field_value("nickname", add.nickname)
        self.change_field_value("title", add.title)
        self.change_field_value("company", add.company)
        self.change_field_value("address", add.address)
        self.change_field_value("home", add.home)
        self.change_field_value("mobile", add.mobile)
        self.change_field_value("work", add.work)
        self.change_field_value("fax", add.fax)
        self.change_field_value("email", add.email)
        self.change_field_value("email2", add.email2)
        self.change_field_value("email3", add.email3)
        self.change_field_value("homepage", add.homepage)
        self.change_field_value("byear", add.byear)
        self.change_field_value("address2", add.address2)
        self.change_field_value("phone2", add.phone2)
        self.change_field_value("ayear", add.ayear)
        self.change_field_value("notes", add.notes)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def count(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/index.php")):
            wd.get("https://localhost/addressbook/addressbook/index.php")
        return len(wd.find_elements_by_name("selected[]"))

    def get_contact_list(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/index.php")):
            wd.get("https://localhost/addressbook/addressbook/index.php")
        contacts = []
        for element in wd.find_elements_by_name("entry"):
            text = element.text
            cells = element.find_elements_by_tag_name("td")
            id = element.find_element_by_name("selected[]").get_attribute("value")
            contacts.append(Contact(firstname=cells[2].text, lastname=cells[1].text, id=id))
        return contacts




