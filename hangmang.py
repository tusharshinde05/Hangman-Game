import pygame
import string
import random
import random_word

# Initialize pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 1000, 900
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman Game")

# Load images
images = []
for i in range(7):
    image = pygame.image.load("hangman" + str(i) + ".png")
    images.append(pygame.transform.scale(image, (300, 300)))

# Game variables
hangman_status = 0
#word="NIKHIL"
#words = ["PYTHON", "HANGMAN", "GAME", "PROGRAMMING", "OPENAI"]
#word = random.choice(words)
word = random_word.RandomWords().get_random_word().upper()
guessed = []

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
CYAN=(0,255,255)
MAGENTA=(255,0,255)
BLUE=(0,0,255)

# Fonts
LETTER_FONT = pygame.font.SysFont("comicsans", 40)
WORD_FONT = pygame.font.SysFont("comicsans", 60)
TITLE_FONT = pygame.font.SysFont("comicsans", 70)

# Game loop
FPS = 60
clock = pygame.time.Clock()
run = True
tries = 6

def draw():
    win.fill(BLUE)
    
    # Draw title
    text = TITLE_FONT.render("HANGMAN", 1, BLACK)
    win.blit(text, (WIDTH//2 - text.get_width()//2, 20))
    
    # Draw word
    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "
    text = WORD_FONT.render(display_word, 1, BLACK)
    win.blit(text, (100, 200))
    
    # Draw hangman image
    win.blit(images[hangman_status], (300, 500))
    
    # Check for game over
    if tries == 0:
        gameover_text = LETTER_FONT.render("Game Over! The word was: " + word, True, (255, 0, 0))
        win.blit(gameover_text, (WIDTH // 2 - gameover_text.get_width() // 2, 350))
    elif "_" not in display_word:
        win_text = LETTER_FONT.render("Congratulations! You won!", True, (0, 255, 0))
        win.blit(win_text, (WIDTH // 2 - win_text.get_width() // 2, 350)) 

    pygame.display.update()

while run:
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
            elif event.key in range(pygame.K_a, pygame.K_z + 1):
                letter = event.unicode.upper()
                if letter in string.ascii_uppercase and letter not in guessed:
                    guessed.append(letter)
                    if letter not in word:
                        hangman_status += 1
                        tries -= 1
    
    draw()

pygame.quit()
