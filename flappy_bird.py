import pygame
from pygame.locals import *
from sys import exit
from random import randint
import os

pygame.init()

x_tela = 400
y_tela = 600
tela = pygame.display.set_mode((x_tela, y_tela))

velocidade_cano = 5
pontos = 0

class Bird(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.num = randint(1, 3)

        if self.num == 1:
            self.sprites = [pygame.image.load(os.path.join('image', 'yellowbox-upflap.png')),
                            pygame.image.load(os.path.join('image', 'yellowbox-downflap.png')),
                            pygame.image.load('image/yellowbox-midflap.png')]
        if self.num == 2:
            self.sprites = [pygame.image.load(os.path.join('image', 'bluebox-downflap.png')),
                             pygame.image.load(os.path.join('image', 'bluebox-upflap.png')),
                             pygame.image.load(os.path.join('image', 'bluebox-midflap.png'))]

        if self.num == 3:
            self.sprites = [pygame.image.load(os.path.join('image', 'redbox-upflap.png')),
                            pygame.image.load(os.path.join('image', 'redbox-downflap.png')),
                            pygame.image.load(os.path.join('image', 'redbox-midflap.png'))]


        self.atual = 0
        self.x = 100
        self.y = 270
        self.image = self.sprites[self.atual]
        self.rect = self.image.get_rect()
        self.rect.topleft = self.x, self.y

    def update(self):
        self.atual = self.atual + 1
        self.rect.topleft = self.x, self.y
        if self.atual >= len(self.sprites):
            self.atual = 0
        self.image = self.sprites[self.atual]

    def reset(self):
        self.y = 270
        self.num = randint(1, 3)



class Fundo(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.nume = randint(1, 2)

        if self.nume == 1:
            self.sprites = pygame.image.load(os.path.join('image', 'background-day.png'))
            self.sprites = pygame.transform.scale(self.sprites, [400, 600])

        if self.nume == 2:
            self.sprites = pygame.image.load(os.path.join('image', 'background-night.png'))
            self.sprites = pygame.transform.scale(self.sprites, [400, 600])

        self.image = self.sprites
        self.rect = self.image.get_rect()
        self.rect.topleft = 0, 0

    def update(self):
        self.image = self.sprites

    def reset(self):
        self.nume = randint(1, 2)



class Num(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.atual = 0
        self.nums = [pygame.image.load(os.path.join('image', '0.png')),
             pygame.image.load(os.path.join('image', '1.png')),
             pygame.image.load(os.path.join('image', '2.png')),
             pygame.image.load(os.path.join('image', '3.png')),
             pygame.image.load(os.path.join('image', '4.png')),
             pygame.image.load(os.path.join('image', '5.png')),
             pygame.image.load(os.path.join('image', '6.png')),
             pygame.image.load(os.path.join('image', '7.png')),
             pygame.image.load(os.path.join('image', '8.png')),
             pygame.image.load(os.path.join('image', '9.png'))]
        self.image = self.nums[self.atual]
        self.rect = self.image.get_rect()
        self.rect.topleft = 200, 0

    def update(self):
        self.image = self.nums[self.atual]

    def reset(self):
        self.atual = 0


class Msg(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = [pygame.image.load(os.path.join('image', 'gameover.png')),
                         pygame.image.load(os.path.join('image', 'message.png'))]

    def update(self, gameover=False, get_ready=False):
        if gameover:
            self.image = self.sprites[0]
            self.rect = self.image.get_rect()
            self.rect.topleft = 100, 170
        if get_ready:
            self.image = self.sprites[1]
            self.rect = self.image.get_rect()
            self.rect.topleft = 100, 170

class Chao(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.sprite = pygame.image.load(os.path.join('image', 'base.png'))
        self.sprite = pygame.transform.scale(self.sprite, [400, 100])
        self.image = self.sprite
        self.rect = self.sprite.get_rect()
        self.rect.topleft = 0, 500

    def update(self):
        self.image = self.sprite

class Cano(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.num = randint(0, 1)
        self.altura = randint(-250, 3)
        self.x = 300

        if self.num == 0:
            self.sprite = pygame.image.load(os.path.join('image', 'pipe-green.png'))
            self.sprite = pygame.transform.flip(self.sprite, False, True)

        if self.num == 1:
            self.sprite = pygame.image.load(os.path.join('image', 'pipe-red.png'))
            self.sprite = pygame.transform.flip(self.sprite, False, True)

        self.image = self.sprite
        self.rect = self.image.get_rect()

    def update(self):
        self.x -= velocidade_cano
        self.rect.topleft = self.x, self.altura
        self.image = self.sprite

grupo_cano = pygame.sprite.Group()
cano = Cano()
grupo_cano.add(cano)

class Cano2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.x = 300
        self.altura = cano.altura + 450

        if cano.num == 0:
            self.sprite = pygame.image.load(os.path.join('image', 'pipe-green.png'))

        if cano.num == 1:
            self.sprite = pygame.image.load(os.path.join('image', 'pipe-red.png'))

        self.image = self.sprite
        self.rect = self.image.get_rect()
        self.rect.topleft = self.x, self.altura

    def update(self):
        self.x -= velocidade_cano
        self.rect.topleft = self.x, self.altura
        self.image = self.sprite

grupo_num = pygame.sprite.Group()
num = Num()
grupo_num.add(num)

grupo_cano2 = pygame.sprite.Group()
cano2 = Cano2()
grupo_cano2.add(cano2)

grupo_base = pygame.sprite.Group()
base = Chao()
grupo_base.add(base)

grupo_msg = pygame.sprite.Group()
msg = Msg()
grupo_msg.add(msg)

grupo_num = pygame.sprite.Group()
num = Num()
grupo_num.add(num)

grupo_background = pygame.sprite.Group()
fundo = Fundo()
grupo_background.add(fundo)

grupo_bird = pygame.sprite.Group()
passaro = Bird()
grupo_bird.add(passaro)

clock = pygame.time.Clock()
tela_inical = True
game_over = False

gravidade = 30

while True:
    while tela_inical:
        passaro.rect.topleft = 170, 330
        msg.update(get_ready=True)
        for ev in pygame.event.get():
            if ev.type == QUIT:
                pygame.quit()
                exit()
            if ev.type == KEYDOWN:
                if ev.key == K_SPACE or ev.key == K_UP or ev.key == K_w:
                    print(f"pontos: {pontos}")
                    tela_inical = False

        clock.tick(30)

        pygame.display.update()
        grupo_background.draw(tela)
        grupo_background.update()

        grupo_bird.draw(tela)
        grupo_bird.update()

        grupo_msg.draw(tela)
        grupo_msg.update()

    for ev in pygame.event.get():
        if ev.type == QUIT:
            print(f"pontos: {pontos}")
            pygame.quit()
            exit()
        if ev.type == KEYDOWN:
            if ev.key == K_SPACE or ev.key == K_UP or ev.key == K_w:
                passaro.y -= 30

    if cano.x == passaro.x:
        cano.altura = randint(-250, 3)
        cano2.altura = cano.altura + 450
        cano.x = x_tela
        cano2.x = x_tela
        pontos += 1
        if num.atual == 9:
            num.atual = 0
        else:
            num.atual += 1

    if passaro.rect.colliderect(base.rect) or passaro.rect.colliderect(cano.rect) or passaro.rect.colliderect(cano2.rect):
        msg.update(gameover=True)
        grupo_msg.draw(tela)
        grupo_msg.update()
        game_over = True
        while game_over:
            for evn in pygame.event.get():
                if evn.type == QUIT:
                    print(f"pontos: {pontos}")
                    pygame.quit()
                    exit()
                if evn.type == KEYDOWN:
                    if evn.key == K_SPACE or evn.key == K_UP or evn.key == K_w:
                        print(f"pontos: {pontos}")
                        passaro.reset()
                        num.reset()
                        pontos = 0
                        fundo.reset()
                        cano.altura = randint(-250, 3)
                        cano2.altura = cano.altura + 450
                        cano.x = x_tela
                        cano2.x = x_tela
                        game_over = False

            pygame.display.update()


    clock.tick(30)

    #cair
    gravidade = 3
    passaro.x = 50
    passaro.y += gravidade

    #fundo
    grupo_background.draw(tela)
    grupo_background.update()

    #pássaro
    grupo_bird.draw(tela)
    grupo_bird.update()

    #cano1
    grupo_cano.draw(tela)
    grupo_cano.update()


    #cano2
    grupo_cano2.draw(tela)
    grupo_cano2.update()

    #chao
    grupo_base.draw(tela)
    grupo_base.update()

    #pontos
    grupo_num.draw(tela)
    grupo_num.update()

    pygame.display.flip()

