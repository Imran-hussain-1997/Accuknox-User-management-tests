import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        # Use meaningful selectors (Visible Text & Placeholders)
        self.username_field = page.get_by_placeholder("Username")
        self.password_field = page.get_by_placeholder("Password")
        self.login_button = page.get_by_role("button", name="Login")

    def navigate(self):
        self.page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    def login(self, user, pwd):
        self.username_field.fill(user)
        self.password_field.fill(pwd)
        self.login_button.click()