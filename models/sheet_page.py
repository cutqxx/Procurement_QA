import time

from .base_page import BasePage
from .locators import SheetPageLocators
from .locators import FormaProrabotkaPotrebnosti
from .locators import FormaKontraktacii
from .locators import FormaOtgruzka
from .locators import FormaLogistika
from .locators import FormaPostuplenie
from .locators import FormaOprihodovanie


class SheetPage(BasePage):

    def scroll_general_table(self):
        self.page.locator("div.table-board-td >> nth=-1").scroll_into_view_if_needed()
        self.page.locator("div.table-board-td >> nth=-1").scroll_into_view_if_needed()
        self.page.locator("div.table-board-td >> nth=-1").scroll_into_view_if_needed()
        self.page.locator("div.table-board-td >> nth=-1").scroll_into_view_if_needed()
        self.page.locator("div.table-board-td >> nth=-1").scroll_into_view_if_needed()
        self.page.locator("div.table-board-td >> nth=-1").scroll_into_view_if_needed()
        self.page.locator("div.table-board-td >> nth=-1").scroll_into_view_if_needed()
        self.page.locator("div.table-board-td >> nth=-1").scroll_into_view_if_needed()
        self.page.locator("div.table-board-td >> nth=-1").scroll_into_view_if_needed()
        self.page.locator("div.table-board-td >> nth=-1").scroll_into_view_if_needed()
        self.page.locator("div.table-board-td >> nth=-1").scroll_into_view_if_needed()
        self.page.locator("div.table-board-td >> nth=-1").scroll_into_view_if_needed()
        self.page.locator("div.table-board-td >> nth=-1").scroll_into_view_if_needed()
        self.page.locator("div.table-board-td >> nth=-1").scroll_into_view_if_needed()
        self.page.locator("div.table-board-td >> nth=-1").scroll_into_view_if_needed()
        self.page.locator("div.table-board-td >> nth=-1").scroll_into_view_if_needed()
        self.page.locator("div.table-board-td >> nth=-1").scroll_into_view_if_needed()
        self.page.locator("div.table-board-td >> nth=-1").scroll_into_view_if_needed()
        self.page.locator("div.table-board-td >> nth=-1").scroll_into_view_if_needed()
        self.page.locator("div.table-board-td >> nth=-1").scroll_into_view_if_needed()
        self.page.locator("div.table-board-td >> nth=-1").scroll_into_view_if_needed()
        self.page.locator("div.table-board-td >> nth=-1").scroll_into_view_if_needed()
        self.page.locator("div.table-board-td >> nth=-1").scroll_into_view_if_needed()
        self.page.locator("div.table-board-td >> nth=-1").scroll_into_view_if_needed()
        self.page.locator("div.table-board-td >> nth=-1").scroll_into_view_if_needed()
        self.page.locator("div.table-board-td >> nth=-1").scroll_into_view_if_needed()
        self.page.locator("div.table-board-td >> nth=-1").scroll_into_view_if_needed()
        self.page.locator("div.table-board-td >> nth=-1").scroll_into_view_if_needed()
        self.page.locator("div.table-board-td >> nth=-1").scroll_into_view_if_needed()
        self.page.locator("div.table-board-td >> nth=-1").scroll_into_view_if_needed()
        self.page.locator("div.table-board-td >> nth=-1").scroll_into_view_if_needed()
        self.page.locator("div.table-board-td >> nth=-1").scroll_into_view_if_needed()
        self.page.locator("div.table-board-td >> nth=-1").scroll_into_view_if_needed()
        self.page.locator("div.table-board-td >> nth=-1").scroll_into_view_if_needed()
        self.page.locator("div.table-board-td >> nth=-1").scroll_into_view_if_needed()
        self.page.locator("div.table-board-td >> nth=-1").scroll_into_view_if_needed()
        self.page.locator("div.table-board-td >> nth=-1").scroll_into_view_if_needed()
        self.page.locator("div.table-board-td >> nth=-1").scroll_into_view_if_needed()
        self.page.locator("div.table-board-td >> nth=-1").scroll_into_view_if_needed()
        self.page.locator("div.table-board-td >> nth=-1").scroll_into_view_if_needed()
        self.page.locator("div.table-board-td >> nth=-1").scroll_into_view_if_needed()
        self.page.locator("div.table-board-td >> nth=-1").scroll_into_view_if_needed()
        self.page.locator("div.table-board-td >> nth=-1").scroll_into_view_if_needed()
        self.page.locator("div.table-board-td >> nth=-1").scroll_into_view_if_needed()
        self.page.locator("div.table-board-td >> nth=-1").scroll_into_view_if_needed()
        self.page.locator("div.table-board-td >> nth=-1").scroll_into_view_if_needed()
        self.page.locator("div.table-board-td >> nth=-1").scroll_into_view_if_needed()
        self.page.locator("div.table-board-td >> nth=-1").scroll_into_view_if_needed()

    def click_button_rasschitat(self):
        self.page.click(SheetPageLocators.BUTTON_RASSCHITAT_IN_FORMA)

    def add_pid_in_forma(self):
        self.page.click(FormaProrabotkaPotrebnosti.PID_BUTTON)
        self.page.locator(FormaProrabotkaPotrebnosti.PID).wait_for()
        self.page.click(FormaProrabotkaPotrebnosti.PID)
        self.page.click(FormaProrabotkaPotrebnosti.BUTTON_ADD_PID)
        time.sleep(1)

    def click_button_open_forma(self, n):
        self.page.click(f"div.nav-buttons div.mdc-button__ripple >> nth={n}")

    def click_button_vnesti_in_forma(self):
        self.page.click(SheetPageLocators.BUTTON_VNESTI_IN_FORMA)

    # ------
    # --Внесение данных в формы заполнения табличных данных

    def add_potrebnost(self):
        self.page.click(SheetPageLocators.BUTTON_ADD_POTREBNOST)
        self.page.set_input_files(SheetPageLocators.UPLOAD_FILES, 'Example/potreb.xlsx')
        # raw = self.page.locator(SheetPageLocators.CHECK_ADD_POTREBNOST).wait_for()
        time.sleep(0.5)
        check = self.page.inner_text(SheetPageLocators.CHECK_ADD_POTREBNOST)
        assert check == "НМЗ-НСК", "Таблица не создана!"

    # Форма "Предв. проработка потребности"
    def fill_the_fields_prorabotka_potrebnosti(self):
        self.page.click(FormaProrabotkaPotrebnosti.GENPODRYADCHICK)
        self.page.click(FormaProrabotkaPotrebnosti.SELECTOR_OPTION)
        self.page.click(FormaProrabotkaPotrebnosti.DATEPICKER_1)
        self.page.click(FormaProrabotkaPotrebnosti.DATE)
        self.page.click(FormaProrabotkaPotrebnosti.IZGOTOVITEL_POLE)
        self.page.click(FormaProrabotkaPotrebnosti.SELECTOR_OPTION)
        self.page.click(FormaProrabotkaPotrebnosti.POSTAVSHIK_POLE)
        self.page.click(FormaProrabotkaPotrebnosti.SELECTOR_OPTION)
        self.page.click(FormaProrabotkaPotrebnosti.DATE_VIBORA_ODCI)
        self.page.click(FormaProrabotkaPotrebnosti.DATE)
        self.page.click(FormaProrabotkaPotrebnosti.DATE_RAZRABOTKI_KDNO)
        self.page.click(FormaProrabotkaPotrebnosti.DATE)
        self.page.click(FormaProrabotkaPotrebnosti.DATE_SOGLASOVANIYA_KDNO)
        self.page.click(FormaProrabotkaPotrebnosti.DATE)
        self.page.fill(FormaProrabotkaPotrebnosti.COMMENT_ZAKUPKA, "Комментарий к закупке")
        self.page.fill(FormaProrabotkaPotrebnosti.ORIENTIR_CENA, "230")
        time.sleep(1)

    def data_entry_check_after_prorabotka_potrebnosti(self):
        self.scroll_general_table()
        CHECK_ORIENTIR_CENA = self.page.inner_text(FormaProrabotkaPotrebnosti.CHECK_ORIENTIR_CENA)
        CHECK_ORIENTIR_STOIMOST = self.page.inner_text(FormaProrabotkaPotrebnosti.CHECK_ORIENTIR_STOIMOST)
        assert CHECK_ORIENTIR_CENA == "230,00", f'значение в поле "Ориентировочная цена РД" = {CHECK_ORIENTIR_CENA}'
        assert CHECK_ORIENTIR_STOIMOST == "575 000,00", f'значение в поле "Ориентировочную стоимость" = {CHECK_ORIENTIR_STOIMOST}'

    # форма "Контрактация"
    def fill_the_fields_kontraknaciya(self):
        self.page.click(FormaKontraktacii.IZGOTOVITEL)
        self.page.click(FormaKontraktacii.SELECTOR_OPTION)
        self.page.click(FormaKontraktacii.POSTAVSHIK)
        self.page.click(FormaKontraktacii.SELECTOR_OPTION)
        self.page.fill(FormaKontraktacii.NOMER_I_DATA_DOGOVORA_S_POSTAVSHIKOM, "№1 от 20.02.22")
        self.page.fill(FormaKontraktacii.NOMER_I_DATA_SPECIFIKACII_S_POSTAVSHIKOM, "№2 от 24.02.22")
        self.page.fill(FormaKontraktacii.BAZIS_POSTAVKI, "Москва")
        self.page.fill(FormaKontraktacii.NAME_MTR_FAKTICH,"Кирпич лучший")
        self.page.click(FormaKontraktacii.ED_IZM_FAKTICH)
        self.page.click(FormaKontraktacii.SELECTOR_OPTION)
        self.page.fill(FormaKontraktacii.KOEFFICIENT_PERESCHETA, "1")
        self.page.fill(FormaKontraktacii.KOLVO_KONTRAKTACII_FAKTICH, "750")
        self.page.fill(FormaKontraktacii.CENA_KONTRAKTACII_FAKTICH,"200")
        self.page.fill(FormaKontraktacii.COMMENT_ZAKUPKA, "Комментарий закупка")

    def data_entry_check_after_kontraktacii(self):
        self.scroll_general_table()
        CHECK_KOLVO_ZAKONTRAKTOVANO_RD = self.page.inner_text(FormaKontraktacii.CHECK_KOLVO_ZAKONTRAKTOVANO_RD)
        CHECK_PROCENT_KONTRAKTACII_KOLVO = self.page.inner_text(FormaKontraktacii.CHECK_PROCENT_KONTRAKTACII_KOLVO)
        CHECK_ORIENTIROVOCHNAYA_STOIMOST = self.page.inner_text(FormaKontraktacii.CHECK_ORIENTIROVOCHNAYA_STOIMOST)
        CHECK_PROCENT_KONTRAKTACII_STOIMOST = self.page.inner_text(FormaKontraktacii.CHECK_PROCENT_KONTRAKTACII_STOIMOST)
        CHECK_KOEFFICIENT_PERESCHETA = self.page.inner_text(FormaKontraktacii.CHECK_KOEFFICIENT_PERESCHETA)
        CHECK_KOLVO_VSEGO_FAKTICH = self.page.inner_text(FormaKontraktacii.CHECK_KOLVO_VSEGO_FAKTICH)
        CHECK_KOLVO_KONTRAKTACII_FAKTICH = self.page.inner_text(FormaKontraktacii.CHECK_KOLVO_KONTRAKTACII_FAKTICH)
        CHECK_CENA_KONTRAKTACII_FAKTICHESKOE = self.page.inner_text(FormaKontraktacii.CHECK_CENA_KONTRAKTACII_FAKTICHESKOE)
        CHECK_STOIMOST_KONTRAKTACII = self.page.inner_text(FormaKontraktacii.CHECK_STOIMOST_KONTRAKTACII)
        assert CHECK_KOLVO_ZAKONTRAKTOVANO_RD == "750,000", f'значение в поле "кол-во законтрактовано РД" = {CHECK_KOLVO_ZAKONTRAKTOVANO_RD}'
        assert CHECK_PROCENT_KONTRAKTACII_KOLVO == "30,000", f'значение в поле "% контрактации (кол-во)" = {CHECK_PROCENT_KONTRAKTACII_KOLVO}'
        assert CHECK_ORIENTIROVOCHNAYA_STOIMOST == "552 500,00", f'значение в поле "Ориентировочную стоимость (руб. без учета НДС)" = {CHECK_ORIENTIROVOCHNAYA_STOIMOST}'
        assert CHECK_PROCENT_KONTRAKTACII_STOIMOST == "27,15", f'значение в поле "% контрактации (ст-сть)" = {CHECK_PROCENT_KONTRAKTACII_STOIMOST}'
        assert CHECK_KOEFFICIENT_PERESCHETA == "1,000", f'значение в поле "Коэффициент пересчета в фактические ед. изм." = {CHECK_KOEFFICIENT_PERESCHETA}'
        assert CHECK_KOLVO_VSEGO_FAKTICH == "2 500,000", f'значение в поле "Кол-во всего фактическое" = {CHECK_KOLVO_VSEGO_FAKTICH}'
        assert CHECK_KOLVO_KONTRAKTACII_FAKTICH == "750,000", f'значение в поле "Кол-во контрактации фактическое" = {CHECK_KOLVO_KONTRAKTACII_FAKTICH}'
        assert CHECK_CENA_KONTRAKTACII_FAKTICHESKOE == "200,00", f'значение в поле "Цена контрактации фактическая (руб. без учета НДС)" = {CHECK_CENA_KONTRAKTACII_FAKTICHESKOE}'
        assert CHECK_STOIMOST_KONTRAKTACII == "150 000,00", f'значение в поле "Стоимость контрактации (руб. без учета НДС)" = {CHECK_STOIMOST_KONTRAKTACII}'

    # форма "Отгрузка":
    def fill_the_fields_otgruzka(self):
        self.page.click(FormaOtgruzka.DATE_OTGRUZKI)
        self.page.click(FormaOtgruzka.DATE)
        self.page.fill(FormaOtgruzka.NOMER_SCH_F, "№1")
        self.page.click(FormaOtgruzka.DATE_SCH_F)
        self.page.click(FormaOtgruzka.DATE)
        self.page.fill(FormaOtgruzka.NOMER_TTN,"№10")
        self.page.click(FormaOtgruzka.DATE_TTN)
        self.page.click(FormaOtgruzka.DATE)
        self.page.fill(FormaOtgruzka.KOLVO_OTGRUZHENO_FAKTICHESKOE, "370")
        self.page.fill(FormaOtgruzka.COMMENT_ZAKUPKA, "Комментарий к закупке")

    def data_entry_check_after_otgruzka(self):
        self.scroll_general_table()
        CHECK_KOLVO_OTGRUZHENO_RD = self.page.inner_text(FormaOtgruzka.CHECK_KOLVO_OTGRUZHENO_RD)
        CHECK_PROCENT_OTGRUZKI_KOLVO = self.page.inner_text(FormaOtgruzka.CHECK_PROCENT_OTGRUZKI_KOLVO)
        CHECK_STOIMOST_OTGRUZKI = self.page.inner_text(FormaOtgruzka.CHECK_STOIMOST_OTGRUZKI)
        CHECK_PROCENT_OTGRUZKI_STOIMOST = self.page.inner_text(FormaOtgruzka.CHECK_PROCENT_OTGRUZKI_STOIMOST)
        CHECK_KOLVO_OTGRUZHENO_FAKTICH = self.page.inner_text(FormaOtgruzka.CHECK_KOLVO_OTGRUZHENO_FAKTICH)
        CHECK_KOLVO_OTGRUZHENO_BAZOVOE = self.page.inner_text(FormaOtgruzka.CHECK_KOLVO_OTGRUZHENO_BAZOVOE)

        assert CHECK_KOLVO_OTGRUZHENO_RD == "370,000", f'значение в поле "Кол-во отгружено РД" = {CHECK_KOLVO_OTGRUZHENO_RD}'
        assert CHECK_PROCENT_OTGRUZKI_KOLVO == "14,800", f'значение в поле "% отгрузки (кол-во)" = {CHECK_PROCENT_OTGRUZKI_KOLVO}'
        assert CHECK_STOIMOST_OTGRUZKI == "74 000,00", f'значение в поле "Стоимость отгрузки (руб. без учета НДС)" = {CHECK_STOIMOST_OTGRUZKI}'
        assert CHECK_PROCENT_OTGRUZKI_STOIMOST == "13,39", f'значение в поле "% отгрузки (ст-сть)" = {CHECK_PROCENT_OTGRUZKI_STOIMOST}'
        assert CHECK_KOLVO_OTGRUZHENO_FAKTICH == "370,000", f'значение в поле "Кол-во отгружено фактическое" = {CHECK_KOLVO_OTGRUZHENO_FAKTICH}'
        assert CHECK_KOLVO_OTGRUZHENO_BAZOVOE == "370,000", f'значение в поле "Кол-во отгружено базовое" = {CHECK_KOLVO_OTGRUZHENO_BAZOVOE}'

    # форма "Логистика"
    def fill_the_fields_logistika(self):
        self.page.fill(FormaLogistika.PEREVOZCHIK, "Перевозчик")
        self.page.fill(FormaLogistika.VID_POSTAVKI, "Вид поставки")
        self.page.fill(FormaLogistika.MESTO_PEREVALKI, "Место перевалки")
        self.page.click(FormaLogistika.DATA_POSTUPLENIYA_V_PORT)
        self.page.click(FormaLogistika.DATE)
        self.page.fill(FormaLogistika.MASSA, "100")
        self.page.fill(FormaLogistika.GABARITY,"10")
        self.page.fill(FormaLogistika.COMMENT_LOGISTIKA, "Комментарий логистика")

    def data_entry_check_after_logistika(self):
        self.scroll_general_table()
        CHECK_PEREVOZCHICK = self.page.inner_text(FormaLogistika.CHECK_PEREVOZCHICK)
        CHECK_VID_POSTAVKI = self.page.inner_text(FormaLogistika.CHECK_VID_POSTAVKI)
        CHECK_MESTO_PEREVALKI = self.page.inner_text(FormaLogistika.CHECK_MESTO_PEREVALKI)
        CHECK_MASSA = self.page.inner_text(FormaLogistika.CHECK_MASSA)
        CHECK_GABARITY = self.page.inner_text(FormaLogistika.CHECK_GABARITY)
        CHECK_COMMENT_LOGISTIKA = self.page.inner_text(FormaLogistika.CHECK_COMMENT_LOGISTIKA)

        assert CHECK_PEREVOZCHICK == "Перевозчик", f'значение в поле "Перевозчик" = {CHECK_PEREVOZCHICK}'
        assert CHECK_VID_POSTAVKI == "Вид поставки", f'значение в поле "Перевозчик" = {CHECK_VID_POSTAVKI}'
        assert CHECK_MESTO_PEREVALKI == "Место перевалки", f'значение в поле "Место перевалки" = {CHECK_MESTO_PEREVALKI}'
        assert CHECK_MASSA == "100,000", f'значение в поле "Масса за ед., тн" = {CHECK_MASSA}'
        assert CHECK_GABARITY == "10,000", f'значение в поле "Габариты за ед., м3" = {CHECK_GABARITY}'
        assert CHECK_COMMENT_LOGISTIKA == "Комментарий логистика", f'значение в поле "Комментарий логистика" = {CHECK_COMMENT_LOGISTIKA}'

    # форма "Поступление"
    def fill_the_fields_postuplenie(self):
        self.page.fill(FormaPostuplenie.KOLVO_POSTAVLENNOE_FAKTICH, "143")

    def data_entry_check_after_postuplenie(self):
        self.scroll_general_table()
        CHECK_KOLVO_POSTAVLENNOE_RD = self.page.inner_text(FormaPostuplenie.CHECK_KOLVO_POSTAVLENNOE_RD)
        CHECK_PROCENT_POSTAVKI_KOLVO = self.page.inner_text(FormaPostuplenie.CHECK_PROCENT_POSTAVKI_KOLVO)
        CHECK_STOIMOST_POSTAVKI = self.page.inner_text(FormaPostuplenie.CHECK_STOIMOST_POSTAVKI)
        CHECK_PROCENT_POSTAVKI_STOIMOST = self.page.inner_text(FormaPostuplenie.CHECK_PROCENT_POSTAVKI_STOIMOST)
        CHECK_KOLVO_POSTAVLENNOE_FAKTICH = self.page.inner_text(FormaPostuplenie.CHECK_KOLVO_POSTAVLENNOE_FAKTICH)
        CHECK_KOLVO_POSTAVLENNOE_BAZOVOE = self.page.inner_text(FormaPostuplenie.CHECK_KOLVO_POSTAVLENNOE_BAZOVOE)

        assert CHECK_KOLVO_POSTAVLENNOE_RD == "143,000", f'значение в поле "Кол-во поставлено РД" = {CHECK_KOLVO_POSTAVLENNOE_RD}'
        assert CHECK_PROCENT_POSTAVKI_KOLVO == "5,720", f'значение в поле "% поставки (кол-во)" = {CHECK_PROCENT_POSTAVKI_KOLVO}'
        assert CHECK_STOIMOST_POSTAVKI == "28 600,00", f'значение в поле "Cтоимость поставки (руб. без учета НДС)" = {CHECK_STOIMOST_POSTAVKI}'
        assert CHECK_PROCENT_POSTAVKI_STOIMOST == "5,180", f'значение в поле "% поставки (ст-сть)" = {CHECK_PROCENT_POSTAVKI_STOIMOST}'
        assert CHECK_KOLVO_POSTAVLENNOE_FAKTICH == "143,000", f'значение в поле "Кол-во поставленное фактическое" = {CHECK_KOLVO_POSTAVLENNOE_FAKTICH}'
        assert CHECK_KOLVO_POSTAVLENNOE_BAZOVOE == "143,000", f'значение в поле "Кол-во поставленное базовое" = {CHECK_KOLVO_POSTAVLENNOE_BAZOVOE}'

    # форма "Оприходование"
    def fill_the_fields_oprihodovanie(self):
        self.page.click(FormaOprihodovanie.DATA_OPRIHODOVANIYA)
        self.page.click(FormaOprihodovanie.DATE)
        self.page.fill(FormaOprihodovanie.KOLVO_OPRIHODOVANNOE_FAKTICH, "100")
        self.page.fill(FormaOprihodovanie.NOMER_AKTA_VHODNOGO_CONTROL, "№7")
        self.page.click(FormaOprihodovanie.DATA_AKTA_VHODNOGO_CONTROL)
        self.page.click(FormaOprihodovanie.DATE)

    def data_entry_check_after_oprihodovanie(self):
        self.scroll_general_table()
        CHECK_KOLVO_OPRIHODOVANO_RD = self.page.inner_text(FormaOprihodovanie.CHECK_KOLVO_OPRIHODOVANO_RD)
        CHECK_PROCENT_OPRIHODOVANO_KOLVO = self.page.inner_text(FormaOprihodovanie.CHECK_PROCENT_OPRIHODOVANO_KOLVO)
        CHECK_STOIMOST_OPRIHODOVANIE = self.page.inner_text(FormaOprihodovanie.CHECK_STOIMOST_OPRIHODOVANIE)
        CHECK_PROCENT_OPRIHODOVANO_STIOMOST = self.page.inner_text(FormaOprihodovanie.CHECK_PROCENT_OPRIHODOVANO_STIOMOST)
        CHECK_KOLVO_OPRIHODOVANNOE_FAKTICH = self.page.inner_text(FormaOprihodovanie.CHECK_KOLVO_OPRIHODOVANNOE_FAKTICH)
        CHECK_KOLVO_OPRIHODOVANNOE_BAZOVOE = self.page.inner_text(FormaOprihodovanie.CHECK_KOLVO_OPRIHODOVANNOE_BAZOVOE)
        assert CHECK_KOLVO_OPRIHODOVANO_RD == "100,000", f'значение в поле "Кол-во оприходовано РД" = {CHECK_KOLVO_OPRIHODOVANO_RD}'
        assert CHECK_PROCENT_OPRIHODOVANO_KOLVO == "4,000", f'значение в поле "% оприходовано (кол-во)" = {CHECK_PROCENT_OPRIHODOVANO_KOLVO}'
        assert CHECK_STOIMOST_OPRIHODOVANIE == "20 000,00", f'значение в поле "Стоимость оприходовано (руб. без учета НДС)" = {CHECK_STOIMOST_OPRIHODOVANIE}'
        assert CHECK_PROCENT_OPRIHODOVANO_STIOMOST == "3,620", f'значение в поле "% оприходовано (ст-сть)" = {CHECK_PROCENT_OPRIHODOVANO_STIOMOST}'
        assert CHECK_KOLVO_OPRIHODOVANNOE_FAKTICH == "100,000", f'значение в поле "Кол-во оприходованное фактическое" = {CHECK_KOLVO_OPRIHODOVANNOE_FAKTICH}'
        assert CHECK_KOLVO_OPRIHODOVANNOE_BAZOVOE == "100,000", f'значение в поле "Кол-во оприходованное базовое" = {CHECK_KOLVO_OPRIHODOVANNOE_BAZOVOE}'

    # форма "Оприходование"
