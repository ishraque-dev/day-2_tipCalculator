print('Welcome to the Tip Calculator!')
bill = float(input('What was the total bill? $'))
tip = int(input('How much tip would you like to give? 10, 12, 15'))
people = int(input("How many people to split the bill?"))
bill_with_tip = tip / 100 * bill + bill
bill_per_person = bill_with_tip/people
final_bill = "{:.2f}".format(bill_per_person)
print(final_bill)
