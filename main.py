from pygame import *
from random import randint
mixer.init()
font.init()

#Классы
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_speed, player_x, player_y, size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(size_x,size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        
        
    def reset(self):
        window.blit(self.image, (self.rect.x,self.rect.y))

class Player(GameSprite):
    def fire(self):
            bullet = Bullet('bullet.png', 5, player1.rect.centerx-20, player1.rect.top, 20, 30)    
            bullets.add(bullet)
            fire_sound.play()


                   
                          
class Enemy(GameSprite):    
    def update(self):
        if self.rect.y < 980:
            self.rect.y += self.speed
        else: 
            self.rect.y = 0
            self.rect.x = randint(50,1820)

            
class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed


#Экран
size_x = 1820
size_y = 980
window = display.set_mode((size_x, size_y))
display.set_caption('Танки')
display.set_icon(image.load('icon2.png'))
background = transform.scale(image.load('background1_.jpg'),(size_x,size_y))

#Музыка
main_music = 'music1.wav'
mixer.init()
mixer.music.load(main_music)
mixer.music.play()
fire_sound = mixer.Sound('fire_sound.wav')


#Переменные
clock = time.Clock()
game_open = True
game_over = False
move_down = False
move_up = False
move_right = False
move_left = False

count = 0
bullets = sprite.Group()

player1 = Player('t26.png', 3, 40, 800, 90, 160)

stena1 = Enemy('Sandbag.png', 0, 0, 620, 128, 128)
stena2 = Enemy('Sandbag.png', 0, 400, 730, 128, 128)
stena3 = Enemy('Sandbag.png', 0, 1000, 670, 128, 128)


font1 = font.Font(None, 24)
font2 = font.Font(None, 42)

textLose = font2.render("О нет, поражение(...", False,(180, 80, 80))     
textWin = font2.render("Ура, победа!", False,(10, 180, 80)) 


enemys = sprite.Group()
for i in range(2):
    enemy = Enemy('tankVraga.png',randint(1,2), randint(50,1600), 0, 110, 220)
    enemys.add(enemy)

#Игровой цикл
while not game_over:
    window.blit(background,(0,0))

    if count >= 6:
        game_open = False
        window.blit(textWin, (500,400))    

    for tank in enemys:                            
        if tank.rect.colliderect(stena1.rect) or tank.rect.colliderect(stena2.rect) or tank.rect.colliderect(stena3.rect):
            tank.rect.y -= 3
            tank.rect.x += 3
        elif tank.rect.colliderect(player1.rect):
            game_open = False
            window.blit(textLose, (500,400))            
    if player1.rect.colliderect(stena1.rect) or player1.rect.colliderect(stena2.rect) or player1.rect.colliderect(stena3.rect):
        player1.rect.x -= 3
        player1.rect.x += 3  

    colliders = sprite.groupcollide(bullets, enemys, True, True)
    for c in colliders:                            
        enemy = Enemy('tankVraga.png', (randint(10,30))/10, randint(50,1600), 0, 110, 220)
        enemys.add(enemy) 
        count += 1




    if move_down:
        player1.rect.y += player1.speed
            
    elif move_up:
        player1.rect.y -= player1.speed

    elif move_right:
        player1.rect.x += player1.speed

    elif move_left:
        player1.rect.x -= player1.speed
    
    if game_open:
        enemys.draw(window)
        enemys.update()
        player1.reset()
        bullets.draw(window)
        bullets.update()
        stena1.reset()
        stena2.reset()
        stena3.reset()



   
    for i in event.get():
        if i.type == QUIT:
            game_over = True

        if game_open:
            
            if i.type == KEYDOWN:
                if i.key == K_w:
                    move_up = True
                if i.key == K_s:
                    move_down = True
                if i.key == K_a:
                    move_left = True
                if i.key == K_d:
                    move_right = True

                if i.key == K_SPACE:
                    player1.fire()

            elif i.type == KEYUP:
                if i.key == K_w:
                    move_up = False
                if i.key == K_s:
                    move_down = False
                if i.key == K_a:
                    move_left = False
                if i.key == K_d:
                    move_right = False     
            
         



            
               
    
    display.update()
    clock.tick(80)