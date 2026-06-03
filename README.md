> **Please note this is an in-progress repository that I am creating to learn automation.**

# QA Automation Portfolio

End-to-end UI test suite for [SauceDemo](https://www.saucedemo.com/) built with Python, Pytest, and Playwright. Covers login, inventory, and checkout flows using the Page Object Model pattern.

---

## Tech Stack

- **Python 3.14.4**
- **Pytest** — test framework
- **Playwright** — browser automation
- **GitHub Actions** — CI/CD *(not yet implemented)*

---

## Project Structure

```
qa-automation-portfolio/
├── pages/
│   ├── login_page.py
│   └── inventory_page.py
├── tests/
│   └── test_login.py
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

---

## Setup & Installation

**1. Clone the repo**
```bash
git clone https://github.com/kn215/Python-Playwright-Learning.git
cd Python-Playwright-Learning
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Install Playwright browsers**
```bash
playwright install
```

---

## Running Tests

**Run the full suite**
```bash
pytest
```

**Run with verbose output**
```bash
pytest -v
```

**Run a specific file**
```bash
pytest tests/test_login.py
```

**Run headed (visible browser) with slow motion**
```bash
pytest --headed --slowmo=500
```

---

## Test Coverage

| Area | Tests |
|------|-------|
| Login — valid credentials | ✓ |
| Login — invalid credentials | ✓ |

More scenarios being added weekly.

---

## Author

Kenneth Navarra · [github.com/kn215](https://github.com/kn215)
