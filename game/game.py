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
doggu_image_data = [pygame.image.load(path) for path in sprite_paths]
ball_image = pygame.image.load("assets/ball_normal.png")

movement_map = {
    "0": (200,200,500,500),
    "1": (100,100,400,400),
    "2": (120,120,380,380),
    "3": (80,80,220,220)
}

class Anim:
    def __init__(self,spd,frames,x,y,w,h,move_map):
        self.counter = 0
        self.speed = spd
        self.frame = 0
        self.frameCount = frames-1
        self.rect = x, y, w, h
        self.move_map = move_map
        
    def update(self):
        if self.counter >= self.speed:
            self.counter = 0
            if self.frame >= self.frameCount:
                self.frame = 0
            else:
                self.frame += 1
            self.rect = self.move_map[str(self.frame)]
        else:
            self.counter += 1

    def getFrame(self):
        return self.frame

    def getRect(self):
        return self.rect
    
    
def main():
    width, height = 600, 400
    size = (width,height)
    screen = pygame.display.set_mode(size)
    ball_rect = 0, 0, 100, 100
    new_ball_img = pygame.transform.scale(ball_image,(100,100))
    anim = Anim(500,4,0,0,0,0,movement_map)
    doggu_rect = anim.getRect()
    while True: # Game Loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
        
        screen.fill((0,0,0))
        screen.blit(doggu_image_data[anim.getFrame()],anim.getRect())
        screen.blit(new_ball_img,ball_rect)
        pygame.display.flip()

        anim.update()
main()
