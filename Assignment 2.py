#Write a program to create a list of fruits and copy only'e' letter fruits to the new list.
fruits = ["orange","apple","mango","grape","banana"]
new_fruits = []
for x in fruits:
    for y in x:
        if y=="e":
            new_fruits.append(x)
print(new_fruits)

#Write a program to find prime number or not
num=int(input("enter the number"))
count=0
for i in range(1,num+1):
    if num%i==0:
        count=count+1
if count==2:
    print("prime number")
else:
    print("not a prime number")
            
            
