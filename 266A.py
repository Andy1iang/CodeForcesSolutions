#https://codeforces.com/contest/266/problem/A

i = 0
stoneLen = int(input())
stones = [*input()] #unpacking the input

count = 0
while i+1<stoneLen:
    if stoneLen == i-1: #at the last stone
        print(count)
        exit()
    elif stones[i] != stones[i+1]: #if stones to the right of stone is different
        i+=1
    else:
        stones.pop(i+1) #gets rid of the next same color stone
        count+=1
        
print(count)