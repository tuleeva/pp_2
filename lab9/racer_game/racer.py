# Imports
import pygame, sys
from pygame.locals import * #содержит константы как QUITT, K_LEFT и тд
import random, time

# Initialzing
pygame.init()

# fps
fps =60
FramePerSec = pygame.time.Clock() #ограничивает в главном цикле скорость обновления экрана

# Определение цветов
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)
white = (255, 255, 255)
gold = (255, 215, 0)

# основные переменные
WIDTH = 400
HEIGHT = 600
SPEED = 3
SCORE = 0
COINS = 0


#Настройка шрифтов
font = pygame.font.SysFont("Verdana", 20)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("GAME OVER!", True, red)

background = pygame.image.load("racer_road.PNG") #фон игры

#создание окна
screen = pygame.display.set_mode((400, 600))
screen.fill(white) #заполнение экрана белым цветом
pygame.display.set_caption("Racer") #заголовок окна


class Enemy(pygame.sprite.Sprite): #класс врага
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("enemy_car.png")
        self.rect = self.image.get_rect() #получение границы обьекта
        self.rect.center = (random.randint(40, WIDTH - 40), 0) #ставит врага в случайное место сверху

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED) #двигает врага вниз
        if (self.rect.top > 600): #если враг уходит за экран, то:
            SCORE += 1 
            self.rect.top = 0
            self.rect.center = (random.randint(40, WIDTH - 40), 0) #враг перемещается наверх в случайное место

c1,c2,c3,c4,c5 = False, False, False, False, False
#класс монеты
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("coinn.PNG")
        self.image = pygame.transform.scale(self.image, (40, 40)) #уменьшаем размер монеты
        self.rect = self.image.get_rect()
        self.value = random.choices([1, 2, 3], weights = [50, 30, 20])[0] #случайная стоимость монет
        self.rect.center = (random.randint(40, WIDTH - 40), random.randint(40, HEIGHT - 40)) #перемещает монету в случайное место

    def move(self):
        global COINS
        global SPEED
        COINS += self.value
        self.respawn()
      
      # увеличивается скорость если собрано столько-то монет
        global c1,c2,c3,c4,c5
        if not c1 and COINS>=10:
            SPEED+=1
            c1=True
        if not c2 and COINS>=20:
            SPEED+=1
            c2=True
        if not c3 and COINS>=30:
            SPEED+=1
            c3=True
        if not c4 and COINS>=40:
            SPEED+=1
            c4=True
        if not c5 and COINS>=50:
            SPEED+=1
            c5=True
        self.rect.top = random.randint(40, WIDTH - 40)
    def respawn(self):
        self.value = random.choices([1, 2, 3], weights=[50, 30, 20])[0] 
        self.rect.center = (random.randint(40, WIDTH - 40), random.randint(40, HEIGHT - 40))

        #класс игрока
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("player_car.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520) #ставит машинку по центру внизу

    def move(self): #управление машинкой стрелками
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)
        if self.rect.top > 0:
            if pressed_keys[K_UP]:
                self.rect.move_ip(0, -5)
        if self.rect.bottom < HEIGHT:
            if pressed_keys[K_DOWN]:
                self.rect.move_ip(0, 5)
                
# Setting up Sprites
P1 = Player()
E1 = Enemy()
C1 = Coin()

# Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
coinss = pygame.sprite.Group()
coinss.add(C1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)

# увеличение скорости со временем
# INC_SPEED = pygame.USEREVENT + 1
# pygame.time.set_timer(INC_SPEED, 1000)

#экран с завершением игры
def game_over_screen():
    screen.fill(black)
    screen.blit(game_over, (130, 250))
    pygame.display.update()
    time.sleep(2)
    pygame.quit()
    sys.exit()

    

    while True:
        for event in pygame.event.get(): #проверяет события, например выход из игры
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

def handle_crash():
    time.sleep(2)

background_y = 0  

while True:
    for event in pygame.event.get():
        # if event.type == INC_SPEED:
        #     SPEED += 0.1
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

 # если игрок сталкивается с врагом то GAME OVER
    if pygame.sprite.spritecollideany(P1, enemies):
             game_over_screen()
             pygame.quit()
             sys.exit()

    # двигает фон вниз
    background_y = (background_y + SPEED) % background.get_height()

    # Нарисуйте фон в рассчитанном положении
    screen.blit(background, (0, background_y))
    screen.blit(background, (0, background_y - background.get_height()))

    scores = font_small.render(f"SCORE: {SCORE}", True, gold)
    screen.blit(scores, (10, 10))

    coins = font_small.render(f"COIN: {COINS}", True, gold)
    screen.blit(coins, (10, 30))

    # рисует и двигает все обьекты
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)

        if entity == C1:
            if pygame.sprite.spritecollideany(P1, coinss):
                entity.move()
        else:
            entity.move()

    # двигает рандомную следующую машину
    for enemy in enemies:
        enemy.move()

    # двигает монеты
    for coin in coinss:
        # if pygame.sprite.collide_rect(P1, coin):
        #     coin.move()
        coin.rect.y += SPEED

        # Монеты возрождаются, если они исчезают за пределами экрана.
        if coin.rect.top > HEIGHT:
            coin.rect.y = -coin.rect.height
            coin.rect.x = random.randint(40, WIDTH - 40)

#обновляет экран и ждет следущего кадра
    pygame.display.update()
    FramePerSec.tick(fps)