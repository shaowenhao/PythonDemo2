my_set ={"aa", "bb", "cc"}
print(my_set)

# can't use my_set[1]

for val in my_set:
    print(val)

print("cc" in my_set)

my_set.add("dd")
print(my_set)

my_set.update(["ee"])
print(my_set)

# remove not existed element throw error, so you can use discard
my_set.remove("aa")
print(my_set)
my_set.discard("bb")
print(my_set)


# change list into set
my_list = [1,2,3]
my_set3 = set(my_list)
print(my_set3)


#UNION | INTERECTION | DIFF | SYMMETRIC | DIFF

A = {'A', 'B', 1, 2, 3}
B = {'B', 'C', 3, 4, 5}
print(A.union(B))
print(A | B)

A.intersection(B)
A & B

A.difference(B)
A - B

