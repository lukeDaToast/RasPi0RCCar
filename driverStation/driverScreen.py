import pygame
import pygame_gui
import controllers

pygame.init()

ZEROED = (0,0)

#display setup
pygame.display.set_caption('Driver Screen')
MAXx = 1024
MAXy = 600
MAXES = (MAXx, MAXy)
window_surface = pygame.display.set_mode((MAXx, MAXy))
#displaySurface = pygame.display.set_mode((X, Y))

#Background setup
background = pygame.Surface((MAXx, MAXy))
backdrop = pygame.image.load("driverStationTemplatev2.jpg")
backdrop = pygame.transform.scale(backdrop, (MAXx, MAXy))

startingScreen = pygame.image.load("driverStationStart.jpg")
startingScreen = pygame.transform.scale(startingScreen, (MAXx, MAXy))
background.blit(startingScreen, ZEROED)

#Mangager setup
manager = pygame_gui.UIManager(MAXES)

#Start button
startButton = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 275), (100, 50)),text='Start', manager=manager)

#Clock setup
clock = pygame.time.Clock()
is_running = True

#Text setup
font = pygame.font.SysFont('franklingothicmedium', 100, bold=True) 
text = ''



def main():
    text = controllers.main()
    print(text)
    text = str(text)


while is_running:
    timeDelta = clock.tick(60)/1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running= False
        manager.process_events(event)

        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == startButton:
                  startButton.hide()
                  startButton.disable()
                  background.blit(backdrop, (0,0))
                  endButton = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((25, 540), (100, 50)),text='Quit', manager=manager)

                  main()
                  
                  batteryLevel = pygame.font.SysFont('franklingothicmedium', 75, bold=True) 
                  words = font.render('hello',True, pygame.Color(39, 193, 178))
                  background.blit(words, (300,300))


            if event.ui_element == endButton:
                is_running = False
                  
                  
                  
                  
   
    manager.update(timeDelta)
    
    window_surface.blit(background, (0,0))
    manager.draw_ui(window_surface)

    pygame.display.update()
