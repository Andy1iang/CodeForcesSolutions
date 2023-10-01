#https://codeforces.com/contest/791/problem/A

weight1,weight2 = input().split()
weight1 = int(weight1)
weight2 = int(weight2)

count = 0
while weight2 >= weight1:
    count +=1
    weight2 *= 2
    weight1 *= 3
    
print(count)