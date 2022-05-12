import pytest
from .models.project_page import ProjectPage
from .models.sheet_page import SheetPage
from playwright.sync_api import Page
import time


@pytest.mark.smoke
class TestSmoke():
    def test_create_new_project(self, page: Page):
        link = "https://dev.procurement.pragma.info/projects"
        page_project = ProjectPage(page, link)
        page_project.open()
        page_project.check_title_projects_page()
        page_project.click_to_button_projects_edit()
        page_project.click_to_button_add_project()
        page_project.create_new_projects()
        time.sleep(1)

    def test_add_potreb_in_project(self, page: Page):
        link = "https://dev.procurement.pragma.info/projects"
        page_project = ProjectPage(page, link)
        page_sheet = SheetPage(page, link)
        page_project.open()
        page_project.open_project()
        # page_sheet.check_name_project()
        page_sheet.add_potrebnost()
        # time.sleep(3)

    def test_fill_forma_prorabotka(self, page: Page):
        print("Тест: заполнение данных в форму предварительной подготовки")
        link = "https://dev.procurement.pragma.info/projects"
        page_project = ProjectPage(page, link)
        page_sheet = SheetPage(page, link)
        page_project.open()
        page_project.open_project()
        page_sheet.click_button_open_forma(1)
        page_sheet.add_pid_in_forma()
        page_sheet.fill_the_fields_prorabotka_potrebnosti()
        page_sheet.click_button_vnesti_in_forma()
        page_sheet.data_entry_check_after_prorabotka_potrebnosti()

    def test_fill_forma_kontraktaciya(self, page: Page):
        print("Тест: заполнение данных в форму контрактации")
        link = "https://dev.procurement.pragma.info/projects"
        page_project = ProjectPage(page, link)
        page_sheet = SheetPage(page, link)
        page_project.open()
        page_project.open_project()
        page_sheet.click_button_open_forma(2)
        page_sheet.add_pid_in_forma()
        page_sheet.fill_the_fields_kontraknaciya()
        page_sheet.click_button_rasschitat()
        page_sheet.click_button_vnesti_in_forma()
        page_sheet.data_entry_check_after_kontraktacii()

    def test_fill_forma_otgruzka(self,page: Page ):
        print("Тест: заполнение данных в форму отгрузки")
        link = "https://dev.procurement.pragma.info/projects"
        page_project = ProjectPage(page, link)
        page_sheet = SheetPage(page, link)
        page_project.open()
        page_project.open_project()
        page_sheet.click_button_open_forma(3)
        page_sheet.add_pid_in_forma()
        page_sheet.fill_the_fields_otgruzka()
        page_sheet.click_button_vnesti_in_forma()
        page_sheet.data_entry_check_after_otgruzka()

    def test_fill_forma_logistika(self, page: Page):
        print("Тест: заполнение данных в форму логистики")
        link = "https://dev.procurement.pragma.info/projects"
        page_project = ProjectPage(page, link)
        page_sheet = SheetPage(page, link)
        page_project.open()
        page_project.open_project()
        page_sheet.click_button_open_forma(4)
        page_sheet.add_pid_in_forma()
        page_sheet.fill_the_fields_logistika()
        page_sheet.click_button_vnesti_in_forma()
        page_sheet.data_entry_check_after_logistika()

    def test_fill_forma_postuplenie(self, page: Page):
        print("Тест: заполнение данных в форму поступление")
        link = "https://dev.procurement.pragma.info/projects"
        page_project = ProjectPage(page, link)
        page_sheet = SheetPage(page, link)
        page_project.open()
        page_project.open_project()
        page_sheet.click_button_open_forma(5)
        page_sheet.add_pid_in_forma()
        page_sheet.fill_the_fields_postuplenie()
        page_sheet.click_button_vnesti_in_forma()
        page_sheet.data_entry_check_after_postuplenie()


    def test_fill_forma_oprihodovanie(self, page: Page):
        print("Тест: заполнение данных в форму оприходование")
        link = "https://dev.procurement.pragma.info/projects"
        page_project = ProjectPage(page, link)
        page_sheet = SheetPage(page, link)
        page_project.open()
        page_project.open_project()
        page_sheet.click_button_open_forma(6)
        page_sheet.add_pid_in_forma()
        page_sheet.fill_the_fields_oprihodovanie()
        page_sheet.click_button_vnesti_in_forma()
        page_sheet.data_entry_check_after_oprihodovanie()

    def test_fill_forma_vidacha_v_prozvodstvo(self, page: Page):
        print("Тест: заполнение данных в форму выдача в производств")
        link = "https://dev.procurement.pragma.info/projects"
        page_project = ProjectPage(page, link)
        page_sheet = SheetPage(page, link)
        page_project.open()
        page_project.open_project()
        page_sheet.click_button_open_forma(7)
        page_sheet.add_pid_in_forma()
        page_sheet.fill_the_fields_vidacha_v_prozvodstvo()
        page_sheet.click_button_vnesti_in_forma()
        page_sheet.data_entry_check_after_vidacha_v_prozvodstvo()


    #---- Корректировка потребности ---
    # def test_korrektirovka_potrabnosti(self, page: Page):
    #     print("Тест: проверка функционала Корректировки потребности")
    #     link = "https://dev.procurement.pragma.info/projects"
    #     page_project = ProjectPage(page, link)
    #     page_sheet = SheetPage(page, link)
    #     page_project.open()
    #     page_project.open_project()
    #     page_sheet.click_button_open_forma(7)
    #     page_sheet.add_pid_in_forma()
    #     page_sheet.fill_the_fields_korrektirovka_potrabnosti()
    #     page_sheet.click_button_vnesti_in_forma()
    #     page_sheet.data_entry_check_after_vidacha_v_prozvodstvo()

    @pytest.mark.new
    def test_delete_project(self, page: Page):
        print("Тест: удаление проекта")
        link = "https://dev.procurement.pragma.info/projects"
        page_project = ProjectPage(page, link)
        page_project.open()
        page_project.click_to_button_projects_edit()
        page_project.delete_project()