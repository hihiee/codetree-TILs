'''
start: (0, 0)
총 N 번 움직임: n 
N번에 걸쳐 움직이려는 방향(direction)과 움직일 거리(distance) 가 주어졌을 때 최종 위치는?

-> 그럼 방향 * 움직이는 거리를 n 번 해야지
'''

# 출발점
x, y = 0, 0

dx = [1, -1,  0, 0]
dy = [0,  0, -1, 1]

n = int(input())

for _ in range(n):
    direction, distance = tuple(input().split())
    distance = int(distance)
    
    if direction == 'E':
        step = 0
    elif direction == 'W':
        step = 1
    elif direction == 'S':
        step = 2
    else:
        step = 3

    x = x + dx[step] * distance
    y = y + dy[step] * distance

print(x, y)


'''

dir_num = 2
x, y = 1, 5
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]

nx, ny = x + dx[dir_num], y + dy[dir_num]



x, y = 0, 0
n = int(input())

# E, W, S, N
dx, dy = [1, -1, 0, 0], [0, 0, -1, 1]

for _ in range(n):
    dir_, steps = input().split()
    steps = int(steps)

    if dir_ == 'N':
        step = 3
    elif dir_ == 'E':
        step = 0
    elif dir_ == 'S':
        step = 2
    elif dir_ == 'W':
        step = 1

    x += dx[step] * steps
    y += dy[step] * steps

print(x, y)

'''