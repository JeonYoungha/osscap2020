from matrix import *
import time

def draw_matrix(m):
    array = m.get_array()
    for y in range(m.get_dy()):
        for x in range(m.get_dx()):
            if array[y][x] == 0 or array[y][x] ==5:
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
               [1,2,0,2,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
               [1,2,0,2,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],       #4
               [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
               [1,2,0,2,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],       #6
               [1,2,0,2,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
               [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],       #8
               [1,2,0,2,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
               [1,2,0,2,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],       #10
               [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
               [1,2,0,2,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],       #12
               [1,2,0,2,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
               [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],       #14
               [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]      
            ]
#arrayscreen에 깨야 하는 블록까지 구현했음
#추후 난이도 조절이나 맵등을 고려해서 arrayscreen을 여러개 만들고 선택하는 방향

bim =[[3]]          #bim = 비행체에서 발사되는 빔, 장애물에 맞은 후 제어 코드 필요


iScreen = Matrix(ArrayScreen)
oScreen = Matrix(iScreen)


flightBlk=Matrix(flight)
flttempBlk = iScreen.clip(top, left, top+flightBlk.get_dy(), left+flightBlk.get_dx())
flttempBlk = flttempBlk + flightBlk
oScreen.paste(flttempBlk, top, left)
draw_matrix(oScreen);print()
bimBlk = Matrix(bim)
"""
def shoot():
    bimBlk = Matrix(bim)       #bim의 x,y좌표값이 필요 // x값을 -1씩 변화시켜야함
    global bimtop, bimleft
#아래 코드는 for 루프를 돌아야함 bimleft를 변화시키면서
    while bimleft!=5:
        tempBlk=iScreen.clip(bimtop,bimleft,bimtop+3,bimleft+3)             #left 값은 불변;
        tempBlk+=tempBlk + bimBlk
        oScreen.paste(tempBlk, bimtop,bimleft)
        draw_matrix(oScreen);print()
        bimleft-=1
    #수정해야 하는 상황 : 변경된 top,left값을 받아오지 못함;
    # ++ iScreen을 업데이트해서 지나온 빔은 삭제하고 업데이트 해야함
#공을 발사하는 함수 정의해야 할듯
"""
#iScreen이 의미하는 것 = block+ 배경
# while 루프 돌면서 array[y][x]==4 or 5일때 ArrayScreen 수정
# 

while True:
    bimtop=top+1
    bimleft=left-1
    key = input('Enter a key from [ q : quit, a : move left, d : move right, \' \' : shoot] : ')
    if key == 'q':   # exit; 
        print('Game terminated...')
        break
    elif key == 'a': # move left
        top+=1
    elif key == 'd': # move right
        top-=1
    if key == ' ': # shoot
        
        while bimleft!=5:             # while 무한루프를 돌고 배열의 값이 3보다 크거나 같으면
                             # 빔 없애고 장애물 없애는 등 제어

            time.sleep(0.2)
            bimtempBlk=iScreen.clip(bimtop,bimleft,bimtop+1,bimleft+1)             #left 값은 불변;
            bimtempBlk+=bimtempBlk + bimBlk
            oScreen=Matrix(iScreen)
            oScreen.paste(bimtempBlk, bimtop,bimleft)
            tempBlk = iScreen.clip(top, left, top+flightBlk.get_dy(), left+flightBlk.get_dx())
            tempBlk = tempBlk + flightBlk
            oScreen.paste(tempBlk, top, left)
            draw_matrix(oScreen);print()
            bimleft-=1            
            
        continue   #continue 대신 충돌에 대한 코드 작성

    
        # 공 발사 함수 사전에 정의하고 쓰면 될 듯 
    

    


    tempBlk = iScreen.clip(top, left, top+flightBlk.get_dy(), left+flightBlk.get_dx())
    tempBlk = tempBlk + flightBlk
    oScreen=Matrix(iScreen)
    oScreen.paste(tempBlk, top, left)
    
    
    
    draw_matrix(oScreen); print()
