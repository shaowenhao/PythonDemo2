num = -1

# if elif else
if num > 0:
    print("positive number")
elif num == 0:
    print("Number is zero")
else:
    print("negative Number")

# for loop  else with for loop

nums = [1,2,3,4,5]
for val in nums:
    print(val)
else:
    print("No val left!!")

sum = 0
for val in nums:
    sum = sum +val
print("sum is",sum)

# while loop
print("Enter an nuber:")
num = int(input())
sum = 0
i = 1
while i < num:
    sum = sum+i
    i = i+1
print("total is:",sum)