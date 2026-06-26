# Question no 1

item = input("Enter item name : ")
price= float(input("Enter price : "))
quantity= int(input("Enter quantity : "))

print ("_______________________")

print ("Item :", item)
subtotal = price*quantity
print ("Subtotal : $",subtotal)
tax = subtotal * 0.05
print ("Tax (5%) : $",tax)

print ("_______________________")

total = subtotal + tax 
print ("Total : $",total)

#Question no 2

birth_year = int(input("Enter your birth year : "))

print ("_______________________")

current_year = 2025
print ("Current Year : ", current_year)

age = current_year - birth_year
print ("You are approximately", age , "years old.")

#Question no 3

exchange_rate = 84.50
USD = float(input("Enter amount in USD : "))

print ("_______________________")
print ("Exchange Rate :", exchange_rate)

converted_amount= USD * exchange_rate
print (USD, "USD is equal to", converted_amount, "in Local Currency")

#Question no 4

number = int(input("Enter a number : "))

print ("_______________________")
if number %2 == 0:
    print (number, "is an Even number.")
if number %2 != 0:
    print (number, "is Odd number.")

# Question no 5

score = int(input("Enter score : "))

print ("_______________________")

if score <= 0 or score  >= 100:
    print ("Invalid score. Please enter 0-100.")
elif score >= 90:
        print ("Grade : A")
elif score >=80 or score <=89:
        print ("Grade : B")
elif score >=70 or score <=79:
        print ("Grade : C")
elif score >=60 or score <=69:
        print ("Grade : D")
else:
        print ("Grade : F")

