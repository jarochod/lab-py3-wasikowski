import pygame as pg
import os
from random import randrange

# Ścieżka do katalogu z plikami gry
FILES_DIR = os.path.join(os.path.dirname(__file__), "files")

# Stałe
WINDOW = 1000
TILE_SIZE = 50
RANGE = (TILE_SIZE // 2, WINDOW - TILE_SIZE // 2, TILE_SIZE)
FPS = 60
TIME_STEP = 110
FONT_SIZE = 35

# Kolory
GREEN_HEAD = (0, 255, 0) # Jasnozielony dla głowy
DARK_GREEN_BODY = (0, 150, 0) # Ciemniejszy zielony dla ciała


def get_random_position():
    """Generuje losową pozycję dla elementów gry, wyrównaną do siatki."""
    return (randrange(*RANGE), randrange(*RANGE))


# Funkcje ładowania plików
def load_sound(filename):
    """Ładuje plik dźwiękowy. Zwraca obiekt pg.mixer.Sound."""
    return pg.mixer.Sound(os.path.join(FILES_DIR, filename))


def load_highscore():
    """Ładuje najlepszy wynik z pliku. Zwraca 0, jeśli plik nie istnieje lub jest błąd."""
    try:
        with open(os.path.join(FILES_DIR, "highscore.txt"), "r") as f:
            return int(f.read())
    except:
        return 0


def save_highscore(score):
    """Zapisuje najlepszy wynik do pliku."""
    with open(os.path.join(FILES_DIR, "highscore.txt"), "w") as f:
        f.write(str(score))


class Snake:
    """Reprezentuje węża w grze."""
    def __init__(self):
        """Inicjalizuje węża, ustawiając jego początkową pozycję, długość i kierunek."""
        self.rect = pg.Rect(0, 0, TILE_SIZE - 2, TILE_SIZE - 2)
        self.rect.center = get_random_position()
        self.length = 1
        self.segments = [self.rect.copy()]
        self.direction = (0, 0) # Początkowy brak ruchu
        # Słownik kontrolujący możliwość skrętu w danym kierunku, aby zapobiec skrętom o 180 stopni
        self.dirs = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 1, pg.K_d: 1}

    def move(self):
        """Przesuwa węża i aktualizuje jego segmenty."""
        self.rect.move_ip(self.direction)
        # Zapewnia, że wąż owija się wokół ekranu
        self.rect.left %= WINDOW
        self.rect.top %= WINDOW
        self.segments.append(self.rect.copy())
        # Utrzymuje długość węża
        self.segments = self.segments[-self.length:]

    def grow(self):
        """Zwiększa długość węża."""
        self.length += 1

    def reset(self):
        """Resetuje węża do stanu początkowego."""
        self.__init__()

    def draw(self, surface):
        """Rysuje węża na podanej powierzchni. Głowa jest jasnozielona, reszta ciała ciemnozielona."""
        for i, segment in enumerate(self.segments):
            if i == len(self.segments) - 1: # Ostatni segment to głowa
                pg.draw.rect(surface, GREEN_HEAD, segment)
            else: # Pozostałe segmenty to ciało
                pg.draw.rect(surface, DARK_GREEN_BODY, segment)

    def check_collision(self):
        """Sprawdza kolizję głowy węża z własnym ciałem. Zwraca True w przypadku kolizji."""
        return self.rect.collidelist(self.segments[:-1]) != -1

    def set_direction(self, key):
        """Ustawia kierunek ruchu węża na podstawie naciśniętego klawisza."""
        if key == pg.K_w and self.dirs[pg.K_w]:
            self.direction = (0, -TILE_SIZE)
            self.dirs = {pg.K_w: 1, pg.K_s: 0, pg.K_a: 1, pg.K_d: 1}
        elif key == pg.K_s and self.dirs[pg.K_s]:
            self.direction = (0, TILE_SIZE)
            self.dirs = {pg.K_w: 0, pg.K_s: 1, pg.K_a: 1, pg.K_d: 1}
        elif key == pg.K_a and self.dirs[pg.K_a]:
            self.direction = (-TILE_SIZE, 0)
            self.dirs = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 1, pg.K_d: 0}
        elif key == pg.K_d and self.dirs[pg.K_d]:
            self.direction = (TILE_SIZE, 0)
            self.dirs = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 0, pg.K_d: 1}


class Food:
    """Reprezentuje jedzenie dla węża."""
    def __init__(self):
        """Inicjalizuje jedzenie, ustawiając jego początkową pozycję."""
        self.rect = pg.Rect(0, 0, TILE_SIZE - 2, TILE_SIZE - 2)
        self.rect.center = get_random_position()

    def respawn(self, occupied_positions):
        """Odradza jedzenie w nowej, losowej pozycji, która nie jest zajęta przez węża."""
        while True:
            new_pos = get_random_position()
            # Sprawdza, czy nowa pozycja nie koliduje z wężem
            if new_pos not in occupied_positions:
                self.rect.center = new_pos
                break

    def draw(self, surface):
        """Rysuje jedzenie na podanej powierzchni."""
        pg.draw.rect(surface, 'red', self.rect)


class Game:
    """Główna klasa gry, zarządzająca logiką, renderowaniem i zdarzeniami."""
    def __init__(self):
        """Inicjalizuje PyGame, okno gry, obiekty węża i jedzenia, a także zmienne gry."""
        pg.init()
        pg.mixer.init() # Inicjalizacja miksera dla dźwięków
        self.screen = pg.display.set_mode([WINDOW] * 2)
        pg.display.set_caption("Snake Game")
        self.clock = pg.time.Clock()
        self.snake = Snake()
        self.food = Food()
        self.time = 0 # Czas używany do kontroli aktualizacji ruchu węża
        self.running = True # Czy gra jest uruchomiona
        self.paused = False # Czy gra jest spauzowana
        self.score = 0 # Aktualny wynik
        self.highscore = load_highscore() # Najlepszy wynik
        self.font = pg.font.SysFont('Arial', FONT_SIZE, True) # Czcionka do wyświetlania tekstu
        self.snd_eat = load_sound("eat.mp3") # Dźwięk po zjedzeniu jedzenia
        self.snd_gameover = load_sound("gameover.mp3") # Dźwięk po przegranej
        self.game_over = False # Czy gra się zakończyła

    def run(self):
        """Główna pętla gry."""
        while self.running:
            self.handle_events() # Obsługuje zdarzenia użytkownika
            if not self.paused and not self.game_over:
                self.update() # Aktualizuje stan gry
            self.draw() # Rysuje elementy gry na ekranie
            self.clock.tick(FPS) # Kontroluje liczbę klatek na sekundę

    def handle_events(self):
        """Obsługuje zdarzenia PyGame, takie jak wyjście, naciśnięcia klawiszy."""
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False # Zamyka grę po kliknięciu 'X'
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.running = False # Zamyka grę po naciśnięciu ESC
                elif event.key == pg.K_r:
                    self.reset() # Resetuje grę po naciśnięciu 'R'
                elif event.key == pg.K_p:
                    self.paused = not self.paused # Przełącza pauzę po naciśnięciu 'P'
                elif not self.paused and not self.game_over:
                    self.snake.set_direction(event.key) # Zmienia kierunek węża

    def update(self):
        """Aktualizuje logikę gry, taką jak ruch węża, kolizje, jedzenie."""
        now = pg.time.get_ticks()
        if now - self.time > TIME_STEP: # Kontroluje szybkość ruchu węża
            self.time = now
            self.snake.move()

            if self.snake.check_collision():
                self.snd_gameover.play()
                self.game_over = True
                if self.score > self.highscore:
                    self.highscore = self.score
                    save_highscore(self.highscore) # Zapisuje nowy najlepszy wynik

            if self.snake.rect.center == self.food.rect.center:
                self.snake.grow() # Wąż rośnie
                self.score += 1 # Zwiększa wynik
                self.snd_eat.play()
                # Generuje nową pozycję dla jedzenia, upewniając się, że nie jest na wężu
                occupied = [segment.center for segment in self.snake.segments]
                self.food.respawn(occupied)

    def reset(self):
        """Resetuje stan gry po zakończeniu gry."""
        self.snake.reset()
        occupied = [segment.center for segment in self.snake.segments]
        self.food.respawn(occupied)
        self.score = 0
        self.game_over = False
        self.paused = False

    def draw(self):
        """Rysuje wszystkie elementy gry na ekranie."""
        self.screen.fill('black') # Czyści ekran czarnym kolorem
        self.snake.draw(self.screen) # Rysuje węża
        self.food.draw(self.screen) # Rysuje jedzenie
        self.draw_text(f"Score: {self.score}", 10, 10) # Wyświetla aktualny wynik
        self.draw_text(f"Highscore: {self.highscore}", 10, 50) # Wyświetla najlepszy wynik
        if self.paused:
            self.draw_centered_text("PAUZA\nP - Wznów | R - Restart | ESC - Wyjdź")
        elif self.game_over:
            self.draw_centered_text("KONIEC GRY\nR - Restart | ESC - Wyjdź")
        pg.display.flip() # Odświeża cały ekran

    def draw_text(self, text, x, y):
        """Rysuje tekst na ekranie w podanej pozycji."""
        surface = self.font.render(text, True, 'white')
        self.screen.blit(surface, (x, y))

    def draw_centered_text(self, text):
        """Rysuje tekst wyśrodkowany na ekranie. Obsługuje wiele linii tekstu."""
        lines = text.split("\n")
        for i, line in enumerate(lines):
            surface = self.font.render(line, True, 'red')
            rect = surface.get_rect(center=(WINDOW // 2, WINDOW // 2 + i * FONT_SIZE))
            self.screen.blit(surface, rect)


if __name__ == '__main__':
    game = Game()
    game.run()
    pg.quit() # Inicjalizacja PyGame