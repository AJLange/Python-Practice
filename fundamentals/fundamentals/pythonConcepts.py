num1 = 42  # variable declaration - integer
num2 = 2.3 # variable declaration - float
boolean = True # variable declaration - bool
string = 'Hello World' # variable declaration - string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #list - initialize - populate
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # initialize dictionary 
fruit = ('blueberry', 'strawberry', 'banana') #initialize tuple 

print(type(fruit)) #type check and log statement
print(pizza_toppings[1]) #log statement
pizza_toppings.append('Mushrooms') #add item to a list
print(person['name']) #log dictionary value
person['name'] = 'George' #change dictionary value
person['eye_color'] = 'blue' #add dictionary value
print(fruit[2]) #log tuple value

if num1 > 45: # if statement
    print("It's greater") #log
else:  #else 
    print("It's lower") #log


if len(string) < 5: # length check
    print("It's a short word!") #log
elif len(string) > 15: #else if
    print("It's a long word!") #log
else: #else
    print("Just right!") #log

for x in range(5): #for loop
    print(x)
for x in range(2,5):  #for loop
    print(x)
for x in range(2,10,3):  #for loop
    print(x)
x = 0
while(x < 5): #while loop
    print(x)
    x += 1 #increment

pizza_toppings.pop()  #remove item from list and return it
pizza_toppings.pop(1)

print(person) #log dictionary item
person.pop('eye_color')  #remove item from list and return it
print(person) #log the dictionary item minus the popped item

for topping in pizza_toppings: # for loop start
    if topping == 'Pepperoni': #if statement
        continue #continue
    print('After 1st if statement') 
    if topping == 'Olives': #if statement
        break #end the loop

def print_hello_ten_times():  #function definition
    for num in range(10): #for loop which counts to 10
        print('Hello')

print_hello_ten_times() # call the function

def print_hello_x_times(x): #this loop prints hello by taking in a param
    for num in range(x):
        print('Hello')

print_hello_x_times(4) #calls function with 4

def print_hello_x_or_ten_times(x = 10): #function definition
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times() #will print 10 times
print_hello_x_or_ten_times(4) #will print 4 times

# the following is a multiline comment:
"""
Bonus section
"""
# and these are single line comments
# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)