
my_tuple = ("apple", "orange", "grapes")

print(my_tuple)
print(my_tuple[1])

print(my_tuple[-1])

print(my_tuple[0:2])

for val in my_tuple:
    print(val)

# tuple object does not support item support
#my_tuple[1] = "Banana"

my_tuple_2 = ("name",(1,2,3),['a','b','c'])
print(my_tuple_2)

# it can change value of list which as element in tuple
my_tuple_2[2][1] = 'A'
print(my_tuple_2)

print("name" in my_tuple_2) #true