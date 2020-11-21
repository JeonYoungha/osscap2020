from matrix import *
import time
import pygame as pg
import sys
import random

# 스페이스바 입력을 위한 pygame모듈 사용
screen = pg.display.set_mode((1, 1))


# Matrix m의 (y,x) 값에 따른 출력부
def draw_matrix(m):
    array = m.get_array()
    for y in range(m.get_dy()):
        for x in range(m.get_dx()):
            if array[y][x] == 0:
                print("□", end='')
            elif array[y][x] == 1:
                print("■", end='')
            elif array[y][x] == 2:
                print("◆", end='')
            elif array[y][x] == 3:
                print("●", end='')
            else:
                print("◆", end='')

        print()


# 스크린 크기와 비행체의 (top,left)좌표 정의
iScreenDy = 16
iScreenDx = 32
flttop = 7
fltleft = 27

# iScreen이 될 기본 array (블록과 테두리 정의되어 있음)
# 이후 다양한 맵을 추가하려면 ArrayScreen을 여러개 만들고
# iScreen=Matrix(ArrayScreen)을 선택하는 방향
# 블록은 고정되어 있고 flight 비행체의 flttop값을 자동으로 변화 (정해진 범위 내)
# 키 입력을 통해 총 발사하고 걸리는 시간을 스코어 형식으로 표현
ArrayScreen = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],  # 0
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],  # 2
    [1, 2, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 2, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],  # 4
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 2, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],  # 6
    [1, 2, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],  # 8
    [1, 2, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 2, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],  # 10
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 2, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],  # 12
    [1, 2, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],  # 14
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
# 총(gun) 행렬 정의
gun = [[3]]
gunBlk = Matrix(gun)

# 비행체 모양 정의
flight = [[0, 1, 1], [1, 1, 0], [0, 1, 1]]
flightBlk = Matrix(flight)

# 스크린 정의;
# iScreen이 의미하는 것 = 블록 + 테두리
iScreen = Matrix(ArrayScreen)
oScreen = Matrix(iScreen)

# 비행체 oScreen에 붙여넣기
flttempBlk = iScreen.clip(flttop, fltleft, flttop + flightBlk.get_dy(), fltleft + flightBlk.get_dx())
flttempBlk = flttempBlk + flightBlk
oScreen.paste(flttempBlk, flttop, fltleft)

# 현재 화면 출력
draw_matrix(oScreen);
print()

# 게임 main 진행부;
while True:  # 무한루프 진행

    # 스크린 초기화; flight객체를 삭제하고 이후 다시 다른 위치에 paste
    # iScreen이 의미하는 것 = 블록 + 테두리
    iScreen = Matrix(ArrayScreen)
    oScreen = Matrix(iScreen)

    # shoot 변수 정의, finish 변수 정의
    shoot = False
    finish =False

    # key 입력을 pygame 통해서 받음
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            pg.quit()
            sys.exit()
        if event.type == pg.KEYDOWN:  # space bar을 누르면 shoot True로
            if event.key == pg.K_SPACE:
                shoot = True
            if event.key == pg.K_BACKSPACE:
                finish = True

    #finish == true 일 때 무한 루프 종료
    if finish == True:
        break

    # shoot 진행
    if shoot == True:
        continue

    # flttop값을 임의로 변경하는 코드 (time.sleep 통해서 구현해야함)
    if flttop == 1:  # 정해진 범위 안에서 flight 객체 이동하기 위한 코드
        flttop += 1
    elif flttop == 12:
        flttop -= 1
    else:
        rand = random.randint(0, 1)  # flight 객체를 random하게 움직이게 하는 코드
        if rand == 0:
            flttop += 1
        else:
            flttop -= 1
    # 변화된 flttop값을 바탕으로 oScreen에 flight객체를 paste하는 코드
    flttempBlk = iScreen.clip(flttop, fltleft, flttop + flightBlk.get_dy(), fltleft + flightBlk.get_dx())
    flttempBlk = flttempBlk + flightBlk
    oScreen.paste(flttempBlk, flttop, fltleft)

    # time.sleep을 통해서 시간 간격 추가, drawmatrix로 출력
    t = 0.5
    time.sleep(t)
    draw_matrix(oScreen);print()







