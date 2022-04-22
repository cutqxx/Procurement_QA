

class AuthPageLocators():
    LOGIN_INPUT = "input.mdc-text-field__input"
    PASSWORD_INPUT = 'input.mdc-text-field__input[type="password"]'
    BUTTON_AUTH = "button.mdc-button.mdc-button--raised"


class BasePageLocators():
    LOGIN_INPUT = "input.mdc-text-field__input"


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



class FormaProrabotkaPotrebnosti():
    BUTTON_PRORABOTKA = "div.nav-buttons div.mdc-button__ripple >> nth=1"
    MODAL_WINDOW = "div.modal-tooltip-content"
    PID_BUTTON = "//html/body/div[1]/div/div/div[1]/div[2]/div/div[2]/table/thead/tr/th[1]/div/button"
    PID = '//*[@id="toggle--А.3"]'
    BUTTON_ADD_PID = "div.pids-flex button"
    GENPODRYADCHICK = "//html/body/div[1]/div/div/div[1]/div[2]/div/div[2]/table/tbody/tr/td[4]/div/div/div[1]/div[1]/div[2]"
    GENPODRYADCHICK_OPTION = "id=react-select-2-option-0"
    DATEPICKER_1 = "div.react-datepicker__input-container"
    DATEPICKER_2 = "div.react-datepicker__input-container"
    DATE = "div.react-datepicker div.react-datepicker__day--005"
    IZGOTOVITEL_POLE = "//html/body/div[1]/div/div/div[1]/div[2]/div/div[2]/table/tbody/tr/td[6]/div/div/div[1]/div[1]/div[2]"
    IZGOTOVITEL_OPTION = "id=react-select-3-option-0"
    POSTAVSHIK_POLE = "//html/body/div[1]/div/div/div[1]/div[2]/div/div[2]/table/tbody/tr/td[7]/div/div/div[1]"
    POSTAVSHIK_OPTION = "id=react-select-4-option-0"
    DATE_VIBORA_ODCI = "//html/body/div[1]/div/div/div[1]/div[2]/div/div[2]/table/tbody/tr/td[8]/div/div[1]/div/label/input"
    DATE_RAZRABOTKI_KDNO = "//html/body/div[1]/div/div/div[1]/div[2]/div/div[2]/table/tbody/tr/td[9]/div/div[1]/div/label/input"
    DATE_SOGLASOVANIYA_KDNO = "//html/body/div[1]/div/div/div[1]/div[2]/div/div[2]/table/tbody/tr/td[10]/div/div[1]/div/label/input"
    COMMENT_ZAKUPKA = "//html/body/div[1]/div/div/div[1]/div[2]/div/div[2]/table/tbody/tr/td[11]/div/label/input"
    ORIENTIR_CENA = "//html/body/div[1]/div/div/div[1]/div[2]/div/div[2]/table/tbody/tr/td[12]/div/label/input"