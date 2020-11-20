from matrix import *
import time
import pygame

pygame.init()

def draw_matrix(m):
    array = m.get_array()
    for y in range(m.get_dy()):
        for x in range(m.get_dx()):
            if array[y][x] == 0:
                print("□", end='')
            elif array[y][x] == 1:
                print("■", end='')
            else:
                
                print("XX", end='')
        print()

flight =[[0,1,1],[1,1,0],[0,1,1]]

iScreenDy=16
iScreenDx=32
top=7
left = 27

ArrayScreen=[
               [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],       #0
               [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],   
               [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],       #2
               [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
               [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],       #4
               [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
               [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],       #6
               [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
               [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],       #8
               [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
               [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],       #10
               [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
               [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],       #12
               [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
               [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],       #14
               [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]      
            ]

block =[
    [0],
    [0],
    [0],
    [2],
    [2],
    [0],
    [2],
    [2],
    [0],
    [2],
    [2],
    [0],
    [2],
    [2],
    [0],
    [0]
    ]

bim =[1,1]

b1=block
b2=block
b3=block

b1Blk=Matrix(b1)
b2Blk=Matrix(b2)
b3Blk=Matrix(b3)


iScreen = Matrix(ArrayScreen)
oScreen = Matrix(iScreen)
flightBlk=Matrix(flight)
tempBlk = iScreen.clip(top, left, top+flightBlk.get_dy(), left+flightBlk.get_dx())
tempBlk = tempBlk + flightBlk
oScreen.paste(tempBlk, top, left)

b1top,b2top,b3top=0,0,0
b1left,b2left,b3left=1,3,5
tempBlk = iScreen.clip(b1top, b1left, b1top+b1Blk.get_dy(), b1left+b1Blk.get_dx())
tempBlk = tempBlk + b1Blk
iScreen.paste(tempBlk, b1top, b1left)
tempBlk = iScreen.clip(b2top, b2left, b2top+b2Blk.get_dy(), b2left+b2Blk.get_dx())
tempBlk = tempBlk + b2Blk
iScreen.paste(tempBlk, b2top, b2left)
tempBlk = iScreen.clip(b3top, b3left, b3top+b3Blk.get_dy(), b3left+b3Blk.get_dx())
tempBlk = tempBlk + b3Blk
iScreen.paste(tempBlk, b3top, b3left)
oScreen=Matrix(iScreen)
draw_matrix(oScreen);print()

def shoot():
    pass
#공을 발사하는 함수 정의해야 할듯

while True:
    key = input('Enter a key from [ q : quit, a : move left, d : move right, \' \' : shoot] : ')
    if key == 'q':   # exit; 
        print('Game terminated...')
        break
    elif key == 'a': # move left
        top+=1
    elif key == 'd': # move right
        top-=1
    elif key == ' ': # shoot
        shoot()    #not implemented; flight의 (1,0)좌표에서(top+1, left)부터 왼쪽으로 쭉 이동하게끔 time.sleep 사용하면 될 듯
        # 공 발사 함수 사전에 정의하고 쓰면 될 듯 
    """
    tempBlk = iScreen.clip(b1top, b1left, b1top+b1Blk.get_dy(), b2left+b2Blk.get_dx())
    tempBlk = tempBlk + b1Blk
    oScreen.paste(b1Blk, b1top, b1left)
    tempBlk = iScreen.clip(b2top, b2left, b2top+b2Blk.get_dy(), b2left+b2Blk.get_dx())
    tempBlk = tempBlk + b2Blk
    oScreen.paste(b2Blk, b2top, b2left)
    tempBlk = iScreen.clip(b3top, b3left, b3top+b3Blk.get_dy(), b3left+b3Blk.get_dx())
    tempBlk = tempBlk + b3Blk
    oScreen.paste(b3Blk, b3top, b3left)
    """

    
    if tempBlk.anyGreaterThan(1):
        if key == 'a': # undo: move right
            top-= 1
        elif key == 'd': # undo: move left
            top+=1
           #공 발사후에 충돌후 코드 작성 부분 ?

        tempBlk = iScreen.clip(top, left, top+flightBlk.get_dy(), left+flightBlk.get_dx())
        tempBlk = tempBlk + flightBlk
    oScreen=Matrix(iScreen)
    oScreen.paste(tempBlk, top, left)
    
    
    
    draw_matrix(oScreen); print()

