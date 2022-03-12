import time
s=0
m=0
h=0
d=0
M=0
j=0
D=0

while True:
  print('|Decade', D, '|Year', j, '|Month', M, '|Day', d, '|Hour', h, '|Minute', m, '|Secondes', s)
  time.sleep(0.999999999999999999999)
  
  s += 1
  if s == 60:
    s=0
    m += 1
            
    if m == 60:
      m=0
      h += 1

      if h == 24:
        h=0
        d += 1

        if d == 30:
          d=0
          M += 1

          if M == 12:
            M=0
            j += 1

            if j == 10:
              j=0
              D += 1   
              break

#developed by Quaatos with <3
  
        
          

