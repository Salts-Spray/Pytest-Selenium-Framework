import pytest
import pytest_html
from utils.driver_factory import DriverFactory


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="firefox", help="Browser to run tests on"
    )


@pytest.fixture(scope="class")
def driver_init(request):
    browser = request.config.getoption("--browser")
    driver = DriverFactory.get_driver(browser)
    request.cls.driver = driver
    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Attach a screenshot to the HTML report on test failure.
    """
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        driver = item.funcargs['driver_init']
        screenshot = driver.get_screenshot_as_base64()
        extra = getattr(report, 'extra', [])
        extra.append(pytest_html.extras.image(screenshot, mime_type='image/png'))
        report.extra = extra
