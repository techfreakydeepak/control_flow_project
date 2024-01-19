#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Basic if else statement
"Question:-1"
my_input = float(input("Enter a number "))
# Check if the number is positive, negative, or zero
if my_input > 0:
    print("The given number is Positive.")
elif my_input < 0:
    print("The given number is Negative.")
else:
    print("The given number is Zero.")


# In[2]:


"Question:-2"
my_input=float(input("enter the number"))
if my_input>=18:
    print("You are eligible for the voting")
else:
    print("You are not eligible for the voting")


# In[5]:


"Question:-3"
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
#  here we Compare the numbers to find the maximum
if num1 > num2:
    max_num = num1
else:
    max_num = num2
# Display the result
print(f"The maximum of {num1} and {num2} is: {max_num}")


# In[7]:


"Question:-4"
year = int(input("Enter a year: "))
# Check if the year is a leap year
if (year % 4 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")


# In[1]:


"Question:-5"
def check_vowel_consonant(char):
    char = char.lower()
    if char == 'a':
        print(f'The character "{char}" is a vowel.')
    elif char == 'e':
        print(f'The character "{char}" is a vowel.')
    elif char == 'i':
        print(f'The character "{char}" is a vowel.')
    elif char == 'o':
        print(f'The character "{char}" is a vowel.')
    elif char == 'u':
        print(f'The character "{char}" is a vowel.')
    else:
        print(f'The character "{char}" is a consonant.')
# Get user input for a characte
user_input = input('Enter a character: ')
# Check and display the result
check_vowel_consonant(user_input)



# In[6]:


"Queston:-6"
def check_number_odd_even(number):
    # Convert the input to an integer
    number = int(number)

    if number % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")
# Get user input for a number
user_input = input("Enter a number: ")
# Check and display the result
check_number_odd_even(user_input)


# In[7]:


"Question:-7"
def absolute_value(number):
    if number < 0:
        return -number
    else:
        return number
# Test the function
num = float(input("Enter a number: "))
result = absolute_value(num)
print(f"The absolute value of {num} is {result}.")


# In[11]:


"Question:-8"
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Determine the largest number using if-else statements
if num1 >= num2 and num1 >= num3:
    largest_number = num1
elif num2 >= num1 and num2 >= num3:
    largest_number = num2
else:
    largest_number = num3
# Display the result
print(f"The largest number among {num1}, {num2}, and {num3} is: {largest_number}")


# In[ ]:


"Question:-9"
my_input = input("Enter the string: ")
if is_palindrome(my_input):
    print(f'The string "{my_input}" is a palindrome.')
else:
    print(f'The string "{my_input}" is not a palindrome.')


# In[ ]:


"Question:-10"
def calculate_grade(score):
    if 90 <= score <= 100:
        return 'A'
    elif 80 <= score < 90:
        return 'B'
    elif 70 <= score < 80:
        return 'C'
    elif 60 <= score < 70:
        return 'D'
    elif 0 <= score < 60:
        return 'F'
    else:
        return 'Invalid score. Please enter a score between 0 and 100.'
# Get user input for the student's score
try:
    score = float(input('Enter the student\'s score: '))
    # Check and display the result
    grade = calculate_grade(score)
    print(f'The student\'s grade is: {grade}')
except ValueError:
    print('Invalid input. Please enter a numeric score.')


# In[ ]:


"Question:-11"
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
if num1 >= num2 and num1 >= num3:
    largest_number = num1
elif num2 >= num1 and num2 >= num3:
    largest_number = num2
else:
    largest_number = num3
    
print(f"The largest number among {num1}, {num2}, and {num3} is: {largest_number}")



# In[ ]:


"Question:-12"
# Get user input for the lengths of three sides of the triangle
try:
    side1 = float(input("Enter the length of the first side: "))
    side2 = float(input("Enter the length of the second side: "))
    side3 = float(input("Enter the length of the third side: "))

    # Check and display the result using nested if-else statements
    if side1 == side2 == side3:
        triangle_type = "Equilateral Triangle"
    else:
        if side1 == side2 or side1 == side3 or side2 == side3:
            triangle_type = "Isosceles Triangle"
        else:
            triangle_type = "Scalene Triangle"

    print(f"The triangle is a {triangle_type}.")
except ValueError:
    print("Invalid input. Please enter numeric values for the side lengths.")


# In[4]:


"Question:-13"
my_input=float(input("enter the year"))
if my_input%4==0:
    print("Print this is a leap year")
else:
    print("Print this not a leap year")


# In[6]:


"Question:-14"
my_input =float(input("Enter the number: "))
if my_input > 0:
    print("The number is positive.")
elif my_input < 0:
    print("The number is negative.")
else:
    print("The number is zero.")


# In[8]:


"Question:-15"
my_input=float(input("enter the number:"))
if 13 <= my_input <= 19:
    print("person is teenager")
else:
    print("person is not teenager")


# In[12]:


"Question:-16"
my_input=float(input("Enter the number:"))
if my_input<0:
    print("the angle is acute")
elif my_input>0:
    print("The angle is obtuse angle")
else:
    print("The angle is right angle")


# In[13]:


"Question:-17"
# Get coefficients from the user
a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient c: "))

# Calculate the discriminant
discriminant = b**2 - 4*a*c

# Check if the discriminant is non-negative
if discriminant >= 0:
    # Calculate the two roots
    root1 = (-b + (discriminant ** 0.5)) / (2*a)
    root2 = (-b - (discriminant ** 0.5)) / (2*a)
    print("Root 1:", root1)
    print("Root 2:", root2)
else:
    # If discriminant is negative, roots are complex numbers
    real_part = -b / (2*a)
    imaginary_part = (abs(discriminant) ** 0.5) / (2*a)
    root1 = complex(real_part, imaginary_part)
    root2 = complex(real_part, -imaginary_part)
    print("Root 1:", root1)
    print("Root 2:", root2)


# In[14]:


"question:-18"
# Get user input for the day number
day_number = int(input("Enter a number (1-7) to represent the day of the week: "))
if 1 <= day_number <= 7:
    # Determine the day of the week based on the input
    if day_number == 1:
        day_of_week = "Monday"
    elif day_number == 2:
        day_of_week = "Tuesday"
    elif day_number == 3:
        day_of_week = "Wednesday"
    elif day_number == 4:
        day_of_week = "Thursday"
    elif day_number == 5:
        day_of_week = "Friday"
    elif day_number == 6:
        day_of_week = "Saturday"
    else:
        day_of_week = "Sunday"

    print(f"The day corresponding to {day_number} is {day_of_week}.")
else:
    print("Invalid input. Please enter a number between 1 and 7.")


# In[15]:


"Question:-19"
year = int(input("Enter a year: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year and divisible by 400.")
        else:
            print(f"{year} is not a leap year.")
    else:
        print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")


# In[17]:


"Question:-20"
num = int(input("Enter a number: "))
if num > 1:
    # Check for factors
    for i in range(2, int(num**0.5) + 1):
        if (num % i) == 0:
            print(f"{num} is not a prime number.")
            break
    else:
        print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")


# In[ ]:


#### elif


# In[18]:


"Question:-21"
num=int(input("enter the the number"))
if num>70:
    print("The marks in grade B")
elif num>80:
    print("the marks in the grade A2")
elif num>90:
    print("The marks in the grade A1")
else:
    print("The marks in the Grade o")


# In[19]:


"Question:-22"
angle1 = float(input("Enter the first angle of the triangle: "))
angle2 = float(input("Enter the second angle of the triangle: "))
angle3 = float(input("Enter the third angle of the triangle: "))
if angle1 + angle2 + angle3 == 180:
    # Check the types of triangles based on angles
    if angle1 == angle2 == angle3:
        print("It's an equilateral triangle.")
    elif angle1 == angle2 or angle2 == angle3 or angle1 == angle3:
        print("It's an isosceles triangle.")
    else:
        print("It's a scalene triangle.")
else:
    print("Invalid triangle. The sum of angles should be 180 degrees.")


# In[20]:


"Question:-23"
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: ")) 
bmi = weight / (height ** 2)
# Categorize BMI
if bmi < 18.5:
    category = "Underweight"
elif 18.5 <= bmi < 25:
    category = "Normal"
elif 25 <= bmi < 30:
    category = "Overweight"
else:
    category = "Obese"

# Print the result
print(f"Your BMI is {bmi:.2f}, and you are categorized as {category}.")

    


# In[21]:


"Question:-24"
number = float(input("Enter a number: "))
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")


# In[22]:


"Question:-25"
character = input("Enter a character: ")
if character.isalpha():
    if character.isupper():
        print("The character is uppercase.")
    elif character.islower():
        print("The character is lowercase.")
else:
    print("The character is special.")


# In[23]:


"Question:-26"
purchase_amount = float(input("Enter the purchase amount: "))
discount_rate_1 = 0.05  # 5% discount for purchases between $100 and $199.99
discount_rate_2 = 0.1   # 10% discount for purchases between $200 and $499.99
discount_rate_3 = 0.15  # 15% discount for purchases of $500 or more
if 100 <= purchase_amount < 200:
    discounted_price = purchase_amount * (1 - discount_rate_1)
    discount_percent = discount_rate_1 * 100
    discount_category = "5%"
elif 200 <= purchase_amount < 500:
    discounted_price = purchase_amount * (1 - discount_rate_2)
    discount_percent = discount_rate_2 * 100
    discount_category = "10%"
elif purchase_amount >= 500:
    discounted_price = purchase_amount * (1 - discount_rate_3)
    discount_percent = discount_rate_3 * 100
    discount_category = "15%"
else:
    discounted_price = purchase_amount
    discount_percent = 0
    discount_category = "0%"
# Print the result
print(f"Original Price: ${purchase_amount:.2f}")
print(f"Discount Category: {discount_category}")
print(f"Discounted Price: ${discounted_price:.2f} (-{discount_percent:.2f}%)")


# In[24]:


"Question:-27"
consumption = float(input("Enter the electricity consumption in kilowatt-hours: "))

# Define electricity rate slabs and corresponding rates
rate_slab_1 = 1.50  # $1.50 per kWh for the first 100 kWh
rate_slab_2 = 2.00  # $2.00 per kWh for the next 200 kWh
rate_slab_3 = 2.50  # $2.50 per kWh for consumption exceeding 300 kWh

# Calculate the electricity bill based on consumption slabs
if consumption <= 100:
    total_bill = consumption * rate_slab_1
elif consumption <= 300:
    total_bill = 100 * rate_slab_1 + (consumption - 100) * rate_slab_2
else:
    total_bill = 100 * rate_slab_1 + 200 * rate_slab_2 + (consumption - 300) * rate_slab_3

# Print the result
print(f"Electricity Consumption: {consumption} kWh")
print(f"Total Bill: ${total_bill:.2f}")


# In[25]:


"Question:-28"
# Get user input for angles and sides of the quadrilateral
angle1 = float(input("Enter the first angle of the quadrilateral: "))
angle2 = float(input("Enter the second angle of the quadrilateral: "))
angle3 = float(input("Enter the third angle of the quadrilateral: "))
angle4 = float(input("Enter the fourth angle of the quadrilateral: "))

side1 = float(input("Enter the length of the first side of the quadrilateral: "))
side2 = float(input("Enter the length of the second side of the quadrilateral: "))
side3 = float(input("Enter the length of the third side of the quadrilateral: "))
side4 = float(input("Enter the length of the fourth side of the quadrilateral: "))

# Check the type of quadrilateral based on angles and sides
if angle1 == angle2 == angle3 == angle4 == 90:
    print("It's a rectangle.")
elif angle1 == angle2 == angle3 == angle4 == 360:
    print("It's a square.")
elif side1 == side2 == side3 == side4:
    print("It's a rhombus.")
elif side1 == side2 and side3 == side4:
    print("It's a parallelogram.")
else:
    print("It's a general quadrilateral.")


# In[ ]:


"Question:-29"
# Get user input for the month
month = input("Enter the month (e.g., January, February, etc.): ").lower()

# Check the season based on the month
if month in ['december', 'january', 'february']:
    season = 'Winter'
elif month in ['march', 'april', 'may']:
    season = 'Spring'
elif month in ['june', 'july', 'august']:
    season = 'Summer'
elif month in ['september', 'october', 'november']:
    season = 'Fall'
else:
    season = 'Invalid month'

# Print the result
if season != 'Invalid month':
    print(f"The season for {month.capitalize()} is {season}.")
else:
    print("Invalid month. Please enter a valid month.")


# In[26]:


"Question:-30"
year = int(input("Enter the year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    year_type = 'Leap Year'
else:
    year_type = 'Common Year'
month = int(input("Enter the month (1-12): "))
if month in [1, 3, 5, 7, 8, 10, 12]:
    days_in_month = 31
elif month in [4, 6, 9, 11]:
    days_in_month = 30
elif month == 2:
    days_in_month = 29 if year_type == 'Leap Year' else 28
else:
    print("Invalid month. Please enter a number between 1 and 12.")
    exit()
# Print the result
print(f"{year} is a {year_type}.")
print(f"The month has {days_in_month} days.")


# In[27]:


## basic level
"Question:-1"
number = float(input("Enter a number: "))
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")


# In[28]:


"Question:-2"
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote yet.")


# In[29]:


"Question:-3"
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
if number1 > number2:
    max_number = number1
else:
    max_number = number2
print(f"The maximum of {number1} and {number2} is: {max_number}")


# In[31]:


"Question:-4"
num=int(input("enter the the number"))
if num<70:
    print("The marks in grade B")
elif num<80:
    print("the marks in the grade A2")
elif num<90:
    print("The marks in the grade A1")
else:
    print("The marks in the Grade o")


# In[32]:


"Question:-5"
my_input=float(input("enter the year"))
if my_input%4==0:
    print("Print this is a leap year")
else:
    print("Print this not a leap year")


# In[33]:


"Question:-6"
angle1 = float(input("Enter the first angle of the triangle: "))
angle2 = float(input("Enter the second angle of the triangle: "))
angle3 = float(input("Enter the third angle of the triangle: "))
if angle1 + angle2 + angle3 == 180:
    # Check the types of triangles based on angles
    if angle1 == angle2 == angle3:
        print("It's an equilateral triangle.")
    elif angle1 == angle2 or angle2 == angle3 or angle1 == angle3:
        print("It's an isosceles triangle.")
    else:
        print("It's a scalene triangle.")
else:
    print("Invalid triangle. The sum of angles should be 180 degrees.")


# In[35]:


"Question:-7"
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
number3 = float(input("Enter the third number: "))
if number1 >= number2 and number1 >= number3:
    largest_number = number1
elif number2 >= number1 and number2 >= number3:
    largest_number = number2
else:
    largest_number = number3
print(f"The largest of {number1}, {number2}, and {number3} is: {largest_number}")


# In[36]:


"Question:-8"
char = input("Enter a character: ")
char_lower = char.lower()
if char_lower in ['a', 'e', 'i', 'o', 'u']:
    print(f"{char} is a vowel.")
elif 'a' <= char_lower <= 'z':
    print(f"{char} is a consonant.")
else:
    print(f"{char} is not a valid alphabet character.")


# In[37]:


"Question:-9"
purchase_amount = float(input("Enter the purchase amount: "))
discount_rate_1 = 0.05  # 5% discount for purchases between $100 and $199.99
discount_rate_2 = 0.1   # 10% discount for purchases between $200 and $499.99
discount_rate_3 = 0.15  # 15% discount for purchases of $500 or more
if 100 <= purchase_amount < 200:
    discounted_price = purchase_amount * (1 - discount_rate_1)
    discount_percent = discount_rate_1 * 100
    discount_category = "5%"
elif 200 <= purchase_amount < 500:
    discounted_price = purchase_amount * (1 - discount_rate_2)
    discount_percent = discount_rate_2 * 100
    discount_category = "10%"
elif purchase_amount >= 500:
    discounted_price = purchase_amount * (1 - discount_rate_3)
    discount_percent = discount_rate_3 * 100
    discount_category = "15%"
else:
    discounted_price = purchase_amount
    discount_percent = 0
    discount_category = "0%"
# Print the result
print(f"Original Price: ${purchase_amount:.2f}")
print(f"Discount Category: {discount_category}")
print(f"Discounted Price: ${discounted_price:.2f} (-{discount_percent:.2f}%)")


# In[38]:


"Question:-10"
def check_number_odd_even(number):
    # Convert the input to an integer
    number = int(number)

    if number % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")
# Get user input for a number
user_input = input("Enter a number: ")
# Check and display the result


# In[39]:


## Intermediate Level:
"Question;-1"
a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient c: "))

# Calculate the discriminant
discriminant = b**2 - 4*a*c

# Check if the discriminant is non-negative
if discriminant >= 0:
    # Calculate the two roots
    root1 = (-b + (discriminant ** 0.5)) / (2*a)
    root2 = (-b - (discriminant ** 0.5)) / (2*a)
    print("Root 1:", root1)
    print("Root 2:", root2)
else:
    # If discriminant is negative, roots are complex numbers
    real_part = -b / (2*a)
    imaginary_part = (abs(discriminant) ** 0.5) / (2*a)
    root1 = complex(real_part, imaginary_part)
    root2 = complex(real_part, -imaginary_part)
    print("Root 1:", root1)
    print("Root 2:", root2)


# In[ ]:


"Question:-2"

