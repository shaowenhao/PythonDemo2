print("Hello World")

# case-sensitive letters(a-z) underscore number(0-9)
x = 5
y = "automation"
print(x)
print(y)

if 10 > 5:
    print("10 is greater than 5 ")

def sum(a,b):
    print(a+b)

x = sum(20,30)

a = 5
b = 2.5
c = 4j

print(type(a))
print(type(b))
print(type(c))

#Casting

x = int(2.5)
y =  float(1)
p = str(10)


x = "Hello World.."
print(x[6:11])

y = "   aaa,aaa  "
print(y.strip())
print(y.replace("a","Y"))
print(y.split(","))


print("Enter your name:")
x = input()
print("hello " +x)