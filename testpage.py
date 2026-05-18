import pytest
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.admin_page import AdminPage

# This 'fixture' runs before every test to set up the pages
@pytest.fixture
def setup(page: Page):
    login_page = LoginPage(page)
    admin_page = AdminPage(page)
    login_page.navigate()
    return login_page, admin_page

# TEST CASE 1: Login Block
def test_valid_login(page: Page, setup):
    login_pg, _ = setup
    login_pg.login("Admin", "admin123")
    # Verify we landed on Dashboard
    expect(page).to_have_url("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")

# TEST CASE 2: Add User Block
def test_add_new_user(page: Page, setup):
    login_pg, admin_pg = setup
    login_pg.login("Admin", "admin123")
    admin_pg.go_to_admin_module()
    
    # We use a unique name so the test doesn't fail on re-run
    test_username = "AccuKnox_Tester_01" 
    admin_pg.create_user("a", test_username, "Password@123")
    admin_pg.verify_success_message()

# TEST CASE 3: Search User Block
def test_search_user(page: Page, setup):
    login_pg, admin_pg = setup
    login_pg.login("Admin", "admin123")
    admin_pg.go_to_admin_module()
    
    # Fill search criteria
    admin_pg.search_username_input.fill("Admin")
    admin_pg.search_button.click()
    
    # Verify the result appears in the table
    expect(page.get_by_role("cell", name="Admin")).to_be_visible()