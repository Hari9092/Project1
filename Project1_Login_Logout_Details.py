from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert



class OrangeHRM:

    def __init__(self, driver):
        self.driver = driver

    input_locator_username = "username"
    input_locator_password = "password"
    click_locator_button = '//button[text()=" Login "]'
    title_locator_text = "//h6[text()='Dashboard']"
    title_page_locator = '//p[@class="oxd-userdropdown-name"]/following-sibling::i'
    pim_emp_title = "//h6[text()='HariPrasath C']"
    click_logout_locator = '//a[text()="Logout"]'
    text_invalid = '//P[text()="Invalid credentials"]'
    add_employee = '//span[text()="PIM"]'
    button_add = '//button[text()=" Add "]//following-sibling::i'
    input_firstName = 'firstName'
    input_lastName = 'lastName'
    button_save = '//button[@type="submit"]'
    employee_Title = '//h6[text()="Hari Prasath"]'
    gender_button = '//input[@value="1"]//following-sibling::span'
    element_Nationality = "document.getElementsByClassName('oxd-select-text-input')[0].innerText='Indian'"
    element_Mar_status = "document.getElementsByClassName('oxd-select-text-input')[1].innerText='Single'"
    element_mili_service = "//div[@class='oxd-form-row']/following::div[73]/input[@class='oxd-input oxd-input--active']"
    element_smoker = "//label[text()='Yes']"
    element_DOB = "//div[@class='oxd-select-wrapper']/following::input[1]"
    element_Submit1 = '//p[text()=" * Required"]//following-sibling::button'
    element_bloodType = "document.getElementsByClassName('oxd-select-text-input')[2].innerText='A+'"
    element_submit2 = "//form/div[2]/button"
    element_emp_find = "//form/div[1]/div/div[1]/div/div[2]/div/div/input"
    element_search= "//button[text()=' Search ']"
    element_firstName = "//div[text()='HariPrasath ']"
    element_trash_button = "//i[@class='oxd-icon bi-trash']"
    element_alert = "//i[@class='oxd-icon bi-trash oxd-button-icon']/parent::button"

    def login_page_username(self, username):
        self.driver.find_element(By.NAME, self.input_locator_username).send_keys(username)

    def login_page_password(self, password):
        self.driver.find_element(By.NAME, self.input_locator_password).send_keys(password)

    def login_page_submit(self):
        self.driver.find_element(By.XPATH, self.click_locator_button).click()

    def logout_page(self):
        self.driver.find_element(By.XPATH, self.title_page_locator).click()
        self.driver.find_element(By.XPATH, self.click_logout_locator).click()

    def title_page_text(self):
        title = WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located
                                                     ((By.XPATH, self.title_locator_text)))
        return title

    def pim_emp_element(self):
        title1 = WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located
                                                      ((By.XPATH, self.pim_emp_title)))
        return title1

    def invalid_cred(self):
        invalid_text = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located
                                                            ((By.XPATH, self.text_invalid)))
        return invalid_text

    def add_employee_list(self):
        self.driver.find_element(By.XPATH, self.add_employee).click()
        self.driver.find_element(By.XPATH, self.button_add).click()

    def employe_firstName(self, firstname):
        self.driver.find_element(By.NAME, self.input_firstName).send_keys(firstname)

    def employee_lastName(self, lastname):
        self.driver.implicitly_wait(50)
        self.driver.find_element(By.NAME, self.input_lastName).send_keys(lastname)
        self.driver.find_element(By.XPATH, self.button_save).click()

    def employee_name_verify(self):
        emp_title_name = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.employee_Title)))
        return emp_title_name

    def employee_search(self,firstname):
        self.driver.find_element(By.XPATH,self.add_employee).click()
        self.driver.find_element(By.XPATH,self.element_emp_find).send_keys(firstname)
        self.driver.find_element(By.XPATH,self.element_search).click()
        self.driver.find_element(By.XPATH,self.element_firstName).click()

    def nationality(self):
        self.driver.execute_script(self.element_Nationality)

    def martial_status(self):
        self.driver.execute_script(self.element_Mar_status)


    def select_DOB(self):
        self.driver.find_element(By.XPATH, self.element_DOB).send_keys('1992-09-16')

    def gender_selection(self):
        self.driver.find_element(By.XPATH, self.gender_button).click()
        self.driver.implicitly_wait(50)

    def check_box_smoker(self):
        self.driver.find_element(By.XPATH, self.element_mili_service).send_keys("Not")
        self.driver.find_element(By.XPATH, self.element_smoker).click()
        self.driver.find_element(By.XPATH, self.element_Submit1).click()

    def blood_group(self):
        self.driver.execute_script(self.element_bloodType)
        self.driver.find_element(By.XPATH,self.element_submit2).click()

    def delete_user(self):
        self.driver.find_element(By.XPATH, self.add_employee).click()
        self.driver.find_element(By.XPATH, self.element_emp_find).send_keys("Hari Prasath")
        self.driver.find_element(By.XPATH, self.element_search).click()

        self.driver.find_element(By.XPATH,self.element_trash_button).click()

        self.driver.find_element(By.XPATH,self.element_alert).click()

