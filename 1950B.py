# https://codeforces.com/contest/1950/problem/B

for _ in range(int(input())):

    n = int(input())
    final = ""

    # nested loops to print checkerboard patter
    for i in range(n):
        temp = ""

        for j in range(n):
            if (i+j) % 2 == 0:
                temp += "##"
            else:
                temp += ".."

        print(temp+"\n"+temp)
