import pygame
pygame.init()

bg_size = (800, 800)
screen = pygame.display.set_mode(bg_size) #создаем окно с размером bg_size
pygame.display.set_caption("Red circle") 
ball_color = pygame.Color('red')
background_color = pygame.Color('white')

position = [400, 400] #начальная позиция шара
radius = 25
steps = 20 #количество пикселей на которое перемещается шар при каждом нажатии на клавишу

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #если пользователь закрыл окно то выходим из программы
            pygame.quit()
            exit()
            
    #нажатие на клавиши:
    keys = pygame.key.get_pressed() #получаем состояние всех клавиш то есть какие клавиши нажаты на данный момент
    if keys[pygame.K_UP]:
        position[1] = max(position[1] - steps, radius) #перемещаем шар в вверх прроверяя чтобы шар не выходил за границу экрана(не опускался ниже радиуса) 
    if keys[pygame.K_DOWN]:
        position[1] = min(position[1] + steps, bg_size[1] - radius) #увеличивая значение перемещаем вниз и чтобы не поднимался выше радиуса
    if keys[pygame.K_LEFT]:
        position[0] = max(position[0] - steps, radius)
    if keys[pygame.K_RIGHT]:
        position[0] = min(position[0] + steps, bg_size[0] - radius)

    screen.fill(background_color) #заполняем весь экран фоном белого цвета то есть очищаем экран перед рисованием нового кадра
    pygame.draw.circle(screen, ball_color, position, radius) #рисуем шар, указываем цвет шара его позицию и радиус

    pygame.display.flip() #обновляем экран, отоюражая все изменения

    pygame.time.Clock().tick(60) #частота кадров