# AccuKnox User Management Tests

Automated end-to-end test suite for OrangeHRM User Management module using Playwright with Page Object Model (POM) pattern.

## 📋 Project Overview

This project automates the complete user management workflow in OrangeHRM, including:
- User login
- Adding new users
- Searching users
- Editing user details
- Validating updates
- Deleting users

**Application Under Test (AUT):** [OrangeHRM Demo](https://opensource-demo.orangehrmlive.com/web/index.php/auth/login)

## 🛠️ Tech Stack

- **Playwright Version:** 1.40.0+ (Python)
- **Python Version:** 3.8+
- **Testing Framework:** pytest
- **Design Pattern:** Page Object Model (POM)

## 📁 Project Structure

```
AccuKnox-user-management-tests/
├── pages/
│   ├── login_page.py          # Login page object
│   └── admin_page.py          # Admin/User management page object
├── tests/
│   └── test_user_management.py # Test cases
├── test_cases.xlsx            # Manual test case documentation
├── requirements.txt           # Python dependencies
├── pytest.ini                 # Pytest configuration
├── .gitignore                 # Git ignore file
└── README.md                  # This file
```

## 🚀 Setup Instructions

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Git

### Installation Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/AccuKnox-user-management-tests.git
   cd AccuKnox-user-management-tests
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Install Playwright browsers:**
   ```bash
   playwright install
   ```

## 📝 Running the Tests

### Run all tests:
```bash
pytest tests/
```

### Run specific test file:
```bash
pytest tests/test_user_management.py
```

### Run specific test case:
```bash
pytest tests/test_user_management.py::test_add_new_user
```

### Run with verbose output:
```bash
pytest tests/ -v
```

### Run with detailed output and screenshots on failure:
```bash
pytest tests/ -v --screenshot=only-on-failure
```

### Run in headed mode (see browser):
```bash
pytest tests/ --headed
```

### Generate HTML report:
```bash
pytest tests/ --html=report.html --self-contained-html
```

## 🧪 Test Cases

### Manual Test Cases

Refer to **test_cases.xlsx** for comprehensive manual test case documentation with the following columns:
- Test Scenario
- Pre-conditions
- Test Steps
- Test Data
- Expected Result
- Actual Result (optional)
- Status (optional)

**Key Manual Test Scenarios:**
1. Navigate to Admin Module
2. Add New User
3. Search User
4. Edit User Details
5. Validate Updated Details
6. Delete User

### Automated Test Cases

#### Test 1: Valid Login
- **Objective:** Verify admin can login successfully
- **Steps:** Enter credentials and click Login
- **Expected:** Dashboard loads with correct URL

#### Test 2: Add New User
- **Objective:** Create a new user in the system
- **Steps:** Navigate to Admin → Click Add → Fill user details → Save
- **Expected:** Success message displayed

#### Test 3: Search User
- **Objective:** Search for created user
- **Steps:** Enter username in search box → Click Search
- **Expected:** User appears in results table

## 📄 Page Object Model Structure

### LoginPage (`pages/login_page.py`)
Handles login functionality with meaningful selectors:
- `username_field` - Username input field
- `password_field` - Password input field
- `login_button` - Login button

**Methods:**
- `navigate()` - Navigate to login page
- `login(user, pwd)` - Perform login

### AdminPage (`pages/admin_page.py`)
Handles user management operations:
- `admin_tab` - Admin module link
- `add_button` - Add user button
- `save_button` - Save button
- `search_username_input` - Search input field
- `search_button` - Search button

**Methods:**
- `go_to_admin_module()` - Navigate to Admin module
- `create_user(employee_name, username, password)` - Create new user
- `verify_success_message()` - Verify success notification

## 🔍 Selector Strategy

This project uses meaningful selectors following best practices:

1. **Role-based selectors** (preferred):
   ```python
   page.get_by_role("button", name="Add")
   page.get_by_role("link", name="Admin")
   ```

2. **Placeholder-based selectors**:
   ```python
   page.get_by_placeholder("Username")
   page.get_by_placeholder("Password")
   ```

3. **Text-based selectors**:
   ```python
   page.get_by_text("Successfully Saved")
   ```

4. **XPath for complex scenarios**:
   ```python
   page.locator("xpath=//label[text()='Username']/../following-sibling::div//input")
   ```

## ⏱️ Wait Strategies

Playwright automatically handles waits with:
- **Auto-waiting:** Elements are waited for before interaction
- **Explicit waits:** Using `expect()` for assertions
- **Proper waits:** Autocomplete suggestions wait before clicking

Example:
```python
self.page.locator(".oxd-autocomplete-dropdown").get_by_text(employee_name).first.click()
```

## 🔐 Test Credentials

**Username:** Admin  
**Password:** admin123

⚠️ **Note:** These are demo credentials for the public OrangeHRM instance. Never commit real credentials to version control.

## 📊 Test Data

Test data is defined within test cases for simplicity:
```python
test_username = "AccuKnox_Tester_01"
password = "Password@123"
```

For larger projects, consider using:
- External CSV/JSON files
- Environment variables
- Database fixtures

## 🐛 Known Issues & Workarounds

### Issue 1: Autocomplete Dropdown Timing
**Problem:** Autocomplete suggestions may not appear immediately  
**Solution:** Added explicit wait for `.oxd-autocomplete-dropdown` before clicking

### Issue 2: Multiple "Select" Dropdowns
**Problem:** Multiple dropdowns with same text  
**Solution:** Used `.first` selector to target the first occurrence

### Issue 3: Dynamic Input Selectors
**Problem:** Input fields lack unique IDs  
**Solution:** Used XPath with label text for reliable identification

## 🔄 CI/CD Integration

### GitHub Actions Example
Create `.github/workflows/tests.yml`:
```yaml
name: Playwright Tests
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - run: pip install -r requirements.txt
      - run: playwright install
      - run: pytest tests/
```

## 📦 Dependencies

See `requirements.txt`:
```
playwright==1.40.0
pytest==7.4.3
pytest-html==4.1.1
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-tests`)
3. Commit changes (`git commit -m 'Add new test cases'`)
4. Push to branch (`git push origin feature/new-tests`)
5. Open a Pull Request

## 📚 Best Practices Implemented

✅ Page Object Model for maintainability  
✅ Meaningful selectors (role, placeholder, text-based)  
✅ Proper wait strategies  
✅ Fixture-based test setup  
✅ Descriptive test names  
✅ DRY principle (Don't Repeat Yourself)  
✅ Clear documentation  
✅ Modular code structure  

## 🚨 Troubleshooting

### Tests fail with "Element not found"
- Verify the application is accessible
- Check if selectors have changed in the AUT
- Run in headed mode to debug: `pytest --headed`

### Playwright not installed
```bash
playwright install
```

### Import errors
Ensure you're in the correct virtual environment and dependencies are installed:
```bash
pip install -r requirements.txt
```

### Tests timeout
Increase timeout in `pytest.ini`:
```ini
[pytest]
timeout = 60
```

## 📞 Support

For issues or questions:
1. Check existing GitHub issues
2. Review Playwright documentation: https://playwright.dev/python/
3. Check pytest documentation: https://docs.pytest.org/

## 📄 License

This project is licensed under the MIT License - see LICENSE file for details.

## 👤 Author

**AccuKnox QA Trainee**  
Practical Assessment - User Management E2E Testing

---

**Last Updated:** 2024  
**Playwright Version:** 1.40.0+  
**Python Version:** 3.8+
