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
    # context = browser.new_context(storage_state="auth.json", **browser_context_args)

    yield context
    context.storage_state(path="auth.json")
    context.close()
    browser.close()
    # -----====---======
# import pytest
# from playwright.sync_api import BrowserType
# from typing import Dict
#
# @pytest.fixture(scope="session")
# def context(
#         browser_type: BrowserType,
#         browser_type_launch_args: Dict,
#         browser_context_args: Dict
# ):
#     context = browser_type.launch_persistent_context("./foobar", **{
#         **browser_type_launch_args,
#         **browser_context_args,
#         "headless": False,
#         "slow_mo": 100
#     })
#     yield context
#     context.close()