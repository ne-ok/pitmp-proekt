import pygame

class Ship:

    def __init__(self, screen):
        """Инициализирует корабль и задает его начальную позицию."""
        self.screen = screen

        # Загрузка изображения корабля и получение прямоугольника.
        self.image = pygame.image.load('C:/Users/kruas/OneDrive/Рабочий стол/LALA/alien_invasion/images/ship.bmp')
        scale_factor = 0.2 # Уменьшение размера в 2 раза.
        new_size = (int(self.image.get_width() * scale_factor), int(self.image.get_height() * scale_factor))
        self.image = pygame.transform.scale(self.image, new_size) # Масштабируем изображение.
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Каждый новый корабль появляется у нижнего края экрана.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Флаги перемещения
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Обновляет позицию корабля с учетом флагов."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += 1
        if self.moving_left and self.rect.left > 0:
            self.rect.centerx -= 1

    def blitme(self):
        """Рисует корабль в текущей позиции."""
        self.screen.blit(self.image, self.rect)