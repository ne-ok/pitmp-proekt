import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Класс, представляющий одного пришельца."""
    def __init__(self, ai_settings, screen):
        """Инициализирует пришельца и задает его начальную позицию."""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load('C:/Users/kruas/OneDrive/Рабочий стол/LALA/alien_invasion/images/alien.bmp')
        self.image = pygame.transform.scale(self.image, (50, 50))  # Изменение размера изображения
        self.rect = self.image.get_rect()
        self.x = float(self.rect.x)
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.y = float(self.rect.y)

    def blitme(self):
        """Выводит пришельца в текущем положении."""
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """Возвращает True, если пришелец находится у края экрана."""
        screen_rect = self.screen.get_rect()
        return self.rect.right >= screen_rect.right or self.rect.left <= 0

    def update(self):
        """Перемещает пришельца влево или вправо в зависимости от направления флота."""
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x
