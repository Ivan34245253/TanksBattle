import pygame
from random import randint
pygame.init()
clock = pygame.time.Clock()

size_x = 1820
size_y = 980
window = pygame.display.set_mode((size_x, size_y))
pygame.display.set_caption('Танки')
pygame.display.set_icon(pygame.image.load('icon2.png'))

background = pygame.transform.scale(pygame.image.load('background1.jpg'),(size_x,size_y))


main_music = 'music1.wav'
pygame.mixer.init()
pygame.mixer.music.load(main_music)
pygame.mixer.music.play()
fire_sound = pygame.mixer.Sound('fire_sound.wav')
fire_sound.play()

game_open = True
game_over = False
move_down = False
move_up = False
move_down2 = False
move_up2 = False

while not game_over:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

        if game_open:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    move_up = True
                if event.key == pygame.K_s:
                    move_down = True

                if event.key == pygame.K_UP:
                    move_up2 = True
                if event.key == pygame.K_DOWN:
                    move_down2 = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    move_up = False
                if event.key == pygame.K_s:
                    move_down = False

                if event.key == pygame.K_UP:
                    move_up2 = False
                if event.key == pygame.K_DOWN:
                    move_down2 = False
 

    window.blit(background,(0,0))
    pygame.display.update()
    clock.tick(80)

