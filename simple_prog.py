import cmath

#assigning values to the variables
a= 1
b= 5
c= 6

#formula for discriminant
d = (b**2) - (4*a*c)

#roots of the euation
sol1= (-b + cmath.sqrt(d)) / (2*a)
sol2= (-b - cmath.sqrt(d)) / (2*a)

print('root 1 =', sol1)
print(f'root 2 = {sol2}')
