# https://codeforces.com/contest/791/problem/A

weight1, weight2 = list(map(int,input().split()))

count = 0
while weight2 >= weight1:
    count += 1
    weight2 *= 2
    weight1 *= 3

print(count)
