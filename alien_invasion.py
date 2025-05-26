import sys
import pygame
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
from alien import Alien
import game_functions as gf
from pygame.sprite import Group

# Запуск основного цикла игры.
def run_game():
    pygame.init() # Инициализация pygame
    ai_settings = Settings() # Создание экземпляра Settings
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)) # Создание окна
    pygame.display.set_caption("Alien Invasion") # Устанавливает заголовок окна

    # Создание кнопки Play.
    play_button = Button(ai_settings, screen, "Play") # Создание кнопки Play

    # Создание экземпляров GameStats и Scoreboard.
    stats = GameStats(ai_settings) # Создает экземпляр GameStats
    sb = Scoreboard(ai_settings, screen, stats) # Создает экземпляр Scoreboard

    # Создание корабля.
    ship = Ship(ai_settings,screen) # Создает корабль

    # Создание группы для хранения пуль.
    bullets = Group() # Создает группу для пуль

    # Создание пришельцев
    aliens = Group() # Создает группу для пришельцев

    # Создание флота пришельцев.
    gf.create_fleet(ai_settings, screen, ship, aliens) # Создает флот пришельцев
    while True: # Основной цикл игры

        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets) # Обрабатывает события
        if stats.game_active: # Если игра активна
            
            ship.update() # Обновляет положение корабля
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets) # Обновляет положение пуль
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets) # Обновляет положение пришельцев
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button) # Обновляет экран


run_game( ) # Запускает игру
