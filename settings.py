class Settings:
    """Класс для хранения всех настроек игры Alien Invasion."""

    def __init__(self):
        """Инициализирует настройки игры."""
        # Параметры экрана
        self.screen_width = 1400
        self.screen_height = 775
        self.bg_color = (255, 255, 255) # Белый фон

        # Настройки корабля
        self.ship_speed_factor = 1 # Скорость корабля (пока без регулировки)

         # Параметры пули
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
