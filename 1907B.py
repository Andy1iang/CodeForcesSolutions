#https://codeforces.com/contest/1907/problem/B

for i in range(int(input())):
  typed = input()
  final = []
  lowerIdx = []
  upperIdx = []
  
  for idx,letter in enumerate(typed):
      
      if letter == 'b':
          final.append('')
          if len(lowerIdx) > 0 and len(final)>0:
              final[lowerIdx.pop()] = ''
        
      elif letter == 'B':
          final.append('')
          if len(upperIdx) > 0 and len(final)>0:
              final[upperIdx.pop()] = ''
        
      else:
          final.append(letter)
    
          if letter.islower():
              lowerIdx.append(idx)
        
          if letter.isupper():
              upperIdx.append(idx)
          
  print(''.join(final))