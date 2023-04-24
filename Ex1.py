# Gitika Chouksey (0827CI201068)
# indentation example

branch = 'CSIT'
if branch == 'CSIT':
    print('Welcome to CSIT')
else:
    print('Other branch')
print('All set !')

# Gitika Chouksey

print('This is python code')
# this is single line comment
"""
This is a multiline comment in Python that
spans several lines. This application is
a Computer Science portal for geeks. 
"""

# Gitika Chouksey
# if else example 

#if-else
num = 100;
if num==100:
    print('num is 100')
    
else:
    print('num is not 100')

#nested if-else
if num<=100:
    if num<=50:
        print("number is between 0 to 50")
    else:
        print("number is between 50 to 100")

else:
    print('number is above 100')
    
    
#if elif else

if num==100:
    print("number is 100")
    
elifnum==200:
    print('number is 200')

elifnum==300:
    print('number is 300')

else:
    print('number something else')

# Gitika Chouksey (0827CI201068)
#List Data structure

fruits = ['mango','apple',1000,'banana','orange',True,58.50]
print(fruits)    #print list
print('element at index 3 '+fruits[3])  #access element using index value
print('length of list ',len(fruits))    #print length of list
fruits.append(2020.55);                 #append to the list
fruits.insert(2,False);                 #insert at index 2
fruits.extend([8,'potato']);            #insert at end
fruits.reverse();  
fruits.remove('apple');
fruits.pop(3);                          #remove at index 3
fruits.clear();
# fruits.sort();                        #only work on same type of values in list
print(fruits);


# Gitika Chouksey (0827CI201068)

# myTuple = ('banana', 'apple', 'orange', 'pineapple');

#creating tuple using tuple constructor
myTuple = tuple(('banana', 'apple', 'orange', 'pineapple'))

 print(myTuple)
 print('length of tuple : ',len(myTuple));       #length of tuple
 print('element at 2 ',myTuple[2]);              #access element using indexing
 print(myTuple[1:3])                             #slicing from index 1 to 2
 print(myTuple.count('banana'))                  #count occurrence of banana
 print('banana' in myTuple)                      # print true if present
mylist = ['banana', 'apple', 'orange', 'pineapple'];
convertedTuple = tuple(mylist);                     #convert list into tuple


# Gitika Chouksey (0827CI201068)
#string data structure

str = 'Welcome to the CSIT Department'
print(str[0])                   #accessing using index
print(str.capitalize())         #capitalize the string
print(''.join(reversed(str)))   #reverse the string
print(str[2:8])                 #string slicing
print(list(str))                #convert string to list
del str                         #delete entire string
String1 = "{1} {0} {2}".format('Geeks', 'For', 'Life')
print(str.count('to'))            #count the word to
print(str.split('the'))           #split into list based on word 'the'
print(str.upper())                #convert into uppercase
print(str.lower())                #convert into lowercase
print(str.find('the'))            #return the starting index of 'the'
print(str.index('to'))            #return the index of 'to'

#Gitika Chouksey (0827CI201068)
#Dictionary data structure

myDict = {100:'Gitika' , 200:'Gourav',300:'Hariom',400:'Himesh',500:'Himanshu',600:'Honey'};
print(myDict)
print(myDict.get(400))          #get value using key
print(myDict.values())          #prints only values
print(myDict.keys())            #prints only keys
print(myDict.pop(400))          #pop item which has key 400
print(myDict.popitem())         #pop last item
del(myDict[100])                #delete item which has key 100
myDict.update({10000:"ram"})      #add new element at last
print(myDict.__sizeof__())

#Gitika Chouksey (0827CI201068)
#lamda function

square = lambda x:x*2

List = [1,2,3,4,5,6,7,8]
newList = list(map(square,List))
print(newList) 

#Gitika Chouksey (0827CI201068)
#class and object

#declaring class student
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

def details(self):
        print('name is : ',self.name)        
        print('age is : ',self.age)        
        print('grade is : ',self.grade)        
    
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def get_grade(self):
        return self.grade
    
    def set_name(self, name):
        self.name = name
    
    def set_age(self, age):
        self.age = age
    
    def set_grade(self, grade):
        self.grade = grade

#initializing object s1     
s1 = Student('kuldeep',20,92)
s1.details()

