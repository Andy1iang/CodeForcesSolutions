# https://codeforces.com/contest/1927/problem/A

for _ in range(int(input())):
 
    leng = int(input())
    s = input()

    if "B" not in s:
        print(0)
    else:
        # finding the two ends of 'B'
        front = s.find("B")
        s = s[::-1]
        end = leng - s.find("B")
        print(end-front)