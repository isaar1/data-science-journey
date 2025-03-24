#1️⃣ Check if a Number is Positive, Negative, or Zero

def check_number(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

#2️⃣ Check if a Number is Even or Odd

def even_or_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

#3️⃣ Print Numbers from 1 to 10 using a for loop

for i in range(1, 11):  
    print(i)

#4️⃣ Use a while loop to keep asking for input until the user enters "stop"
'''
num = int(input("enter any number or stop: "))
while num == int:
    print(num)
    num = input("stop or not")
    num +=1
'''
while True:
    num = input("enter the number")
    if num.lower() == "stop":
        break
    print(num)


#5️⃣ Write a function that calculates the square of a number

def squa(a):
    num = a**2
    print(num)

squa(3)


#6️⃣ Write a function that checks if a number is prime
'''
nums = int(input("enter the number"))
if (nums/1)== nums:
    if (nums/nums) == 1:
        print("number is a prime")
else:
    print("number is not a prime")
'''


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n // 2 + 1):  # Only check up to half of n
        if n % i == 0:
            return False
    return True


#7️⃣ Print Even Numbers from 1 to 20 using a Loop

for i in range(1,21):
    if i%2 == 0:
        print(i)

#8️⃣ Reverse a String using a Function

def reverse_str(n):
    n[::-1]

print(reverse_str("isaar"))


#9️⃣ Find the Largest Number in a List

def find_largest(lst):
    return max(lst)

numbers = [3, 7, 2, 9, 5]
print(find_largest(numbers))  # Output: 9


#🔟 Easy Code: Count Vowels in a String

def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count
print(count_vowels("Hello World"))
