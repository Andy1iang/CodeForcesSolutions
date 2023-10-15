#https://codeforces.com/contest/1722/problem/D

'''
Learned:
If a value is updated based on the previous value and does not need to be accessed later, 
sum method nor prefix sum need to be used, simply iterate through a range and update the previous value every iteration
'''

testCases = int(input())
for i in range(testCases):
    lineLength = int(input())
    line = input()
    lineValues = []
    totalValue = 0
    for i in range(0,lineLength):
        
        if line[i] == 'L':
            lineValues.append( (lineLength - 1 - i)-(i) ) #adding value to the difference to total value it could make by turning around
            totalValue += i #adding it's value to total values
            
        elif line[i] == 'R':
            lineValues.append(( (i)-(lineLength - 1 - i) ))
            totalValue += (lineLength - 1 - i) 
            
    lineValues.sort(reverse=True) #sorting the list of possible differences in descending order
    
    for i in range(lineLength):
        if lineValues[i] > 0: #only adds next possible value if it's over 0
            totalValue += lineValues[i]
        print(totalValue,end=' ')
        
    print('')