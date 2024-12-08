import math as m

sides = input('enter the sides of a triangle: ').split(' ')
[s1, s2, s3] = [ int(x) for x in sides ]

p = s1+s2+s3
s = p/2;
a = m.sqrt(s*(s-s1)*(s-s2)*(s-s3))

tempA = ((s2*s2)+(s3*s3)-(s1*s1))/(2*s2*s3)
A = m.degrees(m.acos(tempA))

tempB = ((s1*s1)+(s3*s3)-(s2*s2))/(2*s1*s3)
B = m.degrees(m.acos(tempB))

tempC = ((s1*s1)+(s2*s2)-(s3*s3))/(2*s1*s2)
C = m.degrees(m.acos(tempC))

print('Perimeter: ', p, '\nArea: ', a, '\nAngles: ', A, ' ', B, ' ', C)