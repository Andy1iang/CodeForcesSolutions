# https://codeforces.com/problemset/problem/158/B

import math

groups = int(input())
people = input().split()
taxis = 0

taxis += people.count('4')  # putting all the groups of 4 in taxis

threes = people.count('3')
twos = people.count('2')
ones = people.count('1')

taxis += threes  # adding the groups of threes

# grouping ones with threes
if threes >= ones:
    ones = 0

elif ones > threes:
    ones = ones-threes

# grouping twos together
taxis += twos//2
twos = twos % 2

# grouping ones with 2s
if twos > 0:
    ones -= 2
    taxis += 1

# grouping ones together
if ones > 0:
    taxis += math.ceil(ones/4)

print(taxis)
