from model.contact import Contact

class ContactHelper:
    def __init__(self, app):
        self.app = app

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        # open_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/index.php")):
            wd.get("https://localhost/addressbook/addressbook/index.php")
        self.select_contact_by_index(index)
        # submit deletion
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def modify_first_contact(self, new_contact_data):
        self.modify_contact_by_index(0)

    def modify_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.select_contact_by_index(index)
        # open modification form
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        # fill add form
        self.fill_add_form(new_contact_data)
        # submit modification
        wd.find_element_by_name("update").click()
        self.contact_cache = None

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
        self.contact_cache = None

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

    contact_cache = None

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        if not (wd.current_url.endswith("/index.php")):
            wd.get("https://localhost/addressbook/addressbook/index.php")
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        if not (wd.current_url.endswith("/index.php")):
            wd.get("https://localhost/addressbook/addressbook/index.php")
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            if not (wd.current_url.endswith("/index.php")):
                wd.get("https://localhost/addressbook/addressbook/index.php")
            self.contact_cache = []
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                firstname = cells[1].text
                lastname = cells[2].text
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                all_phones = cells[5].text.splitlines()
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=id,
                                                  home=all_phones[0], mobile=all_phones[1],work=all_phones[2],
                                                  phone2=all_phones[3]))
        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        home = wd.find_element_by_name("home").get_attribute("value")
        work = wd.find_element_by_name("work").get_attribute("value")
        mobile = wd.find_element_by_name("mobile").get_attribute("value")
        phone2 = wd.find_element_by_name("phone2").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id, home=home,
                       work=work, mobile=mobile, phone2=phone2)
