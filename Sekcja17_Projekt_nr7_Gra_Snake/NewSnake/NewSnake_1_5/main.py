import pygame as pg
from random import randrange
import os

# Stałe
WINDOW = 1000
TILE_SIZE = 50
RANGE = (TILE_SIZE // 2, WINDOW - TILE_SIZE // 2, TILE_SIZE)
FPS = 60
TIME_STEP = 110
HIGHSCORE_FILE = "highscore.txt"

# Funkcja losująca pozycję
def get_random_position():
    return (randrange(*RANGE), randrange(*RANGE))


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
        # Teleportacja przez granice
        if self.rect.left < 0:
            self.rect.right = WINDOW
        elif self.rect.right > WINDOW:
            self.rect.left = 0
        if self.rect.top < 0:
            self.rect.bottom = WINDOW
        elif self.rect.bottom > WINDOW:
            self.rect.top = 0

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
        self.screen = pg.display.set_mode([WINDOW] * 2)
        pg.display.set_caption("Snake Game")
        self.clock = pg.time.Clock()
        self.font = pg.font.SysFont('consolas', 36)
        self.snake = Snake()
        self.food = Food()
        self.time = 0
        self.running = True
        self.paused = False
        self.game_over = False
        self.score = 0
        self.highscore = self.load_highscore()

        # Dźwięki
        self.eat_sound = self.load_sound("eat.mp3")
        self.gameover_sound = self.load_sound("gameover.mp3")

    def load_sound(self, filename):
        try:
            return pg.mixer.Sound(filename)
        except Exception:
            print(f"⚠️ Brak dźwięku: {filename}")
            return None

    def play_sound(self, sound):
        if sound:
            sound.play()

    def load_highscore(self):
        if not os.path.exists(HIGHSCORE_FILE):
            return 0
        try:
            with open(HIGHSCORE_FILE, "r") as f:
                return int(f.read())
        except Exception:
            return 0

    def save_highscore(self):
        try:
            with open(HIGHSCORE_FILE, "w") as f:
                f.write(str(self.highscore))
        except Exception:
            pass

    def reset_game(self):
        self.snake.reset()
        self.food.respawn([])
        self.score = 0
        self.time = pg.time.get_ticks()
        self.paused = False
        self.game_over = False

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
            elif event.type == pg.KEYDOWN:
                if self.game_over:
                    self.reset_game()
                elif event.key == pg.K_ESCAPE:
                    self.running = False
                elif event.key == pg.K_p:
                    self.paused = not self.paused
                elif event.key == pg.K_r:
                    self.reset_game()
                elif event.key in (pg.K_w, pg.K_s, pg.K_a, pg.K_d):
                    self.snake.set_direction(event.key)

    def update(self):
        now = pg.time.get_ticks()
        if now - self.time > TIME_STEP:
            self.time = now
            self.snake.move()

            if self.snake.check_collision():
                self.play_sound(self.gameover_sound)
                self.highscore = max(self.highscore, self.score)
                self.save_highscore()
                self.game_over = True
                return

            if self.snake.rect.colliderect(self.food.rect):
                self.snake.grow()
                self.score += 1
                self.play_sound(self.eat_sound)
                occupied = [segment.center for segment in self.snake.segments]
                self.food.respawn(occupied)

    def draw_text_center(self, text, color, y_offset=0):
        surf = self.font.render(text, True, color)
        rect = surf.get_rect(center=(WINDOW // 2, WINDOW // 2 + y_offset))
        self.screen.blit(surf, rect)

    def draw(self):
        self.screen.fill('black')
        self.snake.draw(self.screen)
        self.food.draw(self.screen)

        # Wyniki
        score_surf = self.font.render(f'Score: {self.score}', True, pg.Color('white'))
        highscore_surf = self.font.render(f'Highscore: {self.highscore}', True, pg.Color('yellow'))
        self.screen.blit(score_surf, (10, 10))
        self.screen.blit(highscore_surf, (10, 50))

        if self.paused:
            self.draw_text_center("PAUSE", pg.Color('gray'))
        elif self.game_over:
            self.draw_text_center("GAME OVER", pg.Color('red'), -30)
            self.draw_text_center("Press any key to restart", pg.Color('white'), 30)

        pg.display.flip()

    def run(self):
        while self.running:
            self.handle_events()
            if not self.paused and not self.game_over:
                self.update()
            self.draw()
            self.clock.tick(FPS)


if __name__ == '__main__':
    Game().run()
    pg.quit()
