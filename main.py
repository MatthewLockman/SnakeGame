# Imported Libraries
import pygame
import time
import random

snakeSpeed = 20

# Window Size of Game
windowX = 720
windowY = 480

# Defining Colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# Initizing the Game
pygame.init()

# Game Window
pygame.display.set_caption("Snake by Matthew Lockman")
gameWindow = pygame.display.set_mode((windowX, windowY))

# FPS Controller
fps = pygame.time.Clock()

# Starting Snake Position
snakePosition = [100, 50]

# Starting Snake Body
snakeBody = [
    [100, 50],
    [90, 50],
    [80, 50],
    [70, 50]
]

# Fruit Position
fruitPos = [random.randrange(1, (windowX//10)) * 10,
            random.randrange(1, (windowY//10)) * 10]

fruitSpawn = True

# Setting Default Snake direction (Towards Right)
direction = "RIGHT"
changeTo = direction

# Initial Score
score = 0

# Displaying Score Function
def showScore(choice, color, font, size):
    # Create the Scoring Object
    scoreFont = pygame.font.SysFont(font, size)
    scoreSurface = scoreFont.render("Score : " + str(score), True, color)
    scoreRect = scoreSurface.get_rect()

    # Display Text
    gameWindow.blit(scoreSurface, scoreRect)

# Game Over Function
def gameOver():
    # Creating the game over Object
    font = pygame.font.SysFont("times new roman", 50)
    gameOverSurface = font.render("Your Score is : " + str(score), True, red)
    gameOverRect = gameOverSurface.get_rect()
    gameOverRect.midtop = (windowX / 2, windowY/4)

    # draw text on screen
    gameWindow.blit(gameOverSurface, gameOverRect)
    pygame.display.flip()

    # Quit the Program after 2 seconds
    time.sleep(2)
    pygame.quit()
    quit()

# Main Function
while True:
    # Handling event keys
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                gameOver()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                changeTo = "UP"
            if event.key == pygame.K_DOWN:
                changeTo = "DOWN"
            if event.key == pygame.K_LEFT:
                changeTo = "LEFT"
            if event.key == pygame.K_RIGHT:
                changeTo = "RIGHT"

    # If two keys pressed simultaneously
    # we don't want snake to move into two directions
    # simultaneously
    if changeTo == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if changeTo == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if changeTo == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if changeTo == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # Moving the snake
    if direction == 'UP':
        snakePosition[1] -= 10
    if direction == 'DOWN':
        snakePosition[1] += 10
    if direction == 'LEFT':
        snakePosition[0] -= 10
    if direction == 'RIGHT':
        snakePosition[0] += 10

    # Snake body growing mechanism
    # if fruits and snakes collide then scores
    # will be incremented by 10
    snakeBody.insert(0, list(snakePosition))
    if snakePosition[0] == fruitPos[0] and snakePosition[1] == fruitPos[1]:
        score += 10
        fruitSpawn = False
    else:
        snakeBody.pop()
         
    if not fruitSpawn:
        fruitPos = [random.randrange(1, (windowX//10)) * 10,
                          random.randrange(1, (windowY//10)) * 10]
         
    fruitSpawn = True
    gameWindow.fill(black)

    for pos in snakeBody:
        pygame.draw.rect(gameWindow, green, pygame.Rect(pos[0], pos[1], 10, 10))

    pygame.draw.rect(gameWindow, white, pygame.Rect(fruitPos[0], fruitPos[1], 10, 10))

    # Game Over Conditions
    if snakePosition[0] < 0 or snakePosition[0] > windowX-10:
        gameOver()
    if snakePosition[1] < 0 or snakePosition[1] > windowY-10:
        gameOver()

    # Touching the snake body
    for block in snakeBody[1:]:
        if snakePosition[0] == block[0] and snakePosition[1] == block[1]:
            gameOver()

    # displaying score countinuously
    showScore(1, white, 'times new roman', 20)
 
    # Refresh game screen
    pygame.display.update()
 
    # Frame Per Second /Refresh Rate
    fps.tick(snakeSpeed)