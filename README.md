# 🛒 E-Commerce Selenium Automation Framework (Python + Pytest + POM)

## 📌 Overview
This is a UI test automation framework built using Selenium WebDriver with Python and Pytest to validate an end-to-end e-commerce workflow. The framework follows industry-standard design patterns such as Page Object Model (POM), data-driven testing using JSON, and modular reusable architecture. It simulates a real user journey from login → product selection → cart → checkout → order confirmation.

## ⚙️ Tech Stack
- Python 3.x  
- Selenium WebDriver  
- Pytest Framework  
- JSON (Test Data Management)  
- Page Object Model (POM)  
- WebDriverWait (Explicit waits)  

## 🏗️ Framework Architecture
pageObjects/ → Page classes (Login, Shop, Checkout pages)  
tests/ → Test scripts (end-to-end scenarios)  
testData/ → JSON-based test data  
conftest.py → Pytest fixtures (browser setup & teardown)  
utilities/ → Common reusable helper functions  

## 🔄 End-to-End Test Flow
1. Launch browser using Pytest fixture  
2. Navigate to login page  
3. Login using credentials from JSON test data  
4. Validate successful login  
5. Search and select products dynamically  
6. Add products to cart  
7. Proceed to checkout  
8. Enter delivery country  
9. Validate order summary  
10. Confirm successful order placement  

## 📂 Data-Driven Testing
Test data is stored in JSON format under testData/. Pytest @pytest.mark.parametrize is used for multiple datasets, enabling execution with multiple users and product combinations.

Example:
@pytest.mark.parametrize("test_data_list_items", test_data_list)

## 🚀 Key Features
✔ Page Object Model (POM) implementation  
✔ Data-driven testing using JSON  
✔ Pytest fixtures for browser setup and teardown  
✔ Explicit waits for synchronization  
✔ Modular page-wise separation (Login / Shop / Checkout)  
✔ Reusable utility methods  
✔ Scalable and maintainable framework design  
✔ Clean separation of test data and test logic  

## ▶️ How to Run Tests
pip install -r requirements.txt  
pytest -v -s  
pytest tests/test_e2e.py -v -s  
pytest -m smoke  

## 📊 Reporting & Debugging
HTML reports with screenshots on failure generated using pytest-html and stored in reports/report.html. 

## 🧠 Design Principles Used
Page Object Model (POM), Data-driven testing, Fixture-based setup, Separation of test logic and page logic, Reusable utilities, Maintainable structure.

## 🔮 Future Enhancements
CI/CD integration using Jenkins or GitHub Actions, Allure reporting dashboard, Dockerized execution, Logging framework integration, API + UI hybrid testing.


## ⭐ Note
This framework is built for learning and real-world QA automation demonstration using scalable industry practices.
