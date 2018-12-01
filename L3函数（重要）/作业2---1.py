# 第一小题

def sn(n):
     print('总和',(1+n)*n//2)

print(sn(100))



def fac(n):
     if n ==1:
          return 1
     return n + fac(n-1)
print(fac(100))

# fn(n) = fn(n-1) + n