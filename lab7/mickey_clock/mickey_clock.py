import pygame
import time
import math
pygame.init()

#size of screen
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock() #обьект для управления временем

#name of the screen
pygame.display.set_caption("Mickey clock")

#загружем и масштабируем изображения
minute_hand = pygame.image.load('SMALLARROW.PNG')
second_hand = pygame.image.load('BIGARROW.PNG')
main_clock = pygame.image.load('main_clock2.PNG')
main_clock = pygame.transform.scale(main_clock, (WIDTH, HEIGHT))
minute_hand = pygame.transform.scale(minute_hand, (800, 800))
second_hand = pygame.transform.scale(second_hand, (800, 800))
#определяем центры для стрелок
center_min = (WIDTH // 2 , HEIGHT // 2 ) #center of the screen
center_sec = (WIDTH // 2 , HEIGHT // 2)
done = False

while not done: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    #благодаря localtime определяем минуты и секунды в текущее время 
    current_time = time.localtime()
    minute = current_time.tm_min
    second = current_time.tm_sec
    
    #вычисляем угол для стрелок
    minute_angle = minute * (360/60) + (second * (360/60)/60)
    second_angle = second * (360/60)
    
    #фон(циферблат) на экране начиная с координат 0,0
    screen.blit(main_clock, (0,0))
    
    #оң қол минутты орналастыру
    rotated_small_arm = pygame.transform.rotate(minute_hand , -minute_angle) #поворачиваем изображение стрелки на расчитанный угол
    minute_rect = rotated_small_arm.get_rect(center=center_min)
    screen.blit(rotated_small_arm, minute_rect.topleft)
    
    #сол қол секундты орналастыру
    rotated_big_arm = pygame.transform.rotate(second_hand, -second_angle)
    second_rect = rotated_big_arm.get_rect(center=center_sec) 
    screen.blit(rotated_big_arm, second_rect.topleft)#отображаем повернутую стрелку на экране
    
    pygame.display.flip() #обновление экрана
    pygame.time.wait(1000) #задержка на 1000 миллисекунд(1 секунду), обновляем каждую секунду
    clock.tick(60) #fps
    
pygame.quit() #завершение работу и закрываем окно