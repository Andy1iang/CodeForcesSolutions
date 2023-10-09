#https://codeforces.com/problemset/problem/8/A

'''
Learned:
Reverse either the original array, or the sequences when checking backwards matching
Add 1 to the range to include the last index in the loop when subtracting sub-array length from original
'''

forward = False
backward = False

flags = input()
tempFlags = ''
firstSeq = input()
secondSeq = input()

for i in range(len(flags)-len(firstSeq)+1):
    if flags[i:i+len(firstSeq)] == firstSeq:
        tempFlags = flags[i+len(firstSeq):]
        break

if len(tempFlags) >= len(secondSeq):
    for i in range(len(tempFlags)-len(secondSeq)+1):
        if tempFlags[i:i+len(secondSeq)] == secondSeq:
            forward = True
            break
            
flags = flags[::-1]
tempFlags = ''

for i in range(len(flags)-len(firstSeq)+1):
    if flags[i:i+len(firstSeq)] == firstSeq:
        tempFlags = flags[i+len(firstSeq):]
        break

if len(tempFlags) >= len(secondSeq):
    for i in range(len(tempFlags)-len(secondSeq)+1):
        if tempFlags[i:i+len(secondSeq)] == secondSeq:
            backward = True
            break
           
if forward and backward:
    print("both")
elif forward:
    print("forward")
elif backward:
    print("backward")
else:
    print("fantasy")