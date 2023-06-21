from selenium.webdriver.common.by import By


class SearchPageLocators:
    """ Локаторы поиска элементов на странице """
    SEARCH_FIELD = (By.CSS_SELECTOR, "#text")
    SEARCH_HINT_TABLE = (By.CSS_SELECTOR, ".mini-suggest__popup-content > li")
    BUTTON_SEARCH = (By.CSS_SELECTOR, "button[type='submit']")
    ONE_URL_SEARCH_RESULT = (By.CSS_SELECTOR, 'li[data-cid="0"] a[accesskey="1"]')


class SearchPageData:
    """ Данные для проверки """
    SEARCH_TEXT = 'Тензор'
    URL_RESULT_SEARCH = 'search'
    GET_ATTR_FROM_URL = 'href'
    PATTERN_URL = r'https://tensor.ru/'


class PicturePageLocators:
    """ Локаторы поиска элементов на странице """
    BUTTON_MENU_ALL = (By.CSS_SELECTOR, 'a[title="Все сервисы"]')
    BUTTON_MENU_PICTURE = (By.CSS_SELECTOR, 'a[aria-label="Картинки"]')
    FIRST_PICTURE_GROUP = (By.CSS_SELECTOR, 'div.PopularRequestList > div:first-child > a')
    NAME_FIRST_PICTURE_GROUP = (By.CSS_SELECTOR, 'div.PopularRequestList:first-child > div:first-child')
    INPUT_FIELD = (By.CSS_SELECTOR, 'input[name="text"]')
    FIRST_PICTURE = (By.CSS_SELECTOR, 'div.justifier__item_first > div > a')
    PICTURE = (By.CSS_SELECTOR, 'img.MMImage-Preview')
    BUTTON_NEXT = (By.CSS_SELECTOR, 'div.CircleButton_type_next > i')
    BUTTON_PREV = (By.CSS_SELECTOR, 'div.CircleButton_type_prev > i')


class PicturePageData:
    """ Данные для проверки """
    PATTERN_URL = r'https://yandex.ru/images/'
