#Create a program that will print your nickname using only asterisk character (*)
from colorama import Fore


nickname ="SUN"
s = [[" " for i in range(6)] for j in range(7)]
u = [[" " for i in range(6)] for j in range(7)]
n = [[" " for i in range(6)] for j in range(7)]

#S
for row in range (7):
    for col in range (6):
        if ((row==0 or row==3 or row==6) and (col>0 and col<5)) or (col==0 and (row>0 and row<3)) or (col==5 and (row>3 and row<6)):
            s [row][col]= "*"

#U
for row in range (7):
    for col in range (6):
        if ((col==0 or col==5 ) and row!=6) or (row==6 and (col>0 and col<5)):
            u [row] [col]= "*"

#N
#code for N
for row in range(7):
    for col in range (6):
        if col==0 or col==5 or (row==col and (col>0 and col<5)):
            n [row][col]= "*"

for i in range (7):
    for j in range (6):
        print(s[i][j], end="")
    print(end="  ")
    for j in range (6):
        print(u[i][j], end="")
    print(end="  ")
    for j in range (6):
            print(n[i][j], end="")
    print(Fore.LIGHTYELLOW_EX)