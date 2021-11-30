from selenium import webdriver
import pages
import time

def before_feature(context, feature):
    context.browser = webdriver.Safari()
    context.registration_page = pages.RegistrationPage(context.browser)
    context.login_page = pages.LoginPage(context.browser)
    context.posts_page = pages.PostsPage(context.browser)

def after_feature(context, feature):
    context.browser.quit()
    
def after_step(context, step):
    # slow down for demo.
    time.sleep(2)