import os

import pytest
from selenium import webdriver


#registering config option

from selenium.webdriver.chrome.options import Options


# Register custom command-line option
def pytest_addoption(parser):

    parser.addoption(
        "--browser_name",
        action="store",
        default="chrome",
        help="Type of browser: chrome, firefox, or edge"
    )


# Browser fixture
@pytest.fixture(scope='session')
def browser_instance(request):

    browser_name = request.config.getoption("browser_name")

    if browser_name == 'chrome':

        chrome_options = Options()

        # Disable password save popup
        chrome_options.add_experimental_option(
            "prefs",
            {
                "credentials_enable_service": False,
                "profile.password_manager_enabled": False
            }
        )

        # Disable password breach notification
        chrome_options.add_argument("--disable-features=PasswordLeakDetection")

        driver = webdriver.Chrome(options=chrome_options)

    elif browser_name == 'edge':

        driver = webdriver.Edge()

    driver.maximize_window()
    driver.implicitly_wait(5)

    yield driver

    driver.quit()


# Hook for screenshot on failure


# =========================
# Add command line option
# =========================

def pytest_addoption(parser):

    parser.addoption(
        "--browser_name",
        action="store",
        default="chrome",
        help="Browser selection: chrome or edge"
    )


# =========================
# Browser Fixture
# =========================

@pytest.fixture(scope="function")
def browser_instance(request):

    browser_name = request.config.getoption("browser_name")

    if browser_name == "chrome":

        chrome_options = Options()

        # Disable password save popup
        chrome_options.add_experimental_option(
            "prefs",
            {
                "credentials_enable_service": False,
                "profile.password_manager_enabled": False
            }
        )

        # Disable password breach popup
        chrome_options.add_argument(
            "--disable-features=PasswordLeakDetection"
        )

        driver = webdriver.Chrome(options=chrome_options)

    elif browser_name == "edge":

        driver = webdriver.Edge()

    else:
        raise Exception("Browser not supported")

    driver.maximize_window()
    driver.implicitly_wait(5)

    yield driver

    driver.quit()


# =========================
# Screenshot on Failure Hook
# =========================
# =========================
# Screenshot on Failure Hook
# =========================

import pytest
import os


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):

    pytest_html = item.config.pluginmanager.getplugin("html")

    outcome = yield
    report = outcome.get_result()

    extra = getattr(report, "extras", [])

    # Capture screenshot only when test fails
    if report.when == "call" and report.failed:

        # Get driver instance from fixture
        driver = item.funcargs["browser_instance"]

        # Create reports folder if not exists
        reports_dir = "reports"

        if not os.path.exists(reports_dir):
            os.makedirs(reports_dir)

        # Screenshot file name
        file_name = report.nodeid.replace("::", "_").replace("/", "_") + ".png"

        # Full screenshot path
        file_path = os.path.join(reports_dir, file_name)

        # Capture screenshot
        driver.save_screenshot(file_path)

        print(f"Screenshot saved at: {file_path}")

        # Add screenshot to HTML report
        html = f'''
        <div>
            <a href="{file_name}">
                <img src="{file_name}" alt="screenshot"
                style="width:500px;height:300px;border:1px solid black;"
                onclick="window.open(this.src)"
                align="right"/>
            </a>
        </div>
        '''

        extra.append(pytest_html.extras.html(html))

    report.extras = extra