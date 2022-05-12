import time
import playwright

import pytest
from .models.auth_page import AuthPage
from playwright.sync_api import Page
import time


@pytest.mark.auth
def test_auth(page:Page):
    link = "https://dev.procurement.pragma.info/auth"
    page1 = AuthPage(page, link)
    page1.open()
    page1.auth_admin()
    time.sleep(3)




