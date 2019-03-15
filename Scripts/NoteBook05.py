#! /home/cofia/miniconda3/bin/python
# Question 1 - Create a while loop that starts with x = 0 and increments x until x is equal to 5. Each iteration should print to the console.

x=0
while x<=5:
    print("Value:%d" %x)
    x = x+1

print("This is the end of the first question \n Next question is as below: ")

# Question 2 - Repeat the previous problem, but the loop will skip printing x = 5 to the console but will print values of x from 6 to 10
for x in range (100) :
    if x != 5 and x<=10 :
        print ("Value:%d" %x)

print("This is the end of the second question \n Next question is as below: ")
# Question 3 - Create a for loop that prints values from 4 to 10 to the console.

for x in range(4,100):
    if x>=4 and x<=10:
        print(x)

