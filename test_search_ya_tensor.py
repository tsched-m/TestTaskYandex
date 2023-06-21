from time import sleep

from pages.picture_page import PicturePage
from pages.search_page import SearchPage


def test_search_ya_tensor(browser):
    """ Тест-кейс проверка поиска в Яндекс """
    print('\nПроверка поиска в Яндекс: запущена')
    link = "https://ya.ru"
    search_page = SearchPage(browser, link)
    search_page.open()
    search_page.should_be_search_field()
    search_page.send_search_text()
    search_page.should_be_hint_table()
    search_page.button_search_click()
    search_page.should_be_result_search_url()
    search_page.should_be_url()
    print('\nПроверка поиска в Яндекс: пройдена')


def test_work_picture(browser):
    """ Тест-кейс проверка работы с изображением Яндекс """
    link = "https://ya.ru"
    print('\nПроверка работы с изображениями Яндекс: запущена')
    picture_page = PicturePage(browser, link)
    picture_page.open()
    picture_page.should_by_menu()
    picture_page.menu_picture_click()
    picture_page.select_window(1)
    picture_page.open_first_picture_group()
    picture_page.should_by_category_name_in_text_field()
    picture_page.open_first_picture()
    picture_page.should_by_picture()
    picture_page.get_src_picture()
    picture_page.next_picture()
    picture_page.should_by_change_picture()
    picture_page.prev_picture()
    picture_page.should_by_same_picture()
    print('\nПроверка работы с изображениями Яндекс: пройдена')
