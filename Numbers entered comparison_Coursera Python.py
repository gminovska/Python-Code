#Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. Enter the numbers from the book for problem 5.1 and Match the desired output as shown. 
largest = None
smalest = None
step = 0
while True:
    entry = raw_input("Enter a number:")
    if entry == 'done': 
        print "Largest number entered:" + str(largest)
        print "Smallest number entered:" + str(smalest)
        break
    try:
           num = int(entry)
    except:
           print "Please enter a number, that input is not valid"
           continue
    if step == 0:
        largest = smalest = num
        step = 1
    if num > largest:   
        largest = num
    if num < smalest:
        smalest = num
    