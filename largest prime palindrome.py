'''
largest prime palindrome less than 1000.

'''
l = []
for num in range (1, 1000):
    if num > 1:
	       for i in range(2,num):
	           if (num % i) == 0:
	               break
	       else:
	           pal = str(num)
	           if pal[0] == pal[-1]:
	               l.append(pal)
print max(l)