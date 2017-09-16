print 'hi'
classmates = ['yang','ding','mu','wa']
classmates.append('admin')
classmates.insert(1,'admin2')
classmates.pop(2)
classmates[1] = 'sl'

print classmates
print len(classmates)
L = ('apple',123,True,classmates)
print L
print len(L)
print L[-1][2] 

age =2
if age >= 18:
   print age,'adult'
else:
      print age,'teemager'
      
for name in classmates:
      print name
sum = 0
for x in [1,2,3,4,5]:
      sum = sum + x
print sum   
   
sum = 0
for x in range(101):
      sum = sum + x
print sum      

sum = 0
n = 99
while n > 0:
    sum = sum + n
    n=n-2
print sum         

birth = 186
if birth < 2000:
    print 'hou'
    print birth
else:
    print 'qian'
    print birth
    
d = {'mich':98,'bob':80,'tra':67}
print d['mich'] 
d['ys'] = 50
print d['ys']
print d.get('ysl',-1)

s = set([1,2,3,4,4])
print s
s.remove(4)
print s

s1 = set([2,3,5])
print s1 & s

s.add(4)
print s

a = abs
print a(-1)

def my_abs(x):
    if x >=0:
       return x
    else:
       return -x
print my_abs(-5)   

if age >= 18:
      pass
def power(x,n=2):
    s = 1
    while n > 0:
      n = n - 1
      s = s * x
    return s
print power(2)
print power(2,3) 

def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum +n*n
    return sum
print calc(1,2,3)   
nums = [1,2,3,4] 
print calc(*nums)    

L = []
for x in range(1,11):
     L.append(x*x)
print L
     
L = [x*x for x in range(1,11)]
print L

L = [x*x for x in range(1,11) if x % 2 == 0]
print L

L = [m+n for m in 'ABC' for n in 'xyz']
print L

L = ['Hello','PhY','hKK']
print [s.lower() for s in L]
 
L = [x*x for x in range(1,11)]
print L
g = (x*x for x in range(1,11))
print g.next()

g = (x*x for x in range(1,11))
for n in g:
    print n
    
def f(x):
    return x*x
print map(f,[1,2,3,4,5])

print map(str,[1,2,3,4,5])
 
def is_odd(n):
    return n%2 ==1
print filter(is_odd,[1,2,3,4,5,6,7,8])    

print sorted([3,2,1,5])






