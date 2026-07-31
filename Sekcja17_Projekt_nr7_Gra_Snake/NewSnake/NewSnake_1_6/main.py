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


def get_random_position():
    return (randrange(*RANGE), randrange(*RANGE))


def load_sound(filename):
    return pg.mixer.Sound(os.path.join(FILES_DIR, filename))


def load_highscore():
    try:
        with open(os.path.join(FILES_DIR, "highscore.txt"), "r") as f:
            return int(f.read())
    except:
        return 0


def save_highscore(score):
    with open(os.path.join(FILES_DIR, "highscore.txt"), "w") as f:
        f.write(str(score))


class Snake:
    def __init__(self):
        self.rect = pg.Rect(0, 0, TILE_SIZE - 2, TILE_SIZE - 2)
        self.rect.center = get_random_position()
        self.length = 1
        self.segments = [self.rect.copy()]
        self.direction = (0, 0)
        self.dirs = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 1, pg.K_d: 1}

    def move(self):
        self.rect.move_ip(self.direction)
        self.rect.left %= WINDOW
        self.rect.top %= WINDOW
        self.segments.append(self.rect.copy())
        self.segments = self.segments[-self.length:]

    def grow(self):
        self.length += 1

    def reset(self):
        self.__init__()

    def draw(self, surface):
        for segment in self.segments:
            pg.draw.rect(surface, 'green', segment)

    def check_collision(self):
        return self.rect.collidelist(self.segments[:-1]) != -1

    def set_direction(self, key):
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
    def __init__(self):
        self.rect = pg.Rect(0, 0, TILE_SIZE - 2, TILE_SIZE - 2)
        self.rect.center = get_random_position()

    def respawn(self, occupied_positions):
        while True:
            new_pos = get_random_position()
            if new_pos not in occupied_positions:
                self.rect.center = new_pos
                break

    def draw(self, surface):
        pg.draw.rect(surface, 'red', self.rect)


class Game:
    def __init__(self):
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode([WINDOW] * 2)
        pg.display.set_caption("Snake Game")
        self.clock = pg.time.Clock()
        self.snake = Snake()
        self.food = Food()
        self.time = 0
        self.running = True
        self.paused = False
        self.score = 0
        self.highscore = load_highscore()
        self.font = pg.font.SysFont('Arial', FONT_SIZE, True)
        self.snd_eat = load_sound("eat.mp3")
        self.snd_gameover = load_sound("gameover.mp3")
        self.game_over = False

    def run(self):
        while self.running:
            self.handle_events()
            if not self.paused and not self.game_over:
                self.update()
            self.draw()
            self.clock.tick(FPS)

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.running = False
                elif event.key == pg.K_r:
                    self.reset()
                elif event.key == pg.K_p:
                    self.paused = not self.paused
                elif not self.paused and not self.game_over:
                    self.snake.set_direction(event.key)

    def update(self):
        now = pg.time.get_ticks()
        if now - self.time > TIME_STEP:
            self.time = now
            self.snake.move()

            if self.snake.check_collision():
                self.snd_gameover.play()
                self.game_over = True
                if self.score > self.highscore:
                    self.highscore = self.score
                    save_highscore(self.highscore)

            if self.snake.rect.center == self.food.rect.center:
                self.snake.grow()
                self.score += 1
                self.snd_eat.play()
                occupied = [segment.center for segment in self.snake.segments]
                self.food.respawn(occupied)

    def reset(self):
        self.snake.reset()
        occupied = [segment.center for segment in self.snake.segments]
        self.food.respawn(occupied)
        self.score = 0
        self.game_over = False
        self.paused = False

    def draw(self):
        self.screen.fill('black')
        self.snake.draw(self.screen)
        self.food.draw(self.screen)
        self.draw_text(f"Score: {self.score}", 10, 10)
        self.draw_text(f"Highscore: {self.highscore}", 10, 50)
        if self.paused:
            self.draw_centered_text("PAUSE")
        elif self.game_over:
            self.draw_centered_text("GAME OVER\nR - Restart | ESC - Exit")
        pg.display.flip()

    def draw_text(self, text, x, y):
        surface = self.font.render(text, True, 'white')
        self.screen.blit(surface, (x, y))

    def draw_centered_text(self, text):
        lines = text.split("\n")
        for i, line in enumerate(lines):
            surface = self.font.render(line, True, 'red')
            rect = surface.get_rect(center=(WINDOW // 2, WINDOW // 2 + i * FONT_SIZE))
            self.screen.blit(surface, rect)


if __name__ == '__main__':
    Game().run()
    pg.quit()
