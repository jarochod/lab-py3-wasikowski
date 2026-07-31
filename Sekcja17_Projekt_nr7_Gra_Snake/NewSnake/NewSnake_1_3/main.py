import pygame as pg
from random import randrange

# Stałe
WINDOW = 1000
TILE_SIZE = 50
RANGE = (TILE_SIZE // 2, WINDOW - TILE_SIZE // 2, TILE_SIZE)
FPS = 60
TIME_STEP = 110


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

        # Teleportacja (bez kolizji ze ścianą)
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
        self.snake = Snake()
        self.food = Food()
        self.time = 0
        self.running = True
        self.score = 0
        self.font = pg.font.SysFont('consolas', 36)

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
            elif event.type == pg.KEYDOWN:
                self.snake.set_direction(event.key)

    def update(self):
        now = pg.time.get_ticks()
        if now - self.time > TIME_STEP:
            self.time = now
            self.snake.move()

            if self.snake.check_collision():
                self.snake.reset()
                self.food.respawn([])
                self.score = 0

            if self.snake.rect.colliderect(self.food.rect):
                self.snake.grow()
                self.score += 1
                occupied = [segment.center for segment in self.snake.segments]
                self.food.respawn(occupied)

    def draw(self):
        self.screen.fill('black')
        self.snake.draw(self.screen)
        self.food.draw(self.screen)

        # Wyświetlanie wyniku
        score_surface = self.font.render(f'Score: {self.score}', True, pg.Color('white'))
        self.screen.blit(score_surface, (10, 10))

        pg.display.flip()


if __name__ == '__main__':
    Game().run()
    pg.quit()
