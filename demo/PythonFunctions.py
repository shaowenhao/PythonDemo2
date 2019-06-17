def printHello():
    print("HELLO")

printHello()

# function with parameter default value
def printHi(name ="wshao"):
    print("Hi " + name)

printHi("Ryan")
printHi()

def returnSum(a,b):
    return (a+b)
x = returnSum(10,20)
print(x)