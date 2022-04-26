class AuthPageLocators():
    LOGIN_INPUT = "input.mdc-text-field__input"
    PASSWORD_INPUT = 'input.mdc-text-field__input[type="password"]'
    BUTTON_AUTH = "button.mdc-button.mdc-button--raised"


class ProjectsPageLocators():
    TITLE_NAME = "div.projects-page-title"
    BUTTON_EDIT_PROJECTS = "//html/body/div[2]/div/header/div/section[1]/div/button[4]/div"
    BUTTON_ADD_PROJECT = "div.projects-page-add-control"
    CHECK_COUNT_PROJECT_EDIT_CARD = "div.project-card.mdc-elevation--z3"
    COUNT_PROJECT_CARD = "div.project-card.clickable"
    BUTTON_ADD_DICTIONARIES = "//html/body/div[1]/div/div/div[1]/div[2]/div[1]/button/div"
    ADD_DICT = "input.mdc-checkbox__native-control"
    SEARCH_FIELD = "input.mdc-text-field__input"
    NAME_NEW_PROJECT = "div#modals span.mdc-text-field__ripple"
    CREATE_PROJECT_BUTTON = "div#modals div.mdc-button__ripple >> nth=1"


class SheetPageLocators():
    BUTTON_ADD_POTREBNOST = "div.nav-buttons div.mdc-button__ripple"
    UPLOAD_FILES = "div.modal-tooltip input"
    NAME_PROJECT = "h4.header-view__title"
    BUTTON_VNESTI_IN_FORMA = "text=Внести"
    FORMA_PRORABOKTA_POTREBNOSTI = "//html/body/div[2]/div/header/div/section[2]/div/div[2]/button/div"
    BUTTON_RASSCHITAT_IN_FORMA = 'button:has-text("Рассчитать")'


class FormaProrabotkaPotrebnosti():
    BUTTON_PRORABOTKA = "div.nav-buttons div.mdc-button__ripple >> nth=1"
    MODAL_WINDOW = "div.modal-tooltip-content"
    PID_BUTTON = "//html/body/div[1]/div/div/div[1]/div[2]/div/div[2]/table/thead/tr/th[1]/div/button"
    PID = '//*[@id="toggle--А.3"]'
    BUTTON_ADD_PID = "div.pids-flex button"
    GENPODRYADCHICK = "td.form-cell.--select"
    SELECTOR_OPTION = "div.react-select__menu div.react-select__option >> nth=0"
    DATEPICKER_1 = "div.react-datepicker__input-container"
    DATEPICKER_2 = "div.react-datepicker__input-container"
    DATE = "div.react-datepicker div.react-datepicker__day--005"
    IZGOTOVITEL_POLE = "//html/body/div[1]/div/div/div[1]/div[2]/div/div[2]/table/tbody/tr/td[6]/div/div/div[1]/div[1]/div[2]"
    POSTAVSHIK_POLE = "//html/body/div[1]/div/div/div[1]/div[2]/div/div[2]/table/tbody/tr/td[7]/div/div/div[1]"
    DATE_VIBORA_ODCI = "//html/body/div[1]/div/div/div[1]/div[2]/div/div[2]/table/tbody/tr/td[8]/div/div[1]/div/label/input"
    DATE_RAZRABOTKI_KDNO = "//html/body/div[1]/div/div/div[1]/div[2]/div/div[2]/table/tbody/tr/td[9]/div/div[1]/div/label/input"
    DATE_SOGLASOVANIYA_KDNO = "//html/body/div[1]/div/div/div[1]/div[2]/div/div[2]/table/tbody/tr/td[10]/div/div[1]/div/label/input"
    COMMENT_ZAKUPKA = "//html/body/div[1]/div/div/div[1]/div[2]/div/div[2]/table/tbody/tr/td[11]/div/label/input"
    ORIENTIR_CENA = "//html/body/div[1]/div/div/div[1]/div[2]/div/div[2]/table/tbody/tr/td[12]/div/label/input"
    CHECK_ORIENTIR_CENA = "div.table-board-td >> nth=49"
    CHECK_ORIENTIR_STOIMOST = "div.table-board-td >> nth=50"


class FormaKontraktacii():
    SELECTOR_OPTION = "div.react-select__menu div.react-select__option >> nth=0"
    IZGOTOVITEL = "div.react-select__value-container"
    POSTAVSHIK = "div.react-select__value-container >> nth = 1"
    NOMER_I_DATA_DOGOVORA_S_POSTAVSHIKOM = "input.mdc-text-field__input"
    NOMER_I_DATA_SPECIFIKACII_S_POSTAVSHIKOM = "input.mdc-text-field__input >> nth = 1"
    BAZIS_POSTAVKI = "input.mdc-text-field__input >> nth = 2"
    NAME_MTR_FAKTICH = "input.mdc-text-field__input >> nth = 3"
    ED_IZM_FAKTICH = "div.react-select__value-container >> nth = 2"
    KOEFFICIENT_PERESCHETA = "input.mdc-text-field__input >> nth = 4"
    KOLVO_KONTRAKTACII_FAKTICH = "input.mdc-text-field__input >> nth = 5"
    CENA_KONTRAKTACII_FAKTICH = "input.mdc-text-field__input >> nth = 6"
    COMMENT_ZAKUPKA = "input.mdc-text-field__input >> nth = 7"
    CHECK_KOLVO_ZAKONTRAKTOVANO_RD = "div.table-board-td >> nth=44"
    CHECK_PROCENT_KONTRAKTACII_KOLVO = "div.table-board-td >> nth=51"
    CHECK_ORIENTIROVOCHNAYA_STOIMOST = "div.table-board-td >> nth=50"
    CHECK_PROCENT_KONTRAKTACII_STOIMOST = "div.table-board-td >> nth=52"
    CHECK_KOLVO_VSEGO_FAKTICH = "div.table-board-td >> nth=17"
    CHECK_KOLVO_KONTRAKTACII_FAKTICH = "div.table-board-td >> nth=45"
    CHECK_CENA_KONTRAKTACII_FAKTICHESKOE = "div.table-board-td >> nth=47"
    CHECK_STOIMOST_KONTRAKTACII = "div.table-board-td >> nth=48"
    CHECK_KOEFFICIENT_PERESCHETA = "div.table-board-td >> nth=16"

class FormaOtgruzka():
    DATE = "div.react-datepicker div.react-datepicker__day--005"
    DATE_OTGRUZKI = "input.mdc-text-field__input"
    NOMER_SCH_F = "input.mdc-text-field__input >> nth= 1"
    DATE_SCH_F = "input.mdc-text-field__input >> nth= 2"
    NOMER_TTN = "input.mdc-text-field__input >> nth= 3"
    DATE_TTN = "input.mdc-text-field__input >> nth= 4"
    KOLVO_OTGRUZHENO_FAKTICHESKOE = "input.mdc-text-field__input >> nth= 5"
    COMMENT_ZAKUPKA = "input.mdc-text-field__input >> nth = 6"
    CHECK_KOLVO_OTGRUZHENO_RD = "div.table-board-td >> nth=54"
    CHECK_PROCENT_OTGRUZKI_KOLVO = "div.table-board-td >> nth=58"
    CHECK_STOIMOST_OTGRUZKI = "div.table-board-td >> nth=57"
    CHECK_PROCENT_OTGRUZKI_STOIMOST = "div.table-board-td >> nth=59"
    CHECK_KOLVO_OTGRUZHENO_FAKTICH = "div.table-board-td >> nth=55"
    CHECK_KOLVO_OTGRUZHENO_BAZOVOE = "div.table-board-td >> nth=56"

