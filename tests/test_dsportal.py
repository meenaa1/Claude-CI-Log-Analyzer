import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()

    # Uncomment this line to run Chrome in headless mode in CI
    options.add_argument("--headless=new")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    driver.implicitly_wait(10)

    yield driver

    driver.quit()


def test_dsportal_home_page(driver):
    # 1. Open the DS Portal application
    driver.get("https://dsportalapp.herokuapp.com/")

    # 2. Click the Get Started button
    get_started_btn = driver.find_element(
        By.XPATH, "//button[text()='Get Started']"
    )
    get_started_btn.click()

    # 3. Intentionally trigger a failure for the log analyzer demo
    non_existent_element = driver.find_element(
        By.ID, "non-existent-login-button"
    )

    assert non_existent_element.is_displayed()

    # # 3. Verify successful navigation to the main dashboard / home page
    # # Ensure the URL updates to the home route and navigation elements are visible
    # assert "home" in driver.current_url
    
    portal_header = driver.find_element(By.XPATH, "//a[contains(text(), 'NumpyNinja')]")
    assert portal_header.is_displayed()
