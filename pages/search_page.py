from pages.Locators import SearchPageLocators, SearchPageData
from pages.base_page import BasePage


class SearchPage(BasePage):
    """ Класс для проверки поиска в яндекс """
    def should_be_search_field(self):
        """ Проверка наличия поля поиска Яндекс"""
        assert self.is_element_present(*SearchPageLocators.SEARCH_FIELD), "Поле поиска отсутствует"
        print('\nПоле поиска найдено')

    def should_be_hint_table(self):
        """ Проверка появления таблицы с подсказками (suggest) для строки поиска Яндекс  """
        assert self.is_element_present(*SearchPageLocators.SEARCH_HINT_TABLE), "Таблица с подсказками отсутствует"
        print('\nТаблицы с подсказками (suggest): OK')

    def should_be_result_search_url(self):
        """ Проверка появления заданной страницы поиска Яндекса """
        assert self.is_url_respond(SearchPageData.URL_RESULT_SEARCH), "URL адрес несоответствует"
        print('\nСтраница поиска: OK')

    def send_search_text(self):
        """ Ввод текста в заданное поле """
        self.send_text(*SearchPageLocators.SEARCH_FIELD, text=SearchPageData.SEARCH_TEXT)

    def button_search_click(self):
        """ Метод активации объекта """
        self.button_click(*SearchPageLocators.BUTTON_SEARCH)
        print('\nПоиска запроса по ключевому слову "Тензор" запущен')

    def should_be_url(self):
        """ Метод проверки соответствия ссылки """
        assert self.get_attr(*SearchPageLocators.ONE_URL_SEARCH_RESULT,
                             SearchPageData.GET_ATTR_FROM_URL) == SearchPageData.PATTERN_URL, "Cсылка на сайт tensor.ru отсутствует"
        print('\nСсылка на сайт tensor.ru: ОК')
