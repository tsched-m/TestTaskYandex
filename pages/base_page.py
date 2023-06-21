from selenium.common import NoSuchElementException


class BasePage:
    def __init__(self, browser, url, timeout=20):
        self.browser = browser
        self.url = url
        self.compare_name_group = None
        self.compare_picture = None
        self.browser.implicitly_wait(timeout)

    def open(self):
        """ Метод открытия браузера """
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        """ Метод проверки наличия элемента """
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def send_text(self, how, what, text=''):
        """ Метод отправки текста """
        field_text = self.browser.find_element(how, what)
        field_text.send_keys(text)

    def button_click(self, how, what):
        """ Метод активации объекта """
        button = self.browser.find_element(how, what)
        button.click()

    def is_url_respond(self, pattern):
        """ Метод проверки текущего URL на соответствие шаблону """
        current_url = self.browser.current_url
        if pattern in current_url:
            return True
        return False

    def get_attr(self, how, what, attr):
        """ Метод получения заданного атрибута """
        element = self.browser.find_element(how, what)
        return element.get_attribute(attr)
