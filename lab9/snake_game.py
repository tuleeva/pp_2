import pygame
import sys
import random
import copy
import time

pygame.init()

scale = 15 #размер одной клетки
score = 0
level = 1
speed = 8
food_x = 10 #координата х еды
food_y = 10 #координат у еды
display = pygame.display.set_mode((500, 500)) #создание окна
pygame.display.set_caption("Snake Game") #заголовок окна
clock = pygame.time.Clock() #обьект для управления частотой кадров

bg_top = (75, 0, 130) #цвет верхней части фона
bg_bottom = (0, 0, 50) #цвет нижней части фона
snake_colour = (0, 128, 0) 
snake_head = (50, 205, 50) 
food_colour = (255, 69, 0)
font_colour = (255, 255, 255)
defeat_colour = (255, 0, 0) #цвет текста при проигрыше
# snake_head = pygame.image.load("snake_head.PNG")
# snake_head = pygame.transform.scale(snake_head, (scale*2, scale*2))

#класс змеи
class Snake:
    def __init__(self, start_x, start_y):
        #координаты головы змеи
        self.x = start_x
        self.y = start_y
        #ширина и высота змеи
        self.w = 15
        self.h = 15
        #направление движения змеи(по умолчанию в право)
        self.x_direction = 1
        self.y_direction = 0
        self.history = [[self.x, self.y]]#список для хранения координат всех сегментов тела змейки
        self.length = 1 #начальная длина змейки(1 сегмент)

    def reset(self): #эта функция возвращает змейку в начальное положение после проигрыша
        self.x = 500/2 - scale #перемещаем голову змейки в центр экрана по х
        self.y = 500/2 - scale # то же самое по у
        self.w = 15 
        self.h = 15
        self.x_direction = 1 #направление снова в право
        self.y_direction = 0 #вертикального движения нет
        self.history = [[self.x, self.y]] #очищаем историю движения
        self.length = 1 #возвращаем длину змейки к 1

    def show(self): #отображает змейку на экране. первый сегмент(голова) имеет другой цвет
        for i in range(self.length): #перебираем каждый сегмент змейки
            if not i == 0:  #если это не голова
                pygame.draw.rect(display, snake_colour, (self.history[i][0], self.history[i][1], self.w, self.h))
            else:  #если это голова змейки
                #display.blit(snake_head, (self.history[i][0], self.history[i][1]))
                pygame.draw.rect(display, snake_head, (self.history[i][0], self.history[i][1], self.w, self.h))

    def check_eat(self): #проверяет сьела ли змейка еду
        if abs(self.history[0][0] - food_x) < scale and abs(self.history[0][1] - food_y) <scale:
            return True
        
    def check_level(self): #увеличивает уровень каждые 5 съеденных кусочков еды
        global level
        if self.length % 5 ==0:
            return True
        
    def snake_grow(self):
        self.length += 1 #увеличиваем длину змейки
        self.history.append(self.history[self.length - 2]) #добавляем новый сегмент в конец

    def collision(self): #проверяет врезалась ли змейка в саму себя
        i = self.length -1
        while i > 0:
            if abs(self.history[0][0] - self.history[i][0]) < self.w and abs(self.history[0][1] - self.history[i][1]) < self.h and self.length > 2:
                return True
            i -= 1

    def update(self): #обновляет положение змейки на экране
        i = self.length - 1
        while i > 0:
            self.history[i] = copy.deepcopy(self.history[i-1]) #перемещаем каждый сегмент вперёд
            i -=1
        self.history[0][0] += self.x_direction * scale #двигаем голову по х
        self.history[0][1] += self.y_direction * scale #то же самое по у

class Food:
    def __init__(self):
        self.type = "normal"
        self.timer = time.time()
        self.new_location()


    def new_location(self): #генерирует еду в случайном месте
        global food_x, food_y
        self.timer = time.time() #запоминаем время появления
        self.type = random.choices(["normal", "rare", "super"], weights=[70, 20, 10])[0]
        food_x = random.randrange(1, int(500/scale) - 1) * scale
        food_y = random.randrange(1, int(500/scale) - 1) * scale

    def show_food(self):
        if self.type == "normal":
            color = (255, 69, 0) #обычная еда - красная
        elif self.type == "rare":
            color = (255, 215, 0) # редкая еда - золотая
        else:
            color = (138, 43, 226) # супер-еда - фиолетовая
        pygame.draw.rect(display, color, (food_x, food_y, scale, scale))

    def update(self):
        if time.time() - self.timer > 7: #после 7 сек еда исчезает
            self.new_location()

def show_score():
    font = pygame.font.SysFont(None, 20)
    text = font.render("Score: " + str(score), True, font_colour)
    display.blit(text, (scale, scale))

def show_level():
    font = pygame.font.SysFont(None, 20)
    text = font.render("Level: " + str(level), True, font_colour)
    display.blit(text, (90 - scale, scale))

def game_loop(): #игровой цикл
    global score
    global level
    global speed
    
    #создаем обьекты змейки и еды
    snake = Snake(500/2, 500/2)
    food = Food()
    food.new_location()

    while True:
        for event in pygame.event.get(): #получаем события клавиатуры
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key ==pygame.K_q:
                    pygame.quit()
                    sys.exit()
                if snake.y_direction == 0:
                    if event.key == pygame.K_UP:
                        snake.x_direction = 0
                        snake.y_direction = -1
                    if event.key == pygame.K_DOWN:
                        snake.x_direction = 0
                        snake.y_direction = 1
                if snake.x_direction ==0:
                    if event.key == pygame.K_LEFT:
                        snake.x_direction = -1
                        snake.y_direction = 0
                    if event.key == pygame.K_RIGHT:
                        snake.x_direction = 1
                        snake.y_direction = 0

        for y in range(500): #делаем фон с градиентом
            colour = (
                bg_top[0] + (bg_bottom[0] - bg_top[0]) * y/500,
                bg_top[1] + (bg_bottom[1] - bg_top[1]) * y/500,
                bg_top[2] + (bg_bottom[2] - bg_top[2]) * y/500
            )
            pygame.draw.line(display, colour, (0, y), (500, y))

        snake.show() #отображаем змейку на экране
        snake.update()
        food.show_food()#отображаем еду на экране
        show_level()#отображаем уровень
        show_score()#отображаем текущий счёт

        if snake.check_eat():
            if food.type == "normal":
                score += 1
            elif food.type == "rare":
                score += 3
            else:
                score += 5
            food.new_location() #перемещаем еду в новое случайное место
            snake.snake_grow() #увеличиваем длину змейки

        if snake.check_level():
            food.new_location() #создаём еду в случайном месте
            level += 1 #увеличиваем уровень
            speed += 1 # увеличиваем скорость игры
            snake.snake_grow() #делаем змею длиннее

        if snake.collision(): #если змея столкнулась с собой
            score = 0 #обнуляем счёт
            level = 1 #сбрасываем уровень до 1
            font = pygame.font.SysFont(None, 100) #создаём шрифт для надписи
            text = font.render("Game Over!", True, defeat_colour) #рисуем текст
            display.blit(text, (50, 200)) #отображаем текст на экране
            pygame.display.update() #обновляем экран
            time.sleep(3) #пауза на 3 сек
            snake.reset() #перезапускаем змейку

        #это чтобы змея проникала через стену
        # if snake.history[0][0] > 500:
        #     snake.history[0][0] = 0
        # if snake.history[0][0] < 0:
        #     snake.history[0][0] = 500
        # if snake.history[0][1] > 500:
        #     snake.history[0][1] = 0
        # if snake.history[0][1] < 0:
        #     snake.history[0][1] = 500
        
        #это если мы хотим чтобы игра закончилась если змея ударилась об стену
        if (snake.history[0][0] <0 or snake.history[0][0] >= 500 or snake.history[0][1] < 0 or snake.history[0][1] >= 500):
            score = 0
            level = 1
            font = pygame.font.SysFont(None, 70)
            text = font.render("GAME OVER!", True, defeat_colour)
            display.blit(text, (90, 200))
            pygame.display.update()
            time.sleep(3)
            snake.reset()

        pygame.display.update()
        clock.tick(speed)

        food.update()

game_loop()