# https://codeforces.com/problemset/problem/479/A

num1 = int(input())
num2 = int(input())
num3 = int(input())

if num1 == 1 and num3 == 1:
    res = num1+num2+num3

elif num2 == 1:
    res = (min(num1, num3)+1)*max(num1, num3)

elif num1 == 1:
    res = (num2+1)*num3

elif num3 == 1:
    res = (num2+1)*num1

else:
    res = num1*num2*num3

print(res)
