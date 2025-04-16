import pygame
import sys
import random
import psycopg2
from datetime import datetime

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 600, 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Game variables
snake_pos = [[100, 50], [90, 50], [80, 50]]
snake_speed = [10, 0]
food = {'pos': [0, 0], 'weight': 1, 'spawn_time': 0}
food_spawn = True
score = 0
level = 1
speed_increase = 0.1
food_counter = 0
fps = pygame.time.Clock()
paused = False

# Database functions
def get_connection():
    return psycopg2.connect(dbname='lab10', user='postgres', password='uralsk07sila', host='localhost', port='5432')

def get_or_create_user(username):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id FROM game_user WHERE username = %s", (username,))
    user = cur.fetchone()
    if user:
        user_id = user[0]
    else:
        cur.execute("INSERT INTO game_user (username) VALUES (%s) RETURNING id", (username,))
        user_id = cur.fetchone()[0]
        conn.commit()
    cur.close()
    conn.close()
    return user_id

def get_last_score(user_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT score, level FROM user_score WHERE user_id = %s ORDER BY saved_at DESC LIMIT 1", (user_id,))
    result = cur.fetchone()
    cur.close()
    conn.close()
    return result if result else (0, 1)

def save_score(user_id, score, level):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO user_score (user_id, score, level) VALUES (%s, %s, %s)", (user_id, score, level))
    conn.commit()
    cur.close()
    conn.close()

def get_username_input():
    username = ""
    input_active = True
    font = pygame.font.SysFont('arial', 30)

    while input_active:
        screen.fill(BLACK)
        prompt = font.render("Enter your name:", True, WHITE)
        user_text = font.render(username, True, GREEN)

        screen.blit(prompt, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 50))
        screen.blit(user_text, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if username.strip() != "":
                        input_active = False
                        break
                elif event.key == pygame.K_BACKSPACE:
                    username = username[:-1]
                else:
                    username += event.unicode
    return username.strip()


# Game start
player_name = get_username_input()
user_id = get_or_create_user(player_name)
score, level = get_last_score(user_id)
print(f"Welcome {player_name}! Your last saved level was {level} with score {score}.")

# Game functions
def check_collision(pos):
    if pos[0] < 0 or pos[0] > SCREEN_WIDTH - 10 or pos[1] < 0 or pos[1] > SCREEN_HEIGHT - 10:
        return True
    if pos in snake_pos[1:]:
        return True
    return False

def get_random_food():
    global food_counter
    while True:
        pos = [random.randrange(1, (SCREEN_WIDTH // 10)) * 10, random.randrange(1, (SCREEN_HEIGHT // 10)) * 10]
        if pos not in snake_pos:
            weight = 2 if food_counter >= 2 else 1
            food_counter = 0 if weight == 2 else food_counter + 1
            return {'pos': pos, 'weight': weight, 'spawn_time': pygame.time.get_ticks()}

# Main game loop
try:
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save_score(user_id, score, level)
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake_speed[1] == 0:
                    snake_speed = [0, -10]
                elif event.key == pygame.K_DOWN and snake_speed[1] == 0:
                    snake_speed = [0, 10]
                elif event.key == pygame.K_LEFT and snake_speed[0] == 0:
                    snake_speed = [-10, 0]
                elif event.key == pygame.K_RIGHT and snake_speed[0] == 0:
                    snake_speed = [10, 0]
                elif event.key == pygame.K_p:
                    paused = not paused
                elif event.key == pygame.K_s:
                    save_score(user_id, score, level)

        if not paused:
            snake_pos.insert(0, list(map(lambda x, y: x + y, snake_pos[0], snake_speed)))

            if check_collision(snake_pos[0]):
                save_score(user_id, score, level)
                pygame.quit()
                sys.exit()

            if snake_pos[0] == food['pos']:
                score += food['weight']
                if score % 3 == 0:
                    level += 1
                food_spawn = True
            else:
                snake_pos.pop()

            if food_spawn:
                food = get_random_food()
                food_spawn = False

            if pygame.time.get_ticks() - food['spawn_time'] > 10000:
                food_spawn = True

        screen.fill(BLACK)
        for pos in snake_pos:
            pygame.draw.rect(screen, GREEN, pygame.Rect(pos[0], pos[1], 10, 10))

        food_color = RED if food['weight'] == 1 else (255, 165, 0)
        pygame.draw.rect(screen, food_color, pygame.Rect(food['pos'][0], food['pos'][1], 10, 10))

        font = pygame.font.SysFont('arial', 20)
        score_text = font.render(f"Score: {score} Level: {level}", True, WHITE)
        screen.blit(score_text, [0, 0])

        if paused:
            pause_text = font.render("Paused (Press P to Resume)", True, WHITE)
            screen.blit(pause_text, [SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2])

        pygame.display.flip()
        fps.tick(10 + level * speed_increase)

except SystemExit:
    pygame.quit()