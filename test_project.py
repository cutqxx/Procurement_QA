import pytest
from .models.project_page import ProjectPage
from .models.sheet_page import SheetPage
from playwright.sync_api import Page
import time


@pytest.mark.smoke
class TestSmoke():
    def test_create_new_project(self, page: Page):
        link = "https://procurement2021.tk/projects"
        page_project = ProjectPage(page, link)
        page_project.open()
        page_project.check_title_projects_page()
        page_project.click_to_button_projects_edit()
        page_project.click_to_button_add_project()
        page_project.create_new_projects()
        time.sleep(1)

    def test_add_potreb_in_project(self, page: Page):
        link = "https://procurement2021.tk/projects"
        page_project = ProjectPage(page, link)
        page_sheet = SheetPage(page, link)
        page_project.open()
        page_project.open_project()
        # page_sheet.check_name_project()
        page_sheet.add_potrebnost()
        # time.sleep(3)

    @pytest.mark.new
    def test_fill_forma_prorabotka(self, page: Page):
        link = "https://procurement2021.tk/projects"
        page_project = ProjectPage(page, link)
        page_sheet = SheetPage(page, link)
        # page_project.open_context()
        print("Тест: заполнение данных в форму предварительной подготовки")
        page_project.open()
        page_project.open_project()
        page_sheet.click_button_open_forma(1)
        page_sheet.add_pid_in_forma()
        page_sheet.fill_the_fields_prorabotka_potrebnosti()
        page_sheet.click_button_vnesti_in_forma()
