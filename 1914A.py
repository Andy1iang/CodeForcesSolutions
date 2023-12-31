#https://codeforces.com/contest/1914/problem/A

for i in range(int(input())):
    input()
    process:str = input()
    count:int = 0
    
    timeNeeded:dict[str,int] = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10,
    'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20,
    'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26
    }
    
    timeTaken:dict[str,int] = {}
    
    #checking how many minutes is spent on each problem
    for minute in process:
        try:
            timeTaken[minute] += 1
        except KeyError: #if it's the first minute solving the problem
            timeTaken[minute] = 1
    
    #checking if time taken was enough
    for problem,time in timeTaken.items():
        if timeNeeded[problem] <= time:
            count += 1
            
    print(count)
    
    