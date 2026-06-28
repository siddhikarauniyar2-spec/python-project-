# Question no 1 

print ("Twinle, twinkle, little star,")
print ("\t How I wonder what you are!")
print ("\t\t Up above the world so high,")
print ("\t\t Like a diamond in the sky.")
print ("Twinle, twinkle, little star,")
print ("\t How I wonder what you are") 

# Question no 2

Lst = [1,2,3,4,5,5,4,4,4] 
list = Lst.count(4)
print(list) 

# Question no 3

color_list_1 ={'White', 'Black', 'Red'}
color_list_2 ={'Red', 'Green'}
print(color_list_1 - color_list_2)

# Question no 4

    #List                  #Tuple
    
  #uses []                # uses()
  #can be changed         #cannot be changed
    #(mutable)              #(immutable)
  #example: [1,2,3]       #example: (1,2,3)

# List
a = [1, 2, 3]
a[0] = 10
print(a)

# Tuple
b = (1, 2, 3)
# b[0] = 10   # Error

# Question no 5

  # " == " hecks whether values are equal.
  # " is " checks whether both variables refer to the same object in memory.

a = [1, 2]
b = [1, 2]

print(a == b)   # True
print(a is b)   # False

#Question no 6
 
  #The global keyword is used inside a function when you want to modify a variable that is declared outside the function.

x = 10

def change():
    global x
    x = 20

change()

print(x)

# Question no 7

i = 1
while i <= 10:
    print (i)
    i = i+1   
    