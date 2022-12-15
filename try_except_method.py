#importing essential modules
from math import sqrt
import cmath


#set of checks to validate the user input
check_input = True

while check_input:
    a= float(input('Value of ''a'' coefficient: '))
    b= float(input('Value of ''b'' coefficient: '))
    c= float(input('Value of ''c'' coefficient: '))

    try:
      
        float(a), float(b), float(c)
        check_input = False

    #if string or boolean characters are inputed
    except ValueError:
      
        print('Please make sure the coefficients are real numbers and try again..')
        check_input = True

print(f'a= {a}, b= {b}, c= {c}')

# calculating discriminant using formula
d= (b**2) - (4*a*c)

# checking condition for discriminant
if d >= 0 :
    root1 = (-b + sqrt(d)) / (2*a)
    root2 = (-b - sqrt(d)) / (2*a)
    
    print(f'The roots of the equation are: {root1} and {root2}')

# when discriminant is less than 0
else:
    print(f'The equation has no solutions')
