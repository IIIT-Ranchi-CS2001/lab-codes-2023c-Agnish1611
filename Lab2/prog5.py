import math as m

nums = input('enter a, b, c: ').split(' ')
[a, b, c] = [int(x) for x in nums]

d = m.sqrt(b)-(4*a*c)

if (d==0):
    r = (-b)/(2*a)
    print('One repeated root: ', r)
elif (d>0):
    r1 = ((-b)+m.sqrt(d))/(2*a)
    r2 = ((-b)-m.sqrt(d))/(2*a)
    print('Two distinct roots: ', r1, ' and ', r2)
else:
    real = (-b)/(2*a)
    img = m.sqrt((-d))/(2*a)
    print('Real part: ', real, '\nImaginary part: ', img)