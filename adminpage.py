from playwright.sync_api import Page, expect

class AdminPage:
    def __init__(self, page: Page):
        self.page = page
        self.admin_tab = page.get_by_role("link", name="Admin")
        self.add_button = page.get_by_role("button", name="Add")
        self.save_button = page.get_by_role("button", name="Save")
        # Selector for the Username search box in the grid
        self.search_username_input = page.locator(".oxd-input").nth(1) 
        self.search_button = page.get_by_role("button", name="Search")

    def go_to_admin_module(self):
        self.admin_tab.click()

    def create_user(self, employee_name, username, password):
        self.add_button.click()
        
        # Handling the dropdowns (Specific to OrangeHRM structure)
        self.page.get_by_text("-- Select --").first.click()
        self.page.get_by_role("option", name="ESS").click()
        
        # Autocomplete field
        self.page.get_by_placeholder("Type for hints...").fill(employee_name)
        # Proper Wait: Wait for the suggestion to appear before clicking
        self.page.locator(".oxd-autocomplete-dropdown").get_by_text(employee_name).first.click()
        
        self.page.get_by_text("-- Select --").click()
        self.page.get_by_role("option", name="Enabled").click()

        # Credentials
        # Note: Using labels to find inputs is a 'meaningful selector'
        self.page.locator("xpath=//label[text()='Username']/../following-sibling::div//input").fill(username)
        self.page.locator("xpath=//label[text()='Password']/../following-sibling::div//input").fill(password)
        self.page.locator("xpath=//label[text()='Confirm Password']/../following-sibling::div//input").fill(password)
        
        self.save_button.click()

    def verify_success_message(self):
        # Proper Wait: Playwright automatically waits for this to be visible
        expect(self.page.get_by_text("Successfully Saved")).to_be_visible()