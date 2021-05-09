num = 0
global steps
steps = 0


def per(n, steps = 0):
  if len(str(n)) == 1:
    print(n)
    print('Total steps: ' + str(steps))
    print('--------------------------')
    return('Done')
    
  
  steps += 1
  digits = [int(i) for i in str(n)]

  result = 1
  for j in digits:
    result *= j
  print(result)
  per(result, steps)
  if steps > 9:
    quit(0)
    
a = int(input('Starting number: '))
stop = True
while stop == True:
    print(a)
    per(a)
    a +=1
       

