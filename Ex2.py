#if with List Comprehension
#Gitika Chouksey 0827CI201068
#List Comprehension

number_list = [ x for x in range(20) if x % 2 == 0]
print(number_list)


#Lambda function with List Comprehension
#Gitika Chouksey 0827CI201068
#List Comprehension

lettersList = list(map(lambda x: x, 'human'))
print(lettersList)


#Nested if with List Comprehension
#Gitika Chouksey 0827CI201068
#List Comprehension

num_list = [y for y in range(100) if y % 2 == 0 if y % 5 == 0]
print(num_list)




#Nested if..elsewith List Comprehension
#Gitika Chouksey 0827CI201068
#List Comprehension

obj = ["Even" if i%2==0 else "Odd" for i in range(10)]
print(obj)



