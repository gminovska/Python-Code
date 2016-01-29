balance = 4842
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
monthlyInterestRate = annualInterestRate/12
total = 0
for i in range (1,13):
    print ('Month:' + str(i))
    minMonthlyPay = round((monthlyPaymentRate * balance), 2)
    total +=minMonthlyPay
    monthlyUnpaidBalance = balance - minMonthlyPay
    balance = round(((monthlyUnpaidBalance) + (monthlyInterestRate * monthlyUnpaidBalance)),2)
    #balance = round (balance + ((balance - minMonthlyPay) * (annualInterestRate/12)), 2) 
    print ('Minimum monthly payment:' + str(minMonthlyPay))
    print ('Remaining balance: ' + str(balance))
print ('Total paid: ' + str(total))
print ('Remaining balance: ' + str(balance))
