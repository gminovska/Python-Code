# This is a solution to the first problem on Euler, finding the sum of all the multiples of 3 or 5 for numbers less than 1000

l =[i for i in range (1,1000) if i % 3 == 0 or i % 5 == 0]
print sum(l)

#an alternative is the folowing:

result = 0

for i in range (0,1000):
    if i % 3 ==0 or i % 5 ==0:
        result = result + i
print result       
