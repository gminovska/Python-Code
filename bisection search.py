'''
Monthly interest rate = (Annual interest rate) / 12.0
Monthly payment lower bound = Balance / 12
Monthly payment upper bound = (Balance x (1 + Monthly interest rate)12) / 12.0
'''


balance = 320000
annualInterestRate = 0.2

mir = annualInterestRate/12 + 1
rb = balance
lo = balance/12
hi =(balance * mir ** 12)/12.0

while True:
    mp = (lo + hi)/2
    for i in range(1,13):
        rb = (rb - mp) * mir
        w = round (rb, 2)
    if w == 0.01:
        val = round(mp,2)
        print ('Lowest payment: ' + str(val))
        break
    if w > 0.01:
        lo = mp
        rb = balance
        continue
    elif w < 0.01:
        hi = mp
        rb = balance
        continue
    else:
        print ('Lowest payment: ' + str(mp))
        break
