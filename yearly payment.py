'''
write a program that calculates the minimum fixed
monthly payment needed in order pay off a credit card balance within 12 months
Assume that the interest is compounded monthly
according to the balance at the end of the month (after the payment for that month is made).
The monthly payment must be a multiple of $10 and is the same for all months.
'''
balance = 3926
annualInterestRate = 0.2
mir = annualInterestRate/12 + 1
rb = balance
mp = 10

while True:
    for i in range(1,13):
        rb = (rb - mp) * mir
    if rb > 0:
        mp +=10
        rb = balance
        continue
    else:
        print ('Lowest payment: ' + str(mp))
        break



