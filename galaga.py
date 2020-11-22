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
                print("□ ", end='')
            elif array[y][x] == 1:
                print("■ ", end='')
            elif array[y][x] == 2:
                print("◆ ", end='')
            elif array[y][x] == 3:
                print("● ", end='')
            elif array[y][x] == 7:
                print("▶ ", end='')
            else:
                print("◆ ", end='')

        print()


# 충돌여부 파악하는 함수 구현
a_y = 0
a_x = 0


def crash(m):
    global a_y
    global a_x
    array = m.get_array()
    for y in range(m.get_dy()):
        for x in range(m.get_dx()):
            if array[y][x] == 4:
                array[y][x] = 1
                a_y = y
                a_x = x
                return True
            elif array[y][x] == 5:
                array[y][x] = 0
                a_y = y
                a_x = x
                return True
    return False


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

# 점수 출력을 위한 emptyScreen 정의 (빈 화면)
emptyScreen = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

# gameover표시용 matrix 정의
gameScreen = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]
overScreen = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]
# 점수표시용 숫자 정의 (0 ~ 9)
def timescore(t):
    if t == 0:
        timeBlk = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]]

    elif t == 1:
        timeBlk = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 0, 0, 0, 0],
            [0, 0, 1, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 1, 1, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]]
    elif t == 2:
        timeBlk = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 1, 1, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]]

    elif t == 3:
        timeBlk = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]]

    elif t == 4:
        timeBlk = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 1, 1, 0, 0, 0],
            [0, 0, 0, 1, 0, 1, 0, 0, 0],
            [0, 0, 1, 0, 0, 1, 0, 0, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]]

    elif t == 5:
        timeBlk = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 1, 1, 1, 1, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 1, 1, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]]

    elif t == 6:
        timeBlk = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 1, 1, 1, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]]

    elif t == 7:
        timeBlk = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 1, 0, 0],
            [0, 0, 1, 0, 0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]]

    elif t == 8:
        timeBlk = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]]

    elif t == 9:
        timeBlk = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 1, 0, 0],
            [0, 1, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 1, 1, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]]
    return timeBlk


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

# 장애물 행렬 정의
obstacle = [[7]]
obstacleBlk = Matrix(obstacle)
obstacletop = 1  # 장애물의 생성 top좌표는 랜덤으로 변함
obstacleleft = 6  # 장애물의 생성 left좌표는 항상 고정 (상수)

#randomnumber을 담는 리스트 정의 (list의 배열값이 1과 14사이일때만 장애물 생성해서 출력
lst=[]
for i in range(1000):
    lst.append(random.randint(1,14))
i=0


# 코드 실행 시간 출력용 변수 선언
start = int(time.time())

# 게임 main 진행부;
while True:  # 무한루프 진행
    # 남아 있는 벽돌이 없을 때 걸린 시간을 출력하기 위한 변수 선언
    printtimescore = False

    #장애물에 맞았을 때 gameover을 출력하기 위한 bool타입 변수
    gameover=False
    # 스크린 초기화; flight객체를 삭제하고 이후 다시 다른 위치에 paste
    # iScreen이 의미하는 것 = 블록 + 테두리
    iScreen = Matrix(ArrayScreen)
    oScreen = Matrix(iScreen)

    # shoot 변수 정의, finish 변수 정의
    shoot = False
    finish = False

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
                printtimescore = True
                finish = True
            if event.key == pg.K_LEFT:
                if flttop != 12:
                    flttop += 1
            elif event.key == pg.K_RIGHT:
                if flttop != 1:
                    flttop -= 1

    # finish == true 일 때 무한 루프 종료
    if finish == True:
        break

    # lst에 저장된 randomnumber 바탕으로 obstacle 생성하기
    if 1 <= lst[i] <= 14:
        oScreen = Matrix(iScreen)
        obstacletop = lst[i]
        obstacletempBlk = iScreen.clip(obstacletop, obstacleleft, obstacletop + 1, obstacleleft + 1)
        obstacletempBlk = obstacletempBlk + obstacleBlk
        oScreen.paste(obstacletempBlk, obstacletop, obstacleleft)

        # 예상 충돌 좌표에서의 충돌 여부 파악
    if obstacleleft == 27:
        if flttop <= obstacletop <= flttop + 2:
            gameover = True
            break

    obstacleleft += 1

    if obstacleleft == 31:
        i += 1
        obstacleleft = 6

    # shoot 진행
    if shoot == True:
        guntop = flttop + 1
        gunleft = fltleft - 1

        obstacleSpeed = 0
        while True:
            oScreen = Matrix(iScreen)
            oScreen.paste(flttempBlk, flttop, fltleft)
            oScreen.paste(obstacletempBlk, obstacletop, obstacleleft)
            time.sleep(0.05)
            guntempBlk = iScreen.clip(guntop, gunleft, guntop + gunBlk.get_dy(), gunleft + gunBlk.get_dx())
            guntempBlk = guntempBlk + gunBlk
            oScreen.paste(guntempBlk, guntop, gunleft)
            gunleft -= 1

            if obstacleleft == 27:
                if flttop <= obstacletop <= flttop + 2:
                    gameover = True
                    break

            #obstacle 블록객체가 너무 빠르게 움직이는 것을 방지
            #현재 whileloop의 timesleep값이 바깥의 값보다 4배 크기때문에 루프를 4번 돌때마다 1칸 움직이게 설정했음
            if obstacleSpeed==0:
                obstacleleft += 1
                obstacleSpeed=2
            elif obstacleSpeed==2:
                obstacleSpeed=3
            elif obstacleSpeed==3:
                obstacleSpeed=4
            elif obstacleSpeed == 4:
                obstacleSpeed=0

            if obstacleleft == 31:
                i += 1
                obstacleleft = 6

            if crash(oScreen):
                draw_matrix(oScreen)
                break
            else:
                draw_matrix(oScreen)
    if ArrayScreen[a_y][a_x] == 2:
        ArrayScreen[a_y][a_x] = 0



    # 바뀐 flttop을 바탕으로 oscreen에 붙여넣기
    flttempBlk = iScreen.clip(flttop, fltleft, flttop + flightBlk.get_dy(), fltleft + flightBlk.get_dx())
    flttempBlk = flttempBlk + flightBlk
    oScreen.paste(flttempBlk, flttop, fltleft)

    # time.sleep을 통해서 시간 간격 추가, drawmatrix로 출력
    t = 0.2
    time.sleep(t)
    draw_matrix(oScreen);
    print()

    # ArrayScreen전체에서 2가 없으면 게임 종료 ( 시간에 따른 스코어 출력)
    count = 0
    # 모든 ArrayScreen의 배열값 돌면서 블록(2)가 남아있다면 count값 증가
    for y in range(iScreenDy):
        for x in range(iScreenDx):
            if ArrayScreen[y][x] == 2:
                count += 1

    # count == 0 (배열에 남은 2 값이 없음) 일 때 종료 및 점수 출력
    if count == 0:
        printtimescore = True
        break

# 코드 실행 시간 출력용 변수 선언
end = int(time.time())

# 코드 실행 시간 변수에 저장 (무한 루프 빠져나올 때까지 걸린 시간) (자료형 : int)
timeSpent = end - start

# printtimescore이 true 일 때 걸린 시간 출력하는 코드
if printtimescore == True:

    # printtimescore == True 이면 새로운 스크린을 따와서 숫자를 붙혀 출력
    timeiScreen = Matrix(emptyScreen)
    timeoScreen = Matrix(timeiScreen)

    # timeSpent에 저장된 숫자를 10의 자릿수와 1의 자릿수로 나누는 코드
    timeoften = timeSpent // 10
    timeofone = timeSpent % 10
    timeoftenBlk = Matrix(timescore(timeoften))
    timeofoneBlk = Matrix(timescore(timeofone))

    # 숫자 출력 index 좌표값
    timeoftentop = 3
    timeofonetop = 3
    timeoftenleft = 4
    timeofoneleft = 18

    # 걸린시간이 한자리 수이면 숫자 하나를 가운데에 출력할 수 있게 index값 조정
    if timeoften == 0:
        timeofonetop = 3
        timeofoneleft = 11

    # 출력화면 깜박이게 하기 (반복문 통해서 빈화면과 출력화면 번갈아서 draw_matrix하기)
    for i in range(2):

        # 빈화면으로 초기화
        timeiScreen = Matrix(emptyScreen)
        timeoScreen = Matrix(timeiScreen)
        draw_matrix(timeoScreen);
        print()
        time.sleep(0.3)

        # timeiScreen에서 clip 따와서 붙혀넣기
        # timeoften != 0일때 실행
        if timeoften != 0:
            timeoftentempBlk = timeiScreen.clip(timeoftentop, timeoftenleft, timeoftentop + timeoftenBlk.get_dy(),

                                                timeoftenleft + timeoftenBlk.get_dx())
            timeoftentempBlk = timeoftentempBlk + timeoftenBlk
            timeoScreen.paste(timeoftentempBlk, timeoftentop, timeoftenleft)

        timeofonetempBlk = timeiScreen.clip(timeofonetop, timeofoneleft, timeofonetop + timeofoneBlk.get_dy(),
                                            timeofoneleft + timeofoneBlk.get_dx())
        timeofonetempBlk = timeofonetempBlk + timeofoneBlk
        timeoScreen.paste(timeofonetempBlk, timeofonetop, timeofoneleft)

        # timeoScreen출력부
        draw_matrix(timeoScreen);
        print()

        time.sleep(0.3)

#장애물에 맞았을 때 (gameover == True)
if gameover == True:
    gameoScreen=Matrix(gameScreen)
    draw_matrix(gameoScreen);print()
    time.sleep(1)
    overoScreen=Matrix(overScreen)
    draw_matrix(overoScreen);print()
