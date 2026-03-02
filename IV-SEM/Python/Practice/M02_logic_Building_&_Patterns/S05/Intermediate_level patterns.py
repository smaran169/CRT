'''def diamond_pattern(n):
    # Upper half
    for i in range(n):
        print(" " * (n - i - 1) + "*" * (2 * i + 1))
    
    # Lower half
    for i in range(n - 2, -1, -1):
        print(" " * (n - i - 1) + "*" * (2 * i + 1))

# Example usage
diamond_pattern(5)''' 
'''
n =  int(input())
for i in range(1, n+1):
    print(" " * (n - i) + "*" * i)
for i in range(n-1, 0, -1):
    print(" " * (n - i) + "*" * i)
    '''

 # Number Pyramid Pattern
  '''rows = 10

for i in range(1, rows + 1):
  
    print(" " * (rows - i), end="")
    
    for j in range(1, i + 1):
        print(j, end="")
    for j in range(i - 1, 0, -1):
        print(j, end="")
    print()''' '''n = int(input("Enter the number of rows: "))
for i in range(1, n + 1):
    for j in range(n-i):
        print(" ", end="")
    for k in range(1,i+1):
        print(k, end=" ")
    print()'''

