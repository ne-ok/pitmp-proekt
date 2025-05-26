import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Класс для управления пулями."""
    def __init__(self, ai_settings, screen, ship):
        """Создает объект пули в текущей позиции корабля."""
        super(Bullet, self).__init__()
        self.screen = screen # Экран, на котором рисуется пуля

        # Создание пули в позиции (0,0) и назначение правильной позиции.
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height) # Создаем прямоугольник пули
        self.rect.centerx = ship.rect.centerx # Устанавливаем координату x пули в центр корабля
        self.rect.top = ship.rect.top # Устанавливаем координату y пули в верхнюю часть корабля

        # Позиция пули хранится в вещественном формате.
        self.y = float(self.rect.y) # Сохраняем координату y пули в виде числа с плавающей точкой
        self.color = ai_settings.bullet_color # Устанавливаем цвет пули из настроек
        self.speed_factor = ai_settings.bullet_speed_factor # Устанавливаем скорость пули из настроек
    def update(self):
        """Перемещает пулю вверх по экрану."""
        # Обновление позиции пули в вещественном формате.
        self.y -= self.speed_factor # Обновляем координату y пули

        # Обновление позиции прямоугольника.
        self.rect.y = self.y # Обновляем координату y прямоугольника пули
    def draw_bullet(self):
        """Рисует пулю на экране."""
        pygame.draw.rect(self.screen, self.color, self.rect) # Рисуем прямоугольник пули на экране
