from .base_page import BasePage
from .locators import ProjectsPageLocators
import time
import playwright


class ProjectPage(BasePage):

    def check_title_projects_page(self):
        title = self.page.inner_text(ProjectsPageLocators.TITLE_NAME)
        assert title == "Проекты", 'Вы находитесь не на экране "Проекты"'

    def click_to_button_add_project(self):
        self.page.click(ProjectsPageLocators.BUTTON_ADD_PROJECT)

    def click_to_button_projects_edit(self):
        self.page.click(ProjectsPageLocators.BUTTON_EDIT_PROJECTS)

    def create_new_projects(self):
        self.page.fill(ProjectsPageLocators.NAME_NEW_PROJECT, "project")
        self.page.click(ProjectsPageLocators.CREATE_PROJECT_BUTTON)
        time.sleep(0.5)
        locator = self.page.locator(ProjectsPageLocators.CHECK_COUNT_PROJECT_EDIT_CARD)
        count = locator.count()
        n = count
        assert self.page.inner_text(f"//div[2]/div/div[2]/div/div/div[2]/div[{n}]/div[2]/span[2]") == "project",\
            "Проект не создан"

    def delete_project(self):
        self.page.click(ProjectsPageLocators.DELETE_PROJECT_BUTTON)
        time.sleep(1)

    def open_project(self):
        assert self.page.locator("text=project"), "В системе нет проекта с названием project!"
        self.page.click("text=project")