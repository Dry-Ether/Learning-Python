print(5+2) 
print(2-5) 
print(2*2)
print(5%2)
print(5//2)
print(2**3) 
print(5/2)  # Division always returns a float in Python 3
print(5+2*3)  # Operator precedence: multiplication before addition
print((5+2)*3)  # Parentheses change the order of operations
print(5+2*3-4/2)  # Combined operations with different preced
print(5+2*3-4/2**2)  # Exponentiation has the highest precedence
print(5+2*3-4/2**2%3)  # Modulus has lower precedence than exponentiation but higher than addition and subtraction
print(5+2*3-4/2**2%3//1)  # Floor division has lower precedence than modulus but higher than addition and subtraction
print(5+2*3-4/2**2%3//1*2   )  # Multiplication has the same precedence as addition and subtraction, evaluated left to right
print(5+2*3-4/2**2%3//1*2+1)  # Addition has the same precedence as multiplication, evaluated left to right
print(5+2*3-4/2**2%3//1*2+1-3)  # Subtraction has the same precedence as addition, evaluated left to right
print(5+2*3-4/2**2%3//1*2+1-3*2)  # Multiplication has the same precedence as addition and subtraction, evaluated left to right
print(5+2*3-4/2**2%3//1*2+1-3*2/2)  # Division has the same precedence as multiplication, evaluated left to right
print(5+2*3-4/2**2%3//1*2+1-3*2/2+1)  # Addition has the same precedence as multiplication and division, evaluated left to right
print(5+2*3-4/2**2%3//1*2+1-3*2/2+1-2)  # Subtraction has the same precedence as addition, evaluated left to right
print(5+2*3-4/2**2%3//1*2+1-3*2/2+1-2*3)  # Multiplication has the same precedence as addition and subtraction, evaluated left to right
print(5+2*3-4/2**2%3//1*2+1-3*2/2+1-2*3+4)  # Addition has the same precedence as multiplication and subtraction, evaluated left to right
print(5+2*3-4/2**2%3//1*2+1-3*2/2+1-2*3+4-5)  # Subtraction has the same precedence as addition, evaluated left to right
print(5+2*3-4/2**2%3//1*2+1-3*2/2+1-2*3+4-5*2)  # Multiplication has the same precedence as addition and subtraction, evaluated left to right
