import unittest
from selenium import webdriver
import time


class WizzairWrongEmailInRegistration(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        time.sleep(5)
        self.browser.close()

    def test_registration_wizzair_account(self):
        self.browser.get("https://wizzair.com")
        secondary_variable = self.browser.find_elements_by_class_name("navigation__button.navigation__button--simple")
        working_variable = secondary_variable.__getitem__(0)
        for i in secondary_variable:
            if i.text == "SIGN IN":
                working_variable = i
                break
        working_variable.click()
        secondary_variable = self.browser.find_element_by_class_name("login-form__footer").find_elements_by_class_name("content__link1")
        for i in secondary_variable:
            if i.text == "REGISTRATION":
                working_variable = i
                break
        working_variable.click()
        secondary_variable = self.browser.find_elements_by_name("email")
        working_variable = secondary_variable.pop(1)
        working_variable.clear()
        working_variable.send_keys("sfdasd")
        secondary_variable = self.browser.find_element_by_name("mobilePhone")
        secondary_variable.clear()
        secondary_variable.send_keys("123")
        secondary_variable = self.browser.find_element_by_xpath("//*[.='Invalid e-mail']").text
        assert secondary_variable == "Invalid e-mail"

        time.sleep(5)


if __name__ == "__main__":
    unittest.main()
