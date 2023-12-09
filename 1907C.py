from collections import Counter
import math

for i in range(int(input())):
    
    
    length = int(input())
    
    word = input()
    
    maxOccur = ridOf = Counter(''.join(word)).most_common(1)[0][1]
    
    if maxOccur < math.floor(length/2):
        print(1) if length%2 != 0 else print(0)
        
    else:
        print(abs(maxOccur-(length-maxOccur)))