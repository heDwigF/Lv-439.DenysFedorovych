import pygame

pygame.init()

WHITE = (255, 255, 255)  
ORANGE = (255, 150, 100)

DISPLAY_WIDTH = 400 
DISPLAY_HEIGH = 400 

gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGH))

pygame.display.set_caption("My first game")

clock=pygame.time.Clock()

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
LIGHT_BLUE = (64, 128, 255)
GREEN = (0, 200, 64)
YELLOW = (225, 225, 0)
PINK = (230, 50, 230)
PI = 3.14

# -------- Main Program Loop -----------
while not done:
  # --- Main event loop
  for event in pygame.event.get(): # User did something
    if event.type == pygame.QUIT:
        print("User asked to quit.")
    # elif event.type == pygame.KEYDOWN:
    #     print("User pressed a key.")
    # elif event.type == pygame.KEYUP:
    #     print("User let go of a key.")
    # elif event.type == pygame.MOUSEBUTTONDOWN:
    #     print("User pressed a mouse button")

#   pygame.draw.arc(gameDisplay, WHITE, (10, 50, 280, 100), 0, PI)
#   pygame.draw.arc(gameDisplay, PINK, (50, 30, 200, 150), PI, 2*PI, 3)
    # pygame.draw.circle(gameDisplay, YELLOW, (100, 100), 50,5)
    # pygame.draw.circle(gameDisplay, PINK, (200, 100), 50)
    # pygame.draw.ellipse(gameDisplay, GREEN, (100, 50, 280, 100))

    # pygame.draw.lines(gameDisplay, WHITE, True, [[10, 10], [140, 70], [280, 20]], 2)
    # pygame.draw.aalines(gameDisplay, WHITE, False, [[10, 100], [140, 170], [280, 110]])

    # pygame.draw.line(gameDisplay, WHITE, [10, 30], [290, 15], 3)
    # pygame.draw.line(gameDisplay, WHITE, [10, 50], [290, 35])
    # pygame.draw.aaline(gameDisplay, WHITE, [10, 70], [290, 55])

    pygame.draw.line(gameDisplay, (255,255,255), [10, 30], [290, 15], 3)
    pygame.draw.rect(gameDisplay, (255,0,0), [55, 50, 80, 55])
    pygame.draw.rect(gameDisplay, (0,0,128), [175, 130, 80, 55]) 
    pygame.draw.rect(gameDisplay, (64, 128, 255), (300, 70, 100, 75), 8)
    pygame.draw.aalines(gameDisplay, (255,255,255), True, [[250, 210], [280, 250], [190, 290], [180, 280]])  
    pygame.draw.circle(gameDisplay, (192,192,192), (300, 300), 50)
    pygame.draw.circle(gameDisplay, (255,255,0), (80, 250), 50, 10)
  # --- Game logic should go here
  # --- Drawing code should go here
  # First, clear the screen to white. Don't put other 
  # drawing commands above this, 
  # or they will be erased with this command.
  
#   gameDisplay.fill(ORANGE)
  
  # --- Go ahead and update the screen with what we've drawn.
  pygame.display.update()
  
  
  # --- Limit to 60 frames per second
clock.tick(60)