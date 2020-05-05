#!/usr/bin/python3

import sys
import fileinput

lines = [line.strip(' \n') for line in fileinput.input()]



goal = int(lines[0])

a=[]
for i in range(len(lines)-2):
    a.append(int(lines[i+2]))


cur_player = 0


def find_pl(cur):
    Range = a[cur];
    avl = []
    end_point = []
    for i in range(Range):#get all the players in range
        avl.append(cur+1+i)

##    print("range ", Range)
    for i in range(Range):
        if avl[i] >= goal:
##            print("reach goal")
            return goal;
        end_point.append(avl[i] + a[avl[i]])
##    print(end_point)
    if len(end_point) == 0:
        return 0;
    return end_point.index(max(end_point))+1;



times = 0
Zero = 0
cant_reach = 0
##print(find_pl(3))
while True:
    times += 1
    if find_pl(cur_player) == 0: #player can't kick the ball
        Zero+=1;
        if Zero >1:
            print("Impossible")
            cant_reach = 1
            break;
    elif find_pl(cur_player) == goal:
        break;
    cur_player = find_pl(cur_player) + cur_player
##    print(cur_player)

if cant_reach !=1:
    print(times) 


    
