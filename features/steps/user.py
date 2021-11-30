from behave import *

@given('新規登録手続き中である')
def start_signup(context):
    context.registration_page.open()

@when('ユーザ名 {username} 、パスワード {password} で登録する')
def register(context, username, password):
    context.registration_page.register(username, password)

@when('ログインを始める')
def start_login(context):
    context.login_page.open()

@when('ユーザ名 {username} 、パスワード {password} でログインする')
def login(context, username, password):
    context.login_page.login(username, password)

@then('{username} としてログインした状態になる')
def logged_in_as(context, username):
    assert context.posts_page.username_logged_in == username
