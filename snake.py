import pygame,sys,random

pygame.init()
ppi=(960,540)
screen=pygame.display.set_mode(ppi)
pygame.display.set_caption("snake")

green=(83,224,45)
black=(0,0,0)
yellow=(249,236,24)

pygame.mixer.music.load("缘结神.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

rect=pygame.Rect(0,0,25,25)

class snake:
    def __init__(self):
        self.body=[]
        self.body.append(rect)
        self.direction=pygame.K_RIGHT
        for i in range(3):
            self.add()
    def add(self):
        new=pygame.Rect(self.body[0].x,self.body[0].y,25,25)
        if self.direction==pygame.K_RIGHT:
            new.x+=25
        elif self.direction==pygame.K_LEFT:
            new.x-=25
        elif self.direction==pygame.K_UP:
            new.y-=25
        elif self.direction==pygame.K_DOWN:
            new.y+=25
        self.body.insert(0,new)
    def drive(self,command):
        x=(pygame.K_RIGHT,pygame.K_LEFT)
        y=(pygame.K_UP,pygame.K_DOWN)
        if (self.direction in x and command in x) or (self.direction in y and command in y):
            pass
        else:
            self.direction=command
    def delete(self):
        self.body.pop()
    def move(self):
        self.add()
        self.delete()
    def circle(self):
        for i in self.body:
            if i.x>960:
                i.x-=960
            elif i.x<0:
                i.x+=960
            if i.y<0:
                i.y+=540
            elif i.y>540:
                i.y-=540

green_snake=snake()

class food:
    def new(self):
        self.x=random.randint(0,935)
        self.y=random.randint(0,515)
        self.rect=pygame.Rect(self.x,self.y,25,25)
    def happen(self):
        pygame.draw.rect(screen,yellow,self.rect)

yellow_food=food()
yellow_food.new()

def get(snake,food):
    for i in snake.body:
        if -25<=i.x-food.x<=25 and -25<=i.y-food.y<=25:
            return True
        else:
            return False

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            green_snake.drive(event.key)

    green_snake.move()
    green_snake.circle()

    a=get(green_snake,yellow_food)
    if a==True:
        green_snake.add()
        yellow_food.new()

    screen.fill(black)

    yellow_food.happen()

    for i in green_snake.body:
        pygame.draw.rect(screen,green,i)

    pygame.display.flip()

    time=pygame.time.Clock()
    time.tick(15)