# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest


def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False


class dom_test(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

    def test_dom_test(self):
        wd = self.wd
        self.Open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.Open_groups_page(wd)
        self.create_group(wd, name="YJdfz uheggf",header= "Yjdfz uheggf",footer= "YJdfz uheggf")
        self.return_to_groups_page(wd)
        self.logout(wd)

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def return_to_groups_page(self, wd):
        wd.find_element_by_link_text("group page").click()

    def create_group(self, wd, name, header, footer):
        # init group creation
        wd.find_element_by_name("group_name").click()
        # fill group firm
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(footer)
        # submit group creacion
        wd.find_element_by_name("submit").click()

    def Open_groups_page(self, wd):
        wd.find_element_by_name("new").click()

    def login(self, wd, username, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def Open_home_page(self, wd):
        wd.get("https://localhost/addressbook/addressbook/group.php")

    def tearDown(self):
        self.wd.quit()


if __name__ == '__main__':
    unittest.main()