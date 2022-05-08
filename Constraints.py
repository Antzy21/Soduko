def cellCanContain(n, S, x, y):
    if not rowCanContain(n, S, x):
        return False
    if not colCanContain(n, S, y):
        return False
    if not boxCanContain(n, S, x, y):
        return False
    return True

def cellCanContainPlus(n, S, x, y):
    if not cellCanContain(n, S, x, y):
        return False
    if not knightsMove(n, S, x, y):
        return False
    if not kingsMove(n, S, x, y):
        return False
    if not orthogonalyAdjacent(n, S, x, y):
        return False
    return True

def rowCanContain(n, S, x):
    if n in S[x]:
        return False
    return True

def colCanContain(n, S, y):
    for row in S:
        if row[y] == n:
            return False
    return True

def knightsMove(n, S, x, y):
    d = [-2, -1, 1, 2]
    for i in d:
        for j in d:
            if abs(i) != abs(j):
                try:
                    if S[x+i][y+j] == n:
                        return False
                except:
                    pass
    return True

def kingsMove(n, S, x, y):
    d = [-1, 0, 1]
    for i in d:
        for j in d:
            try:
                if S[x+i][y+j] == n:
                    return False
            except:
                pass
    return True

def orthogonalyAdjacent(n, S, x, y):
    cons = [n+1]
    if n != 1:
        cons.append(n-1)
    d = [-1, 1]
    for m in cons:
        for i in d:
            try:
                if S[x+i][y] == m or S[x][y+i] == m:
                    return False
            except:
                pass
    return True

def boxCanContain(n, S, x, y):
    X = x//3*3
    Y = y//3*3
    for i in range(3):
        for j in range(3):
            if S[X+i][Y+j] == n:
                return False
    return True