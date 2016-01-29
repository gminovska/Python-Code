l = []
for num in range (1, 1000000):
    if num > 1:
	       for i in range(2,num):
	           if (num % i) == 0:
	               break
	       else:
	           l.append(num)
    if len(l) == 1000:
        print (sum(l))
        quit ()
