import pytest
import os
import allure
import logging
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver

# --- WebDriver fixture ---
@pytest.fixture
def driver() -> WebDriver:
    """A fixture for launching and closing the browser"""
    options = Options()
    options.add_argument("--headless=new")  # Headless mode for CI/Docker
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument(f"--user-data-dir=/tmp/chrome-data-{os.getpid()}")  # Unique profile per session

    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

# --- Logger setup ---
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(f"{LOG_DIR}/test.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    """
    Hook to automatically take screenshot and attach to Allure on test failure
    """
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver")
        test_name = item.name
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        if driver:
            # Create folder for screenshots if not exists
            screenshot_dir = "screenshots"
            os.makedirs(screenshot_dir, exist_ok=True)

            screenshot_file = f"{screenshot_dir}/{test_name}_{timestamp}.png"
            driver.save_screenshot(screenshot_file)

            # Attach screenshot to Allure
            allure.attach.file(
                screenshot_file,
                name=f"Screenshot-{test_name}",
                attachment_type=allure.attachment_type.PNG
            )

            logger.error(f"[FAILED TEST] {test_name} failed. Screenshot saved: {screenshot_file}")
        else:
            logger.error(f"[FAILED TEST] {test_name} failed. No WebDriver instance found for screenshot.")


    



