# Question no 1

def number(number1,number2):
    if number1*number2 <=1000:
        return number1*number2
    else:
        return number1 + number2
     
print ("The result is ", number(20,30))
print ("The result is ", number(40,30))

# Question no 2

previous_num= 0
print ("Printing current and previous number sum in a range(10)")

for i in range(10):
    print ("Current Number ", i,"Previous Number ",previous_num,"Sum : ", i + previous_num)
    previous_num = i 

#Question no 3

string = "python"

print ("Original String is ",string)
print("Printing only even index chars")

for i in range (0 , len(string),2):
    print (string[i]) 

#Question no 4

def remove_chars(char,n):
    return char[n:]
print (remove_chars("python",4))
print (remove_chars("python",2))

#Question no 5

fruits = ["apple","banana","cherry","date","elderberry"]
fruits.append("fig")
fruits.remove("banana")
print (fruits)

