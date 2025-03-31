import pygame 
import math
 
 
WIDTH, HEIGHT = 1200, 800  
FPS = 90 #частота обновления экрана
draw = False    #флаг указывающий рисует ли сейчас пользователь
radius = 2    #радиус(толшина) кисти
color = 'black'       #начальный цвет кисти    
mode = 'pen'   #режим рисования

color_palette = ['black', 'red', 'green', 'blue', 'yellow', 'purple', 'orange', 'pink', 'white'] #список доступных цветов
palette_rects = [] #прямоугольники палитры

def draw_palette():
    x, y = 10, 10 #начальная координата палитры
    size = 40 #размер одного цветного квадрата
    for col in color_palette:
        rect = pygame.Rect(x, y, size, size) #создём квадрат
        pygame.draw.rect(screen, pygame.Color(col), rect) #закрашиваем его
        pygame.draw.rect(screen, pygame.Color('black'), rect, 2) #рамка
        palette_rects.append((rect, col)) #добавляем в список
        y += size + 5 #смещаем вниз для следующего квадрата
 
pygame.init() 
screen = pygame.display.set_mode([WIDTH, HEIGHT]) #создаём окно
pygame.display.set_caption('Paint') #название окна
clock = pygame.time.Clock() #обьект для управления фпс
screen.fill(pygame.Color('white'))  #заливаем фон белым
font = pygame.font.SysFont('None', 60) #шрифт 
 
 
def drawLine(screen, start, end, width, color): 
    #Извлеките координаты x и y начальной и конечной точек
    x1 = start[0] 
    x2 = end[0] 
    y1 = start[1] 
    y2 = end[1] 
    
    #Вычисление абсолютных разностей в координатах x и y
    dx = abs(x1 - x2) 
    dy = abs(y1 - y2) 
    
    #Коэффициенты для линейного уравнения Ax + By + C = 0
    A = y2 - y1  # вертикально
    B = x1 - x2  # горизонтально
    C = x2 * y1 - x1 * y2 
    
    # Если линия скорее горизонтальная, чем вертикальная
    if dx > dy: 
        #Убедитесь, что x1 находится слева от x2
        if x1 > x2: 
            x1, x2 = x2, x1 
            y1, y2 = y2, y1 
        #Повторение по координатам x
        for x in range(x1, x2): 
            #Вычислите координату y, используя линейное уравнение
            y = (-C - A * x) / B 
            #Нарисуйте окружность (пиксель) в положении (x, y)
            pygame.draw.circle(screen, pygame.Color(color), (x, y), width) 
    #Если линия более вертикальная, чем горизонтальная
    else: 
        # Убедитесь, что y1 меньше y2
        if y1 > y2: 
            x1, x2 = x2, x1 
            y1, y2 = y2, y1 
        # Повторение по координатам y
        for y in range(y1, y2): 
            # Вычислите координату x, используя линейное уравнение
            x = (-C - B * y) / A 
            # Нарисуйте окружность (пиксель) в положении (x, y)
            pygame.draw.circle(screen, pygame.Color(color), (x, y), width)

 
 
def drawCircle(screen, start, end, width, color): 
    #извлекаем координаты х и у начальной и конечной точек
    x1 = start[0]  # Извлекаем x-координату начальной точки
    x2 = end[0]  # Извлекаем x-координату конечной точки
    y1 = start[1]  # Извлекаем y-координату начальной точки
    y2 = end[1]  # Извлекаем y-координату конечной точки.
    
    # центр круга
    x = (x1 + x2) / 2  
    y = (y1 + y2) / 2  
    radius = math.hypot(x2 - x1, y2 - y1) // 2 
    
    # Рисуем круг на экране
    pygame.draw.circle(screen, pygame.Color(color), (x, y), radius, width) 

 
 
def drawRectangle(screen, start, end, width, color): 
    x1 = start[0] 
    x2 = end[0] 
    y1 = start[1] 
    y2 = end[1]  
    
    widthr = abs(x1 - x2)  
    height = abs(y1 - y2)  
    
    # Нарисуйте прямоугольник на экране, основываясь на положении начальной и конечной точек
    if x2 > x1 and y2 > y1: 
        pygame.draw.rect(screen, pygame.Color(color), (x1, y1, widthr, height), width)  
    if y2 > y1 and x1 > x2: 
        pygame.draw.rect(screen, pygame.Color(color), (x2, y1, widthr, height), width)  
    if x1 > x2 and y1 > y2: 
        pygame.draw.rect(screen, pygame.Color(color), (x2, y2, widthr, height), width)  
    if x2 > x1 and y1 > y2: 
        pygame.draw.rect(screen, pygame.Color(color), (x1, y2, widthr, height), width) 

while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            exit()  # выходим из программы если закрыли окно
        
        if event.type == pygame.KEYDOWN: 
            #Изменяем режим кисти в зависимости от нажатой клавиши
            if event.key == pygame.K_r: 
                mode = 'rectangle'
            if event.key == pygame.K_c: 
                mode = 'circle'
            if event.key == pygame.K_p: 
                mode = 'pen'
            if event.key == pygame.K_e: 
                mode = 'erase' 
            if event.key == pygame.K_BACKSPACE: 
                screen.fill(pygame.Color('white'))
   
 
      
        if event.type == pygame.MOUSEBUTTONDOWN:  
            draw = True  # Включить рисование
            if mode == 'pen': 
                pygame.draw.circle(screen, pygame.Color(color), event.pos, radius)
            prevPos = event.pos  # сохраняем текущую позицию как предыдущую
            for rect, col in palette_rects:
                if rect.collidepoint(event.pos): #проверяем попал ли клик в квадрат
                    color = col #меняем цвет кисти
 
        
        if event.type == pygame.MOUSEBUTTONUP:  
        # Когда кнопка мыши отпущена
        #Нарисуйте прямоугольник, если режим настроен на рисование:
            if mode == 'rectangle': 
                drawRectangle(screen, prevPos, event.pos, radius, color)
            elif mode == 'circle': 
                drawCircle(screen, prevPos, event.pos, radius, color) 
            draw = False  # Отключить рисование

 
       
        if event.type == pygame.MOUSEMOTION:  
        #когда мышка двигается
            if draw and mode == 'pen': 
                drawLine(screen, lastPos, event.pos, radius, color)  # Если включено рисование и включен режим пера, проведите линию между последней позицией и текущей позицией
            elif draw and mode == 'erase': 
                drawLine(screen, lastPos, event.pos, radius, 'white')  # Если включено рисование и активен режим стирания, проведите белую линию (стирание) между последней позицией и текущей позицией
            lastPos = event.pos  # Обновите последнюю позицию до текущей
 
    draw_palette()
    pygame.display.flip()  # обновление экрана
    clock.tick(FPS)