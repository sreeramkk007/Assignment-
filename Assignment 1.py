#write a program to find odd or even number using conditional statement
n=int(input("Enter a number"))
if n%2 == 0 :
 print("Even number")
else :
 print("Odd number")

#Find largest of three numbers
a=int(input("Enter first number"))
b=int(input("Enter second number"))
c=int(input("Enter third number"))
if a>=b and a>=c:
 largest = a
elif b>=a and b>=c:
 largest = b
else:
 largest = c
print("The largest number is ",largest)

#Find leap year using conditional statement
year=int(input("Enter a year"))
if year%4 == 0:
    if year%100 != 0 or year%400 == 0:
        print("leap year")
    else:
       print ("non leap year")
else:
       print ("non leap year")

#Find summing of numbers using while loop
num = int(input("Enter sum upto:"))
i=0
sum=0
while i<=num:
    sum=sum+i
    i=i+1    
print("sum:",sum)

#Find countdown of a number using while loop
num = int(input("Count upto:"))
i=0
while i<num :
    i=i+1
    print(i)















 



 
