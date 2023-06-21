from selenium.common import ElementClickInterceptedException, NoSuchElementException

from pages.Locators import PicturePageLocators, PicturePageData
from pages.base_page import BasePage


class PicturePage(BasePage):
    """ Клас проверки работы с изображениями в Яндекс """
    def should_by_menu(self):
        """ Проверка наличия меню "Все сервисы" и его активация """
        try:
            self.send_text(*PicturePageLocators.BUTTON_MENU_ALL)
            self.button_click(*PicturePageLocators.BUTTON_MENU_ALL)
            print('\nМеню "Все сервисы": ОК')
        except (ElementClickInterceptedException, NoSuchElementException):
            raise AssertionError('Меню отсутствует или не активно')

    def menu_picture_click(self):
        """ Выбор меню "Картинки" """
        assert self.is_element_present(*PicturePageLocators.BUTTON_MENU_PICTURE), 'Меню картинки отсутствует'
        self.button_click(*PicturePageLocators.BUTTON_MENU_PICTURE)
        print('\nМеню картинки выбрано')

    def should_be_result_search_url(self):
        """ Проверка страницы работы с изображениями """
        assert self.is_url_respond(PicturePageData.PATTERN_URL), "URL адрес несоответствует"
        print('\nПереход на url https://yandex.ru/images/: OK')

    def open_first_picture_group(self):
        """" Открытие первой категории изображения и получение её имени """
        assert self.is_element_present(*PicturePageLocators.NAME_FIRST_PICTURE_GROUP), 'Категории изображения отсутствуют'
        self.compare_name_group = self.get_attr(*PicturePageLocators.NAME_FIRST_PICTURE_GROUP, 'data-grid-text')
        self.button_click(*PicturePageLocators.FIRST_PICTURE_GROUP)
        print('\nПервая категории изображения открывается')

    def should_by_category_name_in_text_field(self):
        """ Проверка вывода наименование категории """
        assert self.get_attr(*PicturePageLocators.INPUT_FIELD,
                             'value') == self.compare_name_group, 'Наименование категории не соответствует'
        print('\nНаименование категории выводится')

    def select_window(self, count):
        """ Переключение на окно """
        new_window = self.browser.window_handles[count]
        self.browser.switch_to.window(new_window)

    def open_first_picture(self):
        """ Открытие первой картинки """
        assert self.is_element_present(*PicturePageLocators.FIRST_PICTURE), 'Изображение отсутствует'
        self.button_click(*PicturePageLocators.FIRST_PICTURE)

    def should_by_picture(self):
        """ Проверка открытия изображения """
        assert self.is_element_present(*PicturePageLocators.PICTURE), 'Изображение не открылась'
        print('\nИзображение открыто')

    def get_src_picture(self):
        """ Получение ссылки на изображение """
        self.compare_picture = self.get_attr(*PicturePageLocators.PICTURE, 'src')
        print('\nУказатель на первое изображение сохранен')

    def next_picture(self):
        """ Переход к следующему изображению """
        assert self.is_element_present(
            *PicturePageLocators.BUTTON_NEXT), 'Кнопка перехода на следующее изображение отсутствует'
        self.button_click(*PicturePageLocators.BUTTON_NEXT)

    def should_by_change_picture(self):
        """ Проверка изменения изображения """
        self.should_by_picture()
        assert self.get_attr(*PicturePageLocators.PICTURE, 'src') != self.compare_picture, 'Изображения совпадают'
        print('\nИзображение сменилось')

    def prev_picture(self):
        """ Переход к предыдущему изображению """
        assert self.is_element_present(
            *PicturePageLocators.BUTTON_PREV), 'Кнопка перехода на предыдущее изображение отсутствует'
        self.button_click(*PicturePageLocators.BUTTON_PREV)

    def should_by_same_picture(self):
        """ Проверка совпадения изображения  """
        self.should_by_picture()
        assert self.get_attr(*PicturePageLocators.PICTURE, 'src') == self.compare_picture, 'Изображения не совпадают'
        print('\nИзображение совпадает с первым')
