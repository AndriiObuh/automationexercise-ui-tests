# automationexercise-ui-tests

Automated UI tests for [automationexercise.com](https://automationexercise.com) using Python, Selenium, Pytest, Docker, and Allure.

## Description

This project contains UI automated tests for the main functionalities of automationexercise.com.  
Tests are built using Page Object Model (POM) and run with Pytest. Results are stored in Allure reports.  

CI/CD is configured with GitHub Actions, running tests automatically on push or pull request to the `main` branch inside Docker.

## Tech Stack

- Python  
- Selenium  
- Pytest  
- Allure  
- Docker  
- GitHub Actions  

## Setup

### 1. Clone the repository
```bash
git clone https://github.com/AndriiObuh/automationexercise-ui-tests.git
cd automationexercise-ui-tests
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate    # Linux/MacOS
.\.venv\Scripts\activate     # Windows
```
### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. (Optional) Build Docker image
```bash
docker build -t automationexercise-ui-tests:latest .
```

### Run Tests
#### Locally
```bash
pytest --alluredir=allure-results
allure serve allure-results
```
#### In Docker
```bash
docker run --rm -v $PWD/allure-results:/app/allure-results automationexercise-ui-tests:latest
```

### CI/CD
GitHub Actions workflow:  .github/workflows/ui-tests.yml
- Runs tests in Docker on push or pull request to main branch
- Uploads Allure results as artifacts

### Project Structure

```
automationexercise-ui-tests/
├── .github/workflows/ui-tests.yml
├── allure-report/
├── allure-results/
├── conftest.py
├── data/data.py
├── generator/generator.py
├── logs/test.log
├── pages/*.py
├── screenshots/
├── tests/*.py
├── Dockerfile
└── requirements.txt
```

### Test Scenarios
- User registration
- Login (correct / incorrect)
- Contact Us form
- Product search
- Add products to cart
- Place order (register during checkout)
- Scroll page

### Contributing
- Fork the repository & create a branch
- Make your changes & write tests if needed
- Commit & push
- Open a Pull Request

### Author
Andrii Obuh