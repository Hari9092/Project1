import json
import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from Project1_Login_Logout_Details import OrangeHRM


class HRMLogin(unittest.TestCase):

    driver = None
    data_list = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = Options()
        cls.driver.add_argument("--start-maximized")
        cls.driver=webdriver.Chrome(options=cls.driver)
        cls.driver.implicitly_wait(50)
        cls.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        json_path = "C:\\Users\\harip\\PycharmProjects\\pythonProject\\DataSource\\Project1_testdata.json"
        with open(json_path) as jsonfile:
            cls.data_list = json.load(jsonfile)

    @classmethod
    def tearDownClass(cls) -> None:
        print("after all test")



    def test_TC_Login_01(self):
        login_page = OrangeHRM(self.driver)
        login_page.login_page_username(self.data_list.get("login_data").get("user_name"))
        login_page.login_page_password(self.data_list.get("login_data").get("password"))
        login_page.login_page_submit()
        assert login_page.title_page_text()
        login_page.logout_page()

    def test_TC_Login_02(self):
        login_page = OrangeHRM(self.driver)
        login_page.login_page_username(self.data_list.get("login_data").get("user_name"))
        login_page.login_page_password(self.data_list.get("login_data").get("wrong_password"))
        login_page.login_page_submit()
        assert login_page.invalid_cred()

    def test_TC_PIM_01(self):
        login_page = OrangeHRM(self.driver)
        login_page.login_page_username(self.data_list.get("login_data").get("user_name"))
        login_page.login_page_password(self.data_list.get("login_data").get("password"))
        login_page.login_page_submit()
        login_page.add_employee_list()
        login_page.employe_firstName(self.data_list.get("login_data").get("firstname"))
        login_page.employee_lastName(self.data_list.get("login_data").get("lastname"))
        assert login_page.pim_emp_element()


    def test_TC_PIM_02(self):
        login_page = OrangeHRM(self.driver)
        login_page.login_page_username(self.data_list.get("login_data").get("user_name"))
        login_page.login_page_password(self.data_list.get("login_data").get("password"))
        login_page.login_page_submit()
        login_page.employee_search(self.data_list.get("login_data").get("firstname"))
        assert login_page.pim_emp_element()
        login_page.nationality()
        login_page.martial_status()
        login_page.select_DOB()
        login_page.gender_selection()
        login_page.check_box_smoker()
        login_page.blood_group()
        assert login_page.pim_emp_element()


    def test_TC_PIM_03(self):
        login_page = OrangeHRM(self.driver)
        login_page.login_page_username(self.data_list.get("login_data").get("user_name"))
        login_page.login_page_password(self.data_list.get("login_data").get("password"))
        login_page.login_page_submit()
        login_page.delete_user()
















