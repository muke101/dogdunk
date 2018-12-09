import pygame, sys

pygame.init()

doggu = pygame.image.load("assets/spr_dog_1.png")
doggu_rect = doggu.get_rect()

# Helpers
def compPos(pos_a,pos_b):
    return pos_a.x == pos_b.x and pos_a.y == pos_b.y
"""
class Game:
    def __init__(self, play_action, stop_action):
        self.play = play
        self.stop = stop
        
    def runOption(option_name):
        for opt in options:
            if opt["name"] == menuOption["name"]:
                opt

    def runPress(pos):
        if pos == play_area:
            play_area.run()
        else:
            stop_area.run()
            
def mouseHandler(event,state):
    if state == "menu":
        if event.type == pygame.MOUSEMOTION:
            pos = event.pos
            mainMenu.handle((x,y))
"""     
# Actual instances
# Menu options
startOption = { "name": "Start Game", "rect": (0,0,600,200) }
quitOption = { "name": "Quit", "rect": (0,200,600,400) }

menuOptions = [startOption, quitOption]

# mainMenu = MenuState(menuOptions)

sprite_names = ["spr_dog_1.png","spr_dog_2.png","spr_dog_3.png","spr_dog_4.png"]
sprite_paths = ["assets/" + s for s in sprite_names]
image_data = [pygame.image.load(path) for path in sprite_paths]

def updateCounter(c,lim):
    if c >= lim: return 0
    return c + 1

def main():
    width, height = 600, 400
    size = (width,height)
    screen = pygame.display.set_mode(size)
    doggu_rect = 0, 0, 300, 300
    anim_counter = 0
    while True: # Game Loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        # Update current game state
        anim_counter = updateCounter(anim_counter,3)
        
        screen.fill((0,0,0))
        screen.blit(image_data[anim_counter],doggu_rect)
        pygame.display.flip()

main()
