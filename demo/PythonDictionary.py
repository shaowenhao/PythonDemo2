my_dict = {
    "class" : "animal",
    "name" : "Bird",
    "age" : 5
}

print(my_dict)
print(my_dict["name"])
print(my_dict.get("age"))
print(my_dict.values())


for val in my_dict:
    print(val, my_dict[val])

for x,y in my_dict.items():
    print(x , y )

my_dict["color"] = "yellow"
print(my_dict)

#del my_dict
my_dict.clear()
print(my_dict)