
nums = input('Enter two numbers: ').split(' ')
[a, b] = [int(x) for x in nums]

print('Sum: ', (a+b), '\nDifference: ', (abs(a-b)), '\nProduct: ', (a*b), '\nFraction Quotient: ', (a/b), '\nInteger Quotient: ', (a//b), '\nRemainder: ', (a%b), '\nExponential: ', (a**b))