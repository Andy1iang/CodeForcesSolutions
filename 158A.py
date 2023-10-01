#https://codeforces.com/contest/158/problem/A

stat = input().split()
scores = input().split()
place = scores[int(stat[1])-1] #getting score of at the qualifying index

count = 0
for i in scores:
    if int(i) >= int(place) and int(i) != 0:
        count +=1
        
print(count)