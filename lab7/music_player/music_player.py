import pygame
import os

pygame.init()

playlist = [] #пустой список где будут хранится все пути к музыке
music_folder_path = "/Users/User/Desktop/pp_2/labs/lab7/music_player/musics"
all_music = os.listdir(music_folder_path) #получаем список всех файлов в указанной папке

for song in all_music:
    if song.endswith(".mp3"):
        playlist.append(os.path.join(music_folder_path, song))
#настройки окна:
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Lana Del Rey playlist") 
clock = pygame.time.Clock() #обьект для управления частотой обновления экрана

background = pygame.image.load(os.path.join("buttons", "background.jpg"))
background = pygame.transform.scale(background, (WIDTH, HEIGHT)) #мастабируем фоновое изображение до размера окна

font1 = pygame.font.SysFont(None, 25) #размер шрифта

#настройки для кнопок:
button_size = (70, 70)
play_button = pygame.transform.scale(pygame.image.load(os.path.join("buttons", "play.png")), button_size)
pause_button = pygame.transform.scale(pygame.image.load(os.path.join("buttons", "pause.png")), button_size)
next_button = pygame.transform.scale(pygame.image.load(os.path.join("buttons", "next.png")), button_size)
previous_button = pygame.transform.scale(pygame.image.load(os.path.join("buttons", "back.png")), button_size)

index = 0
music_play = False #флаг означающий что музыка не играет
pygame.mixer.music.load(playlist[index]) #загружаем первый трек
pygame.mixer.music.play(1) #воспроизведение трека, музыка будет играть 1 раз
music_play = True #флаг означающий что трек теперь играет

run = True
while run:
    screen.blit(background, (0, 0))

    text1 = font1.render(os.path.basename(playlist[index]), True, (0, 0, 0)) #имя текущего трека в центре экрана
    screen.blit(text1, (WIDTH // 2 - text1.get_width() // 2, 500)) #позиция на экране

    # размещение кнопок:
    screen.blit(previous_button, (273, 585))
    screen.blit(next_button, (460, 587))

    if music_play: #если музыка играет, то показываем кнопку паузы
        screen.blit(pause_button, (370, 590))
    else: #иначе кнопку играть
        screen.blit(play_button, (370, 590))

    pygame.display.update() #обновляем экран
    clock.tick(24) #FPS

    for event in pygame.event.get(): #получаем все события происходящие в программе 
        if event.type == pygame.QUIT: #если закрыли окно то выходим из программы
            run = False
            pygame.quit()
            exit()

        elif event.type == pygame.KEYDOWN: #если нажата клавиша:
            if event.key == pygame.K_SPACE: # когда нажата клавиша пробела то переключаем между play и pause
                if music_play:
                    music_play = False
                    pygame.mixer.music.pause()
                else:
                    music_play = True
                    pygame.mixer.music.unpause()
            
            if event.key == pygame.K_RIGHT: #если нажали на правую стрелку переходим к след треку
                index = (index + 1) % len(playlist)
                pygame.mixer.music.load(playlist[index])
                pygame.mixer.music.play()
            if event.key == pygame.K_LEFT: #если нажали на левую стрелку переходим к пердыдущему треку
                index = (index - 1) % len(playlist)
                pygame.mixer.music.load(playlist[index])
                pygame.mixer.music.play()

#проверяем играет ли музыка на данный момент. Если не играет то music_play указывает на то что музыка должна играть
# и переходим к следущему треку
if not pygame.mixer.music.get_busy() and music_play: 
    index = (index + 1) % len(playlist)
    pygame.mixer.music.load(playlist[index])
    pygame.mixer.music.play()