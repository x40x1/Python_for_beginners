import pygame

class Game:
    def __init__(self, width, height):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Pong Game")
        self.ball = Ball(self.width // 2, self.height // 2)
        self.paddle1 = Paddle(20, self.height // 2 - 50)
        self.paddle2 = Paddle(self.width - 40, self.height // 2 - 50)
        self.score1 = 0
        self.score2 = 0
        self.game_over = False

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.ball.draw(self.screen)
        self.paddle1.draw(self.screen)
        self.paddle2.draw(self.screen)
        font = pygame.font.Font(None, 36)
        score1_text = font.render(str(self.score1), True, (255, 255, 255))
        score2_text = font.render(str(self.score2), True, (255, 255, 255))
        self.screen.blit(score1_text, (self.width // 4, 10))
        self.screen.blit(score2_text, (self.width * 3 // 4, 10))
        pygame.display.update()

    def update(self):
        self.ball.update()
        self.paddle1.update()
        self.paddle2.update()
        if self.ball.x < 0:
            self.score2 += 1
            self.reset()
        elif self.ball.x > self.width:
            self.score1 += 1
            self.reset()
        if self.ball.y < 0 or self.ball.y > self.height:
            self.ball.dy *= -1
        if self.ball.collides_with(self.paddle1) or self.ball.collides_with(self.paddle2):
            self.ball.dx *= -1.1
        if self.score1 >= 10 or self.score2 >= 10:
            self.game_over = True

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    self.paddle1.dy = -5
                elif event.key == pygame.K_s:
                    self.paddle1.dy = 5
                elif event.key == pygame.K_UP:
                    self.paddle2.dy = -5
                elif event.key == pygame.K_DOWN:
                    self.paddle2.dy = 5
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    self.paddle1.dy = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    self.paddle2.dy = 0

    def reset(self):
        self.ball = Ball(self.width // 2, self.height // 2)
        self.paddle1 = Paddle(20, self.height // 2 - 50)
        self.paddle2 = Paddle(self.width - 40, self.height // 2 - 50)

    def run(self):
        while not self.game_over:
            self.handle_events()
            self.update()
            self.draw()
        pygame.quit()


class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 10
        self.color = (255, 255, 255)
        self.dx = 5
        self.dy = 5

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def update(self):
        self.x += self.dx
        self.y += self.dy

    def collides_with(self, paddle):
        if self.x - self.radius < paddle.x + paddle.width and self.x + self.radius > paddle.x:
            if self.y - self.radius < paddle.y + paddle.height and self.y + self.radius > paddle.y:
                return True
        return False


class Paddle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 20
        self.height = 100
        self.color = (255, 255, 255)
        self.dy = 0

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def update(self):
        self.y += self.dy
        if self.y < 0:
            self.y = 0
        elif self.y + self.height > 600:
            self.y = 500