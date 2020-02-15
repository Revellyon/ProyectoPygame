import pygame as pg
from pygame.locals import *
import sys , os
from random import randint
from pygame import *
from Nave import *
from Asteroides import *
from explosion import *
from texto import *
FPS = 60

class Juego():
    clock = pg.time.Clock()
    def __init__(self):
       
        self.player_group = pg.sprite.Group()
        self.asteroid_group = pg.sprite.Group()      
        self.all_group = pg.sprite.Group()

        
        self.texto = Texto()
        self.ship = Nave(10, 300)
        self.player_group.add(self.ship)
        self.ship.lives = 2

        self.contador = 0   
        self.puntuacion = 0

        self.all_group.add(self.ship, self.asteroid_group)
        self.default_font = pg.font.Font(None, 28)

        self.meteor_max = 0
        self.meteor_creados = 0
        self.ultimo_meteor = FPS * 12
        self.nuevo_meteor = FPS// 4
        
        self.expl= []

        self.aux = 1
        self.texto.run1()
        
    def nuevoMeteor(self,dt):
        self.ultimo_meteor += dt
        if self.ultimo_meteor >= self.nuevo_meteor:
            nuevo = Meteor( x=randint(800,1000), y=randint(10, 550))
            nuevo.speed = randint(1,4)
        self.asteroid_group.add(nuevo)
        self.ultimo_meteor = 0

    def nuevoMeteor2(self,dt):
        self.meteor_max = 20
        self.ultimo_meteor += dt
        if self.ultimo_meteor >= self.nuevo_meteor:
            nuevo = Meteor( x=randint(800,1000), y=randint(10, 550))
            nuevo.speed = randint(4,6)
        self.asteroid_group.add(nuevo)
        self.ultimo_meteor = 0

    def quitGame(self):
        while True:
            for event in pg.event.get():
                if event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                            pg.quit()
                            sys.exit()

    def handleEvents(self):
        for event in pg.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                        pg.quit()
                        sys.exit()
           
                if event.key == K_UP:
                    self.ship.go_up()

                if event.key == K_DOWN:
                    self.ship.go_down()
       
        keys_pressed = pg.key.get_pressed()
        if keys_pressed[K_UP]:
            self.ship.go_up()
            self.ship.speed +=0.4
        if keys_pressed[K_DOWN]:
            self.ship.go_down()
            self.ship.speed +=0.4
       
        if keys_pressed[K_UP] == False and keys_pressed[K_DOWN] == False:
            self.ship.speed = 5

    def start_screen(self):
        while True:
            self.texto.screen.blit(self.texto.background_menu,(0,0))
            rect = self.texto.text_titulo.get_rect()
            self.texto.screen.blit(self.texto.text_titulo,((800 - rect.w)//2,100))
            rect = self.texto.text_insert_coin.get_rect()
            self.texto.screen.blit(self.texto.text_insert_coin,((800 - rect.w)//2,330)) 
            self.texto.screen.blit(self.texto.text_instructions,(50,560))
            self.texto.screen.blit(self.texto.text_story,(500,560))
            self.ship.lives = 5
            
            pg.display.update()
            for event in pg.event.get():

                if event.type == KEYDOWN:
                        if event.key == K_i:
                            #self.texto.run3()
                            self.texto.run7()
                            self.rules_screen()
                            return
               
                        if event.key == K_SPACE:                                    
                            self.texto.run4()        
                            self.level_1()
                            
                            return
                
                        if event.key == K_s:
                            #self.texto.run3()
                            self.texto.run6()
                            self.Story_screen()
                            return

                
                        if event.key == K_ESCAPE:
                            pg.quit()
                            sys.exit()
    
    def rules_screen(self):
        while True:
            self.texto.screen.blit(self.texto.background_rules,(0,0))
            self.texto.screen.blit(self.texto.text_controlesU,(100, 100))
            self.texto.screen.blit(self.texto.text_controlesD,(100,200))
            self.texto.screen.blit(self.texto.UP,(170,100))
            self.texto.screen.blit(self.texto.DOWN,(170,200))            
            self.texto.screen.blit(self.texto.text_controlesS,(100,300))
            self.texto.screen.blit(self.texto.text_controlesE,(100,400))
            self.texto.screen.blit(self.texto.UP,(340,300))
            self.texto.screen.blit(self.texto.DOWN,(270,300))
            rect = self.texto.text_return.get_rect()
            self.texto.screen.blit(self.texto.text_return,((800 - rect.w)//2,560))

            pg.display.update()
            for event in pg.event.get():
                if event.type == KEYDOWN:
                        if event.key == K_SPACE:
                            #self.texto.run2() 
                            self.texto.run1()
                            self.start_screen()
                            return
                
                        if event.key == K_ESCAPE:
                            pg.quit()
                            sys.exit()
    
    def Story_screen(self):
        while True:
            self.texto.screen.blit(self.texto.background_story,(0,0))
            rect = self.texto.text_return.get_rect()
            self.texto.screen.blit(self.texto.text_return,((800 - rect.w)//2,560))
            self.texto.screen.blit(self.texto.text_historia1,(50, 25))
            self.texto.screen.blit(self.texto.text_historia2,(50, 75))
            self.texto.screen.blit(self.texto.text_historia3,(50, 125))
            self.texto.screen.blit(self.texto.text_historia4,(50, 175))
            self.texto.screen.blit(self.texto.text_historia5,(50, 225))
            self.texto.screen.blit(self.texto.text_historia6,(50, 275))
            self.texto.screen.blit(self.texto.text_historia7,(50, 325))
            self.texto.screen.blit(self.texto.text_historia8,(50, 375))
            self.texto.screen.blit(self.texto.text_historia9,(50, 425))
            self.texto.screen.blit(self.texto.text_historia10,(230, 475))
            
            pg.display.update()
            for event in pg.event.get():
                if event.type == KEYDOWN:
                        if event.key == K_SPACE:
                            #self.texto.run2()
                            self.texto.run1()
                            self.start_screen()
                            return
                
                        if event.key == K_ESCAPE:
                            pg.quit()
                            sys.exit()
    
    def level_1(self):
        while True:

            dt = self.clock.tick(FPS)
            
            tiempo =  pg.time.get_ticks()/1000
            if self.aux==tiempo:
                self.aux+=1
                print(tiempo)
            


            self.handleEvents()
            self.meteor_max = 15     
            if len(self.asteroid_group) == 14:
                self.puntuacion += 5
         
            self.colisiones()
            
            self.all_group.update(dt)
            self.all_group.draw(self.texto.screen) 
            
            pintados = len(self.asteroid_group)
            if pintados < self.meteor_max:
                self.nuevoMeteor(dt)

            self.texto.screen.blit(self.texto.background_img,(0,0))           
            self.livescounter = self.texto.fontP.render(str(self.ship.lives), True, WHITE)
            self.marcador = self.texto.fontP.render(str(self.puntuacion), True, WHITE)
            self.all_group.update(dt)
            self.all_group.draw(self.texto.screen)     

            self.asteroid_group.update(dt)
            self.asteroid_group.draw(self.texto.screen)           
            self.texto.screen.blit(self.livescounter, (100, 10))
            self.texto.screen.blit(self.marcador, (660, 10))

            if self.puntuacion == 50:
                self.puntuacion += 150
                self.level_complete()

            if self.ship.lives == 0:
                self.texto.run8()
                
                self.gameOver()

            pg.display.flip()

            
        self.quitGame()

    def level_complete(self):
        while True:
            dt = self.clock.tick(FPS)
            
            self.marcador = self.texto.fontP.render(str(self.puntuacion), True, WHITE)
            
            self.colisiones()
            if self.puntuacion == 200:
                self.texto.screen.blit(self.texto.background_img,(0,0))

            if self.puntuacion == 450:
                self.texto.screen.blit(self.texto.background_image,(0,0))

            self.livescounter = self.texto.fontP.render(str(self.ship.lives), True, WHITE)
            

            self.all_group.update(dt)
            self.all_group.draw(self.texto.screen)     

            self.asteroid_group.update(dt)
            self.asteroid_group.draw(self.texto.screen)

            self.texto.screen.blit(self.livescounter, (100, 10))
            self.texto.screen.blit(self.marcador, (660, 10))

            rect = self.texto.text_win.get_rect()
            self.texto.screen.blit(self.texto.text_win, ((800 - rect.w)//2, 230))
            rect = self.texto.text_level.get_rect()
            self.texto.screen.blit(self.texto.text_level, ((800 - rect.w)//2, 310))
            
            if self.ship.lives == 0:
                #self.texto.run8()
                
                self.gameOver()
            
            pg.display.flip()

            pg.display.update() 

            for event in pg.event.get():
                    if event.type == KEYDOWN:
                            if event.key == K_SPACE:                                
                                self.asteroid_group.empty()
                                                            
                                self.level_2()
                                return
                            if event.key == K_UP:
                                self.ship.go_up()

                            if event.key == K_DOWN:
                                self.ship.go_down()
       
            keys_pressed = pg.key.get_pressed()
            if keys_pressed[K_UP]:
                self.ship.go_up()
                self.ship.speed +=0.4
            if keys_pressed[K_DOWN]:
                self.ship.go_down()
                self.ship.speed +=0.4
        
            if keys_pressed[K_UP] == False and keys_pressed[K_DOWN] == False:
                self.ship.speed = 5

    def level_2(self):
        while True:
            dt = self.clock.tick(FPS)
                    
            self.handleEvents()
                  
            if len(self.asteroid_group) == 19:
                self.puntuacion += 5
         
            self.colisiones()
            
            self.all_group.update(dt)
            self.all_group.draw(self.texto.screen) 

            pintados = len(self.asteroid_group)
            if pintados < self.meteor_max:
                self.nuevoMeteor2(dt)

            self.texto.screen.blit(self.texto.background_image,(0,0))           
            self.livescounter = self.texto.fontP.render(str(self.ship.lives), True, WHITE)
            self.marcador = self.texto.fontP.render(str(self.puntuacion), True, WHITE)
            self.all_group.update(dt)
            self.all_group.draw(self.texto.screen)     

            self.asteroid_group.update(dt)
            self.asteroid_group.draw(self.texto.screen)           
            self.texto.screen.blit(self.livescounter, (100, 10))
            self.texto.screen.blit(self.marcador, (660, 10))

            if self.puntuacion == 300:
                self.level_end()

            if self.ship.lives == 0:
                self.texto.run8()
                
                self.gameOver()

            pg.display.flip()

            
        self.quitGame()

    def level_end(self):
        while True:
            dt = self.clock.tick(FPS)
            
            self.colisiones()
            self.marcador = self.texto.fontP.render(str(self.puntuacion), True, WHITE)
            self.texto.screen.blit(self.texto.background_image,(0,0))
            self.livescounter = self.texto.fontP.render(str(self.ship.lives), True, WHITE)
            

            self.all_group.update(dt)
            self.all_group.draw(self.texto.screen)     

            self.asteroid_group.update(dt)
            self.asteroid_group.draw(self.texto.screen)

            self.texto.screen.blit(self.livescounter, (100, 10))
            self.texto.screen.blit(self.marcador, (660, 10))
            
            if self.ship.lives == 0:
                self.texto.run8()
                
                self.gameOver()
            
            #APARICION PLANETA Y ATERRIZAJE
            if len(self.asteroid_group) == 0:
                self.gameOver()


            pg.display.flip()

            pg.display.update() 

            for event in pg.event.get():
                    if event.type == KEYDOWN:   
                            if event.key == K_ESCAPE:
                                pg.quit()
                                sys.exit()                           
                            if event.key == K_UP:
                                self.ship.go_up()

                            if event.key == K_DOWN:
                                self.ship.go_down()
       
            keys_pressed = pg.key.get_pressed()
            if keys_pressed[K_UP]:
                self.ship.go_up()
                self.ship.speed +=0.4
            if keys_pressed[K_DOWN]:
                self.ship.go_down()
                self.ship.speed +=0.4
        
            if keys_pressed[K_UP] == False and keys_pressed[K_DOWN] == False:
                self.ship.speed = 5

    def gameOver(self):  
        while True:
            dt = self.clock.tick(FPS)
            if self.puntuacion <= 200:
                self.texto.screen.blit(self.texto.background_img,(0,0))
            
            if self.puntuacion > 200:
                self.texto.screen.blit(self.texto.background_image,(0,0))
             
            self.all_group.update(dt)
            self.all_group.draw(self.texto.screen)     

            self.asteroid_group.update(dt)
            self.asteroid_group.draw(self.texto.screen)

            self.texto.screen.blit(self.livescounter, (100, 10))
            self.texto.screen.blit(self.marcador, (660, 10))

            rect = self.texto.text_gameOver.get_rect()
            self.texto.screen.blit(self.texto.text_gameOver, ((800 - rect.w)//2, 200))
            rect = self.texto.text_insert_coin.get_rect()
            self.texto.screen.blit(self.texto.text_insert_coin, ((800 - rect.w)//2, 560))

            pg.display.flip()

            pg.display.update()       
            for event in pg.event.get():
                    if event.type == KEYDOWN:
                            if event.key == K_SPACE:
                                self.all_group.empty()
                                self.ship = Nave(10, 300)
                                self.player_group.add(self.ship)
                                self.all_group.add(self.ship)
                                self.asteroid_group.empty()
                                self.puntuacion = 0                                
                                self.texto.run1() 
                                self.start_screen()
                                return
                    if event.type == KEYDOWN:
                            if event.key == K_ESCAPE:
                                pg.quit()
                                sys.exit()

    def colisiones(self):
        if self.ship.lives > 1:
                self.colision = pg.sprite.groupcollide(self.asteroid_group, self.player_group, True, False  ) 
                for hit in self.colision:
                    self.expl = Explosion(hit.rect.center)
                    self.texto.run5()
                    self.all_group.add(self.expl)   
                        
                    self.contador += 1
                if self.contador > 0:              
                    self.ship.lives -= 1
        self.contador = 0

        if self.ship.lives == 1:
            self.colision = pg.sprite.groupcollide(self.player_group, self.asteroid_group, True, False)
            for hit in self.colision:
                self.expl = Explosion(hit.rect.center)
                self.texto.run5()
                self.all_group.add(self.expl)   
                self.contador += 1
            if self.contador > 0:              
                self.ship.lives -= 1
        self.contador = 0

    