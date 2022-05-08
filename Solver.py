import Sodukos
from Constraints import *
from numpy import matrix as m

#print(m(Sodukos.s1))

def solve(S):
    for x, row in enumerate(S):
        for y, cell in enumerate(row):
            if cell == 0:
                for n in range(1,10):
                    if cellCanContain(n, S, x, y):
                        S[x][y] = n
                        solve(S)
                        S[x][y] = 0
                return
    print(m(S))

solve(Sodukos.s1)