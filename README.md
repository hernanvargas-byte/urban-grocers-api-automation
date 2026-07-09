# Urban Grocers - API Automation Testing Framework

This repository contains an automated testing suite designed to validate the REST API backend functionality for the **Urban Grocers** platform. The framework focuses on verifying business rules, boundary values, data integrity, and error-handling logic during user creation workflows.

## 🧪 Automated Workflows Covered
* **Positive Scenarios:** Validation of successful user creation using compliant `firstName` parameters.
* **Negative Scenarios:** Testing system response with empty strings, special characters, integers, and length limit boundary injections.
* **Response Validation:** Asserting correct HTTP status codes (e.g., 201 Created, 400 Bad Request) and structure parsing.

## 🛠️ Tech Stack & Engineering Techniques
* **Language:** Python 3.12+
* **Test Runner:** Pytest
* **HTTP Client:** Requests
* **Automation Patterns:** Modular separation of concerns. Endpoints configurations (`configuration.py`), request payloads (`data.py`), and atomic request methods (`sender_stand_request_post.py`) are strictly decoupled from the test assertions layer (`create_user_test.py`).

## 📐 Project Structure
```text
📦 api_stand_tests
 ┣ 📂 resources                  # Text logs, static mocks, and test artifacts.
 ┣ 📜 configuration.py          # Centralized API base URLs and endpoint routes.
 ┣ 📜 data.py                   # Request body dictionaries and headers mapping.
 ┣ 📜 sender_stand_request_get.py   # HTTP GET request wrappers.
 ┣ 📜 sender_stand_request_post.py  # HTTP POST request wrappers.
 ┣ 📜 create_user_test.py       # Main test suite containing positive and negative test cases.
 ┣ 📜 .gitignore                # Target exclusions for virtual environments and IDE caches.
 ┗ 📜 README.md                 # Project documentation.
```
## 🚀 Getting Started & Execution Instructions
### 1. Clone the Repository
```bash 
git clone [https://github.com/hernanvargas-byte/api_stand_tests.git](https://github.com/hernanvargas-byte/api_stand_tests.git)
cd api_stand_tests
```
### 2. Configure the Virtual Environment
```bash
python -m venv .venv
# On Windows (Git Bash / Command Prompt):
source .venv/Scripts/activate
# On macOS/Linux:
source .venv/bin/activate
```
### 3. Install Dependencies
```bash
pip install requests pytest
```

### 4. Run the Test Suite
To execute all functional API tests with detailed verbose output, run:
```bash
pytest create_user_test.py -v
```