import time

from .base_page import BasePage
from .locators import SheetPageLocators
from .locators import FormaProrabotkaPotrebnosti


class SheetPage(BasePage):
    def add_potrebnost(self):
        self.page.click(SheetPageLocators.BUTTON_ADD_POTREBNOST)
        self.page.set_input_files(SheetPageLocators.UPLOAD_FILES, 'Example/potreb.xlsx')
        raw = "//html/body/div[2]/div/div[2]/div/div/div[2]/table/tbody/tr[1]/td[1]/div/span"
        self.page.locator(raw).wait_for()
        check = self.page.inner_text(raw)
        assert check == "НМЗ-НСК", "Таблица не создана!"

    def fill_the_fields_prorabotka_potrebnosti(self):
        self.page.click(FormaProrabotkaPotrebnosti.GENPODRYADCHICK)
        self.page.click(FormaProrabotkaPotrebnosti.GENPODRYADCHICK_OPTION)
        self.page.click(FormaProrabotkaPotrebnosti.DATEPICKER_1)
        self.page.click(FormaProrabotkaPotrebnosti.DATE)
        self.page.click(FormaProrabotkaPotrebnosti.IZGOTOVITEL_POLE)
        self.page.click(FormaProrabotkaPotrebnosti.IZGOTOVITEL_OPTION)
        self.page.click(FormaProrabotkaPotrebnosti.POSTAVSHIK_POLE)
        self.page.click(FormaProrabotkaPotrebnosti.POSTAVSHIK_OPTION)
        self.page.click(FormaProrabotkaPotrebnosti.DATE_VIBORA_ODCI)
        self.page.click(FormaProrabotkaPotrebnosti.DATE)
        self.page.click(FormaProrabotkaPotrebnosti.DATE_RAZRABOTKI_KDNO)
        self.page.click(FormaProrabotkaPotrebnosti.DATE)
        self.page.click(FormaProrabotkaPotrebnosti.DATE_SOGLASOVANIYA_KDNO)
        self.page.click(FormaProrabotkaPotrebnosti.DATE)
        self.page.fill(FormaProrabotkaPotrebnosti.COMMENT_ZAKUPKA, "Комментарий к закупке")
        self.page.fill(FormaProrabotkaPotrebnosti.ORIENTIR_CENA, "100")
        time.sleep(3)

    def click_button_rasschitat(self):
        self.page.click()

    def add_pid_in_forma(self):
        self.page.click(FormaProrabotkaPotrebnosti.PID_BUTTON)
        self.page.click(FormaProrabotkaPotrebnosti.PID)
        self.page.click(FormaProrabotkaPotrebnosti.BUTTON_ADD_PID)
        time.sleep(1)

    def click_button_open_forma(self, n):
        self.page.click(f"div.nav-buttons div.mdc-button__ripple >> nth={n}")

    def click_button_vnesti_in_forma(self):
        self.page.click(SheetPageLocators.BUTTON_VNESTI_IN_FORMA)




