""" Take user input
number = 2  

# Condition of the while loop
while number < 5 :  
    print("Thank you")
    # Increment the value of the variable "number by 1"
    number = number+1"""

""" Take user input
number = int(input("Enter a number: "))  

# Condition of the while loop
while number <= 5:  
    # Find the mod of 2
    if number % 2 == 0:  
        print("The number", number, "is even")
    else:
        print("The number", number, "is odd")

    # Increment `number` by 1
    number += 1"""

# Fibonacci series using a while loop
"""n = int(input("Enter the number of terms: "))

a, b = 0, 1
count = 0

print("Fibonacci Series:", end=" ")

while count < n:
    print(a, end=" ")
    a, b = b, a + b
    count += 1"""

#for loop        
"""for loop
for in range (7)
print (i)"""
"""
for i in range (1,11,2):
    print(i)"""
"""
PASSWORD = "secure123"
while True:
    user_input = input("Enter password: ")
    
    if user_input == PASSWORD:
        print("Access Granted!")
        break  # Exit loop if the password is correct
    else:
        print("Incorrect password. Try again.")"""


# Constant password
PASSWORD = "secure123"

# Allow up to 3 attempts
for attempt in range(5):
    user_input = input("Enter password: ")
    
    if user_input == PASSWORD:
        print("Access Granted!")
        break  # Exit loop if the password is correct
    else:
        print("Incorrect password. Try again.")

# If the loop completes without a correct attempt
else:
    print("Too many incorrect attempts. Access Denied.")
