class MyClass:
    name = "Ryan wenhao"
    age = 20

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sum(self, aa, bb):
        print(aa + bb)


x = MyClass("Iris", 18)
print(x.name)
z = x.sum(5,7)

#del x  name 'x' is not defined
print(x.age)

