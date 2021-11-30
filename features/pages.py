class BasePage(object):
    def __init__(self, browser):
        self.browser = browser

class RegistrationPage(BasePage):
    def open(self):
        self.browser.get('http://localhost:8080/auth/register')

    def register(self, username, password):
        self.browser.find_element_by_id('username').send_keys(username)
        self.browser.find_element_by_id('password').send_keys(password)
        self.browser.find_element_by_css_selector('form').submit()

class LoginPage(BasePage):
    def open(self):
        self.browser.get('http://localhost:8080/auth/login')

    def login(self, username, password):
        self.browser.find_element_by_id('username').send_keys(username)
        self.browser.find_element_by_id('password').send_keys(password)
        self.browser.find_element_by_css_selector('form').submit()

class PostsPage(BasePage):
    @property
    def username_logged_in(self):
        return self.browser.find_element_by_css_selector('nav ul li:first-child span').text
