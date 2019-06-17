# 4 collection data type in Python

#List      []       ordered   | indexed | changeable | duplicates
#Tuple    ()        ordered   | indexed | unchangeable | duplicates
#Set       {}       unordered | unindexed | no duplicates
#Dictionary  {K:V}  unordered | changeable | indexed | no duplicates


# List| Tuple | Set |Dictionary

#List

my_list = ["China", "USA", "Jap"]
print(my_list)
print(my_list[0])

my_list[1] = "Europe"
print(my_list)

for val in my_list:
    print(val)

print(len(my_list))

my_list.append("Canada")
print(my_list)

my_list.insert(4,"Miland")
print(my_list)

my_list.remove("Jap")
print(my_list)

my_list.clear()
print(my_list)



fruits = ["apple", "orange", "banana"]
fruits.reverse()
print(fruits)

my_list2 = ["apple", 1, 2, 3.0]
my_list3 = ["aplles", [1,2,3], ['a','b','c']]
print(my_list3[1][2])