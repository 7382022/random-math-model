import math #importing mathe module
#using ceil and floor function of math module
print('The floor and ceiling value of 23.56 are: ' + str(math.ceil(23.56)) + ', ' + str(math.floor(23.56)))

x=10
y=-15
#using copysign function
print('The value of x after copying the sign from y is: ' + str(math.copysign(x,y)))


#using fabs and gcd function
print('Absolute value of -96 and 56 are: ' + str(math.fabs(-96)) + ',' + str(math.fabs(56)))

print('The GCD of 24 and 56 : ' + str(math.gcd(24, 56)))