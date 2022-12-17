# 1, 4 => 2, 3 => 4, 1 => 3, 2...

# a < b  
# a, b => 2a, b-a =>

# k, 3k => 2k, 2k....
# k, 5k => 2k, 3k => 4k, 1k => ...
# k, 7k => 2k, 6k => 4k, 4k => ...
# k, 15k => 2k, 14k => 4k, 12k => 8k, 8k...

def answer(arr):
    def gcd(x, y):
        if x < y:
            x, y = y, x
        while (y):
            x, y = y, x % y
        return x

    def forever(x, y):
        quotient = (x+y)/gcd(x, y)
        if int(quotient) != quotient:
            return True
        quotient = int(quotient)
        return (quotient & (quotient-1)) != 0  
   
    def pair(u, match, seen):
        for v in range(l):
            if M[u][v] and seen[v] == False:
                seen[v] = True
               
                # if a has been matched to b, retrieve a from match[b]
                # check if it can be matched to another number given the
                # current seen list. If so, updated match[b] to c (current)
                if match[v] == -1 or pair(match[v], match, seen):
                    match[v] = u
                    return True
        return False
           
    # build graph
    l = len(arr)
    M = [[None] * l for _ in range(l)]
   
    for i in range(l):
        for j in range(i, l):
            M[i][j] = forever(arr[i], arr[j])
            M[j][i] = M[i][j]  
   
    match = [-1] * l
    result = 0
    for i in range(l):
        seen = [False] * l
        if pair(i, match, seen):
            result += 1
    return l - 2 * (result//2)

print(answer([1, 7, 3, 21, 13, 19]))
