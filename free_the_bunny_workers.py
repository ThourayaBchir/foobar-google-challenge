
"""
About Polya's enumeration theorem.

Free the Bunny Workers
======================
You need to free the bunny workers before Commander Lambda's space station explodes! Unfortunately, the Commander was very careful with the highest-value workers -- they all work in separate, maximum-security work rooms. The rooms are opened by putting keys into each console, then pressing the open button on each console simultaneously. When the open button is pressed, each key opens its corresponding lock on the work room. So, the union of the keys in all of the consoles must be all of the keys. The scheme may require multiple copies of one key given to different minions.
The consoles are far enough apart that a separate minion is needed for each one. Fortunately, you have already relieved some bunnies to aid you - and even better, you were able to steal the keys while you were working as Commander Lambda's assistant. The problem is, you don't know which keys to use at which consoles. The consoles are programmed to know which keys each minion had, to prevent someone from just stealing all of the keys and using them blindly. There are signs by the consoles saying how many minions had some keys for the set of consoles. You suspect that Commander Lambda has a systematic way to decide which keys to give to each minion such that they could use the consoles.
You need to figure out the scheme that Commander Lambda used to distribute the keys. You know how many minions had keys, and how many consoles are by each work room.  You know that Command Lambda wouldn't issue more keys than necessary (beyond what the key distribution scheme requires), and that you need as many bunnies with keys as there are consoles to open the work room.
Given the number of bunnies available and the number of locks required to open a work room, write a function solution(num_buns, num_required) which returns a specification of how to distribute the keys such that any num_required bunnies can open the locks, but no group of (num_required - 1) bunnies can.
Each lock is numbered starting from 0. The keys are numbered the same as the lock they open (so for a duplicate key, the number will repeat, since it opens the same lock). For a given bunny, the keys they get is represented as a sorted list of the numbers for the keys. To cover all of the bunnies, the final solution is represented by a sorted list of each individual bunny's list of keys.  Find the lexicographically least such key distribution - that is, the first bunny should have keys sequentially starting from 0.
num_buns will always be between 1 and 9, and num_required will always be between 0 and 9 (both inclusive).  For example, if you had 3 bunnies and required only 1 of them to open the cell, you would give each bunny the same key such that any of the 3 of them would be able to open it, like so:
[
  [0],
  [0],
  [0],
]
If you had 2 bunnies and required both of them to open the cell, they would receive different keys (otherwise they wouldn't both actually be required), and your solution would be as follows:
[
  [0],
  [1],
]
Finally, if you had 3 bunnies and required 2 of them to open the cell, then any 2 of the 3 bunnies should have all of the keys necessary to open the cell, but no single bunny would be able to do it.  Thus, the solution would be:
[
  [0, 1],
  [0, 2],
  [1, 2],
]
Languages
=========
To provide a Python solution, edit solution.py
To provide a Java solution, edit Solution.java
Test cases
==========
Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.
-- Python cases --
Input:
solution.solution(2, 1)
Output:
    [[0], [0]]
Input:
solution.solution(4, 4)
Output:
    [[0], [1], [2], [3]]
Input:
solution.solution(5, 3)
Output:
    [[0, 1, 2, 3, 4, 5], [0, 1, 2, 6, 7, 8], [0, 3, 4, 6, 7, 9], [1, 3, 5, 6, 8, 9], [2, 4, 5, 7, 8, 9]]
"""

from math import factorial
from collections import Counter
from fractions import gcd

def cycle_count(c, n):
    cc=factorial(n)
    for a, b in Counter(c).items():
        cc//=(a**b)*factorial(b)
    return cc        

def cycle_partitions(n, i=1):
    yield [n]
    for i in range(i, n//2+1):
        for p in cycle_partitions(n-i, i):
            yield [i]+p

def answer(w, h, s):    
    grid=0
    for cpw in cycle_partitions(w):
        for cph in cycle_partitions(h):            
            m=cycle_count(cpw, w)*cycle_count(cph, h)
            grid+=m*(s**sum([sum([gcd(i, j) for i in cpw]) for j in cph]))
              
    return grid//(factorial(w)*factorial(h))

print(answer(2, 3, 2))



from math import factorial
from collections import Counter
from fractions import gcd

def cycle_count(c, n):
    cc=factorial(n)
    for a, b in Counter(c).items():
        cc//=(a**b)*factorial(b)
    return cc        

def cycle_partitions(n, i=1):
    yield [n]
    for i in range(i, n//2+1):
        for p in cycle_partitions(n-i, i):
            yield [i]+p

def answer(w, h, s):    
    grid=0
    for cpw in cycle_partitions(w):
        for cph in cycle_partitions(h):            
            m=cycle_count(cpw, w)*cycle_count(cph, h)
            grid+=m*(s**sum([sum([gcd(i, j) for i in cpw]) for j in cph]))
             
    return grid//(factorial(w)*factorial(h))
