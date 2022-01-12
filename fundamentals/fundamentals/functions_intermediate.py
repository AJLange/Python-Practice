'''
Update values in Dictionaries and lists

'''

x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

'''
Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
Change the last_name of the first student from 'Jordan' to 'Bryant'
In the sports_directory, change 'Messi' to 'Andres'
Change the value 20 in z to 30
'''

x[1][0] = 15
students[0]["last_name"] = "Bryant"
sports_directory["soccer"][0] = "Andres"
z[0]["y"] = 30


# just testing it
print(x)
print(students)
print(sports_directory)
print(z)

'''
Iterate through a list of dictionaries

Create a function iterateDictionary(some_list) that, given a list of dictionaries, 
the function loops through each dictionary in the list and prints each key and the 
associated value. 
'''
def iterateDictionary(some_list):
    for i in range(0,len(some_list)):
        my_dict = some_list[i]
        for k, v in my_dict.items():
            print(k, " - ", v, ", ", end="", sep="")
        print("")


students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
iterateDictionary(students) 


'''
Get values from a list of dictionaries

Create a function iterateDictionary2(key_name, some_list) that, given a 
list of dictionaries and a key name, the function prints the value stored 
in that key for each dictionary. 
'''

def iterateDictionary2(key_name, some_list):
    for i in range(0,len(some_list)):
        my_dict = some_list[i]
        print(my_dict[key_name])

iterateDictionary2('first_name', students) 


'''
Iterate Through a Dictionary with List Values
Create a function printInfo(some_dict) that given a dictionary
whose values are all lists, prints the name of each key along with
the size of its list, and then prints the associated values
within each key's list. 
'''

def printInfo(some_dict):
    for k in some_dict:
        my_list = some_dict[k]
        list_len = len(my_list)
        print(list_len, k)
        for i in range(0, list_len):
            print(my_list[i])


dojo = {
'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)

