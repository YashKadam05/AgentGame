import pygame
pygame.init()
width,height=800,600
win=pygame.display.set_mode((width,height))
pygame.display.set_caption("Mission E-X18")
clock=pygame.time.Clock()

white=(255,255,255)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
black=(0,0,0)


bgx,bgy=0,0
# bgx,bgy=-10968,0
bg=[pygame.image.load('backgrounds/bg1.png'),pygame.image.load('backgrounds/bg2.png'),pygame.image.load('backgrounds/bg3.png'),pygame.image.load('backgrounds/bg4.png'),pygame.image.load('backgrounds/bg5.png'),pygame.image.load('backgrounds/bg6.2.png'),pygame.image.load('backgrounds/bg7.png'),pygame.image.load('backgrounds/bg8.png'),pygame.image.load('backgrounds/bg8.png'),pygame.image.load('backgrounds/bg8.png'),pygame.image.load('backgrounds/bg8.png'),pygame.image.load('backgrounds/bg8.png'),pygame.image.load('backgrounds/bg8.png'),pygame.image.load('backgrounds/bg8.png'),pygame.image.load('backgrounds/bg9.png'),pygame.image.load('backgrounds/bg10.png')]

def background():
    win.blit(bg[0],(bgx,bgy))
    win.blit(bg[1],(bgx+width,bgy))
    win.blit(bg[2],(bgx+width+width,bgy))
    win.blit(bg[3],(bgx+width+width+width,bgy))
    win.blit(bg[4],(bgx+width+width+width+width,bgy))
    win.blit(bg[5],(bgx+width+width+width+width+width,bgy))
    win.blit(bg[6],(bgx+width+width+width+width+width+width,bgy))
    win.blit(bg[7],(bgx+width+width+width+width+width+width+width,bgy))

    win.blit(bg[8],(bgx+width+width+width+width+width+width+width+width,bgy))
    win.blit(bg[9],(bgx+width+width+width+width+width+width+width+width+width,bgy))
    win.blit(bg[10],(bgx+width+width+width+width+width+width+width+width+width+width,bgy))
    win.blit(bg[11],(bgx+width+width+width+width+width+width+width+width+width+width+width,bgy))
    win.blit(bg[12],(bgx+width+width+width+width+width+width+width+width+width+width+width+width,bgy))
    win.blit(bg[13],(bgx+width+width+width+width+width+width+width+width+width+width+width+width+width,bgy))
    win.blit(bg[14],(bgx+width+width+width+width+width+width+width+width+width+width+width+width+width+width,bgy))
    win.blit(bg[15],(bgx+width+width+width+width+width+width+width+width+width+width+width+width+width+width+width,bgy))

heroS=[pygame.image.load('hero/Standing.png')]
heroR=[pygame.image.load('hero/R1.png'),pygame.image.load('hero/R2.png'),pygame.image.load('hero/R3.png'),pygame.image.load('hero/R4.png'),pygame.image.load('hero/R5.png'),pygame.image.load('hero/R6.png'),pygame.image.load('hero/R7.png'),pygame.image.load('hero/R8.png'),pygame.image.load('hero/R9.png')]
heroL=[pygame.image.load('hero/L1.png'),pygame.image.load('hero/L2.png'),pygame.image.load('hero/L3.png'),pygame.image.load('hero/L4.png'),pygame.image.load('hero/L5.png'),pygame.image.load('hero/L6.png'),pygame.image.load('hero/L7.png'),pygame.image.load('hero/L8.png'),pygame.image.load('hero/L9.png')]
speed=5
i=0
xh,yh=120,380
# xh,yh=120,462
def Hero():
    global xh,yh,i,bgx,sx,si,cx
    keys=pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        # yh-=speed
        i+=1
        bgx-=speed
        sx-=speed
        cx-=speed
        if i>=9:
            i=0
        # print(sx,sy)
        logic()
        win.blit(heroR[i],(xh,yh))
    elif keys[pygame.K_LEFT]:
        # yh+=speed
        i+=1
        bgx+=speed
        sx+=speed
        cx+=speed
        si=0
        if i>=9:
            i=0
        # print(sx,sy)
        logic()
        win.blit(heroL[i],(xh,yh))
    elif keys[pygame.K_UP]:
        win.blit(heroR[1],(xh,yh))
        logic()
    else:
        win.blit(heroS[0],(xh,yh))


jumpHeight=25
vel=jumpHeight
gravity=5
jumping=False
def jump():
    global jumping,vel,yh,si
    if jumping:
        yh-=vel
        vel-=gravity
        # print(xh,yh)
    if vel<-jumpHeight:
        jumping=False
        si=2
        vel=jumpHeight


# someCase=True
someCase=True
someCase2=True
someCase3=True
def logic():
    global yh,bgx,someCase,someCase2,sx,cx,ci,speed,sv,cv,someCase3,cy,run
    keys=pygame.key.get_pressed()
    #slide
    if bgx<-760 and bgx>-1110 and someCase:
        if keys[pygame.K_RIGHT]:
            yh-=2
        elif keys[pygame.K_LEFT]:
            yh+=2
    #boxJump
    if bgx<=-1560 and yh>=240 and someCase:
        bgx=-1560
        if keys[pygame.K_RIGHT] and keys[pygame.K_SPACE] and yh>=167:
            bgx-=speed
            yh=190
    if keys[pygame.K_LEFT] and yh==190 and bgx>=-1560 and someCase:
        yh=242

    if bgx<=-1935 and yh>=190 and someCase:
        bgx=-1935
        if keys[pygame.K_RIGHT] and keys[pygame.K_SPACE] and yh>=115:
            bgx-=speed
            yh=134
    if keys[pygame.K_LEFT] and yh==134 and bgx>=-1935 and someCase:
        yh=190

    #hole
    if bgx<=-2260 and bgx>=-2285 and yh==134 and keys[pygame.K_RIGHT] and someCase2:
        someCase=False
        yh=400
        bgx=-2260
        #remove
        run=False
        print("You Fall in Hole")
    #holes
    if bgx<=-3060 and bgx>=-3085 and yh==326 and keys[pygame.K_RIGHT] and someCase2:
        someCase=False
        yh=400
        bgx=-3070
        #remove
        run=False
        print("You Fall in Hole")
    elif bgx<=-3160 and bgx>=-3185 and yh==326 and keys[pygame.K_RIGHT] and someCase2:
        someCase=False
        yh=400
        bgx=-3170
        #remove
        run=False
        print("You Fall in Hole")
    elif bgx<=-3260 and bgx>=-3285 and yh==326 and keys[pygame.K_RIGHT] and someCase2:
        someCase=False
        yh=400
        bgx=-3270
        #remove
        run=False
        print("You Fall in Hole")
    elif bgx<=-3360 and bgx>=-3385 and yh==326 and keys[pygame.K_RIGHT] and someCase2:
        someCase=False
        yh=400
        bgx=-3370
        #remove
        run=False
        print("You Fall in Hole")

    #slide
    if bgx<-2420 and bgx>-2665 and someCase2:
        someCase=False
        if keys[pygame.K_RIGHT]:
            yh+=4
        elif keys[pygame.K_LEFT]:
            yh-=4

    #slide
    if bgx<-3970 and bgx>-4065 and someCase2:
        someCase=False
        if keys[pygame.K_RIGHT]:
            yh-=3
        elif keys[pygame.K_LEFT]:
            yh+=3
    if bgx<-4165 and bgx>=-4265 and someCase2:
        someCase=False
        yh=326
    if keys[pygame.K_LEFT] and bgx==-4165:
        someCase=False
        someCase2=False
        bgx-=speed
        sx-=speed
    #bridge
    if bgx <= -4335 and bgx >= -4608 and keys[pygame.K_LEFT]:
        bg[5]=pygame.image.load('backgrounds/bg6.png')
        #remove
        run=False
        print("You got Drowned")

    if bgx == -4610:
        someCase=False
        someCase2=False
        bg[5]=pygame.image.load('backgrounds/bg6.png')
        sx-=speed
        bgx-=speed

    # wall
    if bgx<=-4675 and yh==326 and keys[pygame.K_RIGHT]:
        someCase=False
        someCase2=False
        bgx=-4675

    # climb
    if bgx<=-4675 and bgx>=-4720 and keys[pygame.K_UP]:
        yh-=8
        if yh<=69:
            yh=69
    # wall
    if bgx>=-4675 and yh==69 and keys[pygame.K_LEFT]:
        someCase=False
        someCase2=False
        bgx=-4675
        sx-=speed
        cx-=speed

    # fall
    if bgx<=-4760 and bgx>=-4805 and yh==69 and keys[pygame.K_RIGHT]:
        someCase=False
        someCase2=False
        yh=210
        bgx=-4760
    # wall
    if bgx>=-4760 and yh==210 and keys[pygame.K_LEFT]:
        someCase=False
        someCase2=False
        bgx=-4760
        sx-=speed
        cx-=speed

    # fall
    if bgx<=-5465 and bgx>=-5500 and yh==210 and keys[pygame.K_RIGHT]:
        someCase=False
        someCase2=False
        yh=462
        bgx=-5465

    # wall
    if bgx>=-5460 and yh==462 and keys[pygame.K_LEFT]:
        someCase=False
        someCase2=False
        bgx=-5460
        sx-=speed
        cx-=speed
    # cobra
    if bgx<=-5560 and bgx>=-10308 and someCase3:
        sv=False
        cv=True
        if keys[pygame.K_RIGHT]:
            cx-=5
            ci+=1
            if ci>=7:
                ci=0
        if keys[pygame.K_SPACE]:
            speed+=1

    if bgx<=-10308:
        cv=False
        someCase3=False
        speed=5
    if cx>=140 and cx<=160 and yh==462:
        run=False
        print("eaten by cobra")

    # wall
    if bgx<=-11078 and yh==462 and keys[pygame.K_RIGHT]:
        someCase=False
        someCase2=False
        bgx=-11078
        sx+=speed
        cx+=speed
    # climb
    if bgx<=-11078 and bgx>=-11200 and keys[pygame.K_UP]:
        yh-=8
        if yh<=69:
            yh=69
    # wall
    if bgx>=-11058 and yh==69 and keys[pygame.K_LEFT]:
        someCase=False
        someCase2=False
        someCase3=False
        bgx=-11058
        sx-=speed
        cx-=speed
    # fall
    if bgx<=-11183 and bgx>=-11283 and yh==69 and keys[pygame.K_RIGHT]:
        someCase=False
        someCase2=False
        someCase3=False
        yh=377
        bgx=-11188
    # wall
    if bgx>=-11188 and yh==377 and keys[pygame.K_LEFT]:
        someCase=False
        someCase2=False
        someCase3=False
        bgx=-11188
        sx-=speed
        cx-=speed
    #end
    if yh==377 and bgx<=-12283:
        run=False
        print("Bomb Planted, MISSION ACCOMPLISHED!")


scorpio=[pygame.image.load('JungleEntities/scorpio.png'),pygame.image.load('JungleEntities/scorpio2.png'),pygame.image.load('JungleEntities/scorpio3.png')]
sx,sy=4300,326
si=0
sv=True
def Scorpio():
    if sv:
        win.blit(scorpio[si],(sx+192,sy+5))
    # print(sx,sy)

cobra=[pygame.image.load('JungleEntities/CL1.png'),pygame.image.load('JungleEntities/CL2.png'),pygame.image.load('JungleEntities/CL3.png'),pygame.image.load('JungleEntities/CL4.png'),pygame.image.load('JungleEntities/CL5.png'),pygame.image.load('JungleEntities/CL6.png'),pygame.image.load('JungleEntities/CL7.png')]
cx,cy=1520,472
ci=0
cv=False
def Cobra():
    global cx,cv
    if cv:
        win.blit(cobra[ci],(cx,cy))
        if cx<=-60:
            cx=600


# sfx=pygame.mixer.Sound("spyMusic.wav")
# sfx.play()
pygame.mixer.init()
pygame.mixer.music.load("spyMusic.wav")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.4)

run=True
while run:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                jumping=True
                si=0

    background()
    Hero()
    Scorpio()
    Cobra()
    jump()
    pygame.display.update()

pygame.quit()
