import pygame.font


class Button():
    """Класс для создания кнопок."""
    def __init__(self, ai_settings, screen, msg):
        """Инициализирует атрибуты кнопки."""
        self.screen = screen # Экран, на котором рисуется кнопка
        self.screen_rect = screen.get_rect() # Получаем прямоугольник экрана

        # Назначение размеров и свойств кнопок.
        self.width, self.height = 200, 50 # Ширина и высота кнопки
        self.button_color = (0, 255, 0) # Цвет кнопки (зеленый)
        self.text_color = (255, 255, 255) # Цвет текста (белый)
        self.font = pygame.font.SysFont(None, 48) # Шрифт текста

        # Построение объекта rect кнопки и выравнивание по центру экрана.
        self.rect = pygame.Rect(0, 0, self.width, self.height) # Создаем прямоугольник кнопки
        self.rect.center = self.screen_rect.center # Выравниваем кнопку по центру экрана

        # Сообщение кнопки создается только один раз.
        self.prep_msg(msg) # Подготавливаем сообщение для отображения

    def prep_msg(self, msg):
        """Преобразует msg в прямоугольник и выравнивает текст по центру."""
        self.msg_image = self.font.render(msg, True, self.text_color, # Создаем поверхность с текстом
        self.button_color)
        self.msg_image_rect = self.msg_image.get_rect() # Получаем прямоугольник поверхности с текстом
        self.msg_image_rect.center = self.rect.center # Выравниваем текст по центру кнопки
    def draw_button(self):
        """Отображает пустую кнопку и выводит сообщение."""
        # Отображение пустой кнопки и вывод сообщения.
        self.screen.fill(self.button_color, self.rect) # Заполняем кнопку цветом
        self.screen.blit(self.msg_image, self.msg_image_rect) # Отображаем текст на кнопке