''' 
1) write a python code to count the digiit of number?
2)sum of the digit of a number
3)product of the digit of a number
4)reverse of number
5)count even and odd digits
6)lagest digit of the number


''' 
''''
num = int(input("Enter a number: "))
digit_count = len(str(abs(num)))   
print("Number of digits:", digit_count)
'''
'''
def sum_of_digits(n):
    total = 0
    while n > 0:
        total += n % 10   
        n //= 10          
    return total


print(sum_of_digits(1234))  
'''''
''''
def product_of_digits(n):
    product = 1
    while n > 0:
        digit = n % 10
        product *= digit
        n //= 10
    return product

# Example
print(product_of_digits(523))  # Output: 30
'''
''''
def reverse_number(n):
    rev = 0
    while n > 0:
        digit = n % 10       # extract last digit
        rev = rev * 10 + digit
        n //= 10             # remove last digit
    return rev

# Example
print(reverse_number(12345))  # Output: 54321

''''

def count_even_odd_digits(num):
    even_count = 0
    odd_count = 0
    
    for digit in str(num):  # convert number to string to iterate
        if digit.isdigit():  # ensure it's a digit
            if int(digit) % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
    
    return even_count, odd_count






