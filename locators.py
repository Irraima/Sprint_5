class Locators:
    LOGO = ".//div[@class = 'AppHeader_header__logo__2D0X2']"
    NAME_INPUT = ".//label[text() = 'Имя']/parent::*/input"
    EMAIL_INPUT = ".//label[text() = 'Email']/parent::*/input"
    PASSWORD_INPUT = ".//label[text() = 'Пароль']/parent::*/input"
    PASSWORD_ERROR = ".//p[text() = 'Некорректный пароль']"
    LOGIN_BUTTON = ".//button[text() = 'Войти']"
    ALT_LOGIN_BUTTON = ".//a[text() = 'Войти']"
    LOGOUT_BUTTON = ".//button[text() = 'Выход']"
    LOGIN_AC_BUTTON = ".//button[text() = 'Войти в аккаунт']"
    AC_BUTTON = ".//p[text() = 'Личный Кабинет']"
    RES_PASS_BUTTON = ".//a[text() = 'Восстановить пароль']"
    REG_BUTTON = ".//button[text() = 'Зарегистрироваться']"
    ALT_REG_BUTTON = ".//a[text() = 'Зарегистрироваться']"
    CONST_BUTTON = ".//p[text() = 'Конструктор']"
    BUN_ACTIVE = ".//div[1][contains(@class, 'type_current')]"
    BUN = ".//span[text() = 'Булки']"
    SAUCE_ACTIVE = ".//div[2][contains(@class, 'type_current')]"
    SAUCE = ".//span[text() = 'Соусы']"
    FILLING_ACTIVE = ".//div[3][contains(@class, 'type_current')]"
    FILLING = ".//span[text() = 'Начинки']"

