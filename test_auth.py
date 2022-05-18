import pytest
from .models.auth_page import AuthPage
from .models.project_page import ProjectPage
from playwright.sync_api import Page


@pytest.mark.auth
def test_auth(page: Page):
    print('Авторизация за администратора')
    link = "https://dev.procurement.pragma.info/auth"
    page1 = AuthPage(page, link)
    page2 = ProjectPage(page, link)
    page1.open()
    page1.auth_admin()
    page2.check_title_projects_page()

    # time.sleep(3)




