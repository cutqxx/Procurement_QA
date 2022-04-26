import pytest
from playwright.sync_api import Playwright, sync_playwright
from playwright.sync_api import BrowserType
from playwright.sync_api import (Browser, BrowserContext)
from typing import Dict,Generator


@pytest.fixture()
def context(
    browser: Browser,
    browser_type: BrowserType,
    browser_type_launch_args: Dict,
    browser_context_args: Dict,
):

    browser = browser_type.launch(**{
        **browser_type_launch_args,
        **browser_context_args,
        "headless": False,
        "slow_mo": 100
    })
    context = browser.new_context(storage_state="auth.json", **browser_context_args)

    yield context
    context.storage_state(path="auth.json")
    context.close()
    browser.close()




# @pytest.fixture(scope="function")
# def context(playwright: Playwright):
#
#     print("\nЗапуск браузера")
#     chromium = playwright.chromium
#     browser = chromium.launch(headless=False)
#     # context = browser.new_context()
#     context = browser.new_context(storage_state="./auth.json")
#     # page = context.new_page()
#
#     yield browser
#     # context.storage_state(path="auth.json")
#     print("\nЗакрытие браузера")
#     browser.close()

# @pytest.fixture()
# def context(
#         browser: Browser, browser_context_args:Dict
# ) -> Generator[BrowserContext, None, None]:
#     context = browser.new_context(storage_state="auth.json", **browser_context_args)
#
#     yield context
#     context.close()