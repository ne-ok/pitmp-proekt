class Settings:
    """Класс для хранения всех настроек игры Alien Invasion."""

    def __init__(self):
        """Инициализирует настройки игры."""
        # Параметры экрана
        self.screen_width = 1400
        self.screen_height = 775
        self.bg_color = (230, 230, 230)  # Светло-серый фон

        # Настройки корабля
        self.ship_speed_factor = 1  # Скорость корабля

        # Параметры пули
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Параметры пришельцев
        self.alien_speed_factor = 1  # Скорость пришельцев
        self.fleet_drop_speed = 10  # Насколько опускается флот при смене направления
        self.fleet_direction = 1    # 1 - движение вправо, -1 - влево

        self.alien_speed_factor = 0.5  # уменьшили скорость пришельцев
        self.fleet_direction = 1  # направление движения флота (1 — вправо, -1 — влево)
        self.fleet_drop_speed = 10  # скорость опускания флота вниз
