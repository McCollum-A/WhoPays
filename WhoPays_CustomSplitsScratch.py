# Andrew McCollum, 2021
# WhoPays, Ideas for implementing custom split percentages

# This file is a work-in-progress

"""This part of the app is getting redone. Originally the custom split was allow a custom
percentage of the final bill that each person would pay. However, I realized there was no real
use for such a feature. Instead, this function will be renamed, and perform subtractive
math to equate how much a person needs to pay you back, tip inlcuded. E.G. you pay the bill
and Bob's item cost $25, this will compute how much of the tip that $25 added."""

from decimal import Decimal

# get starting info
print("Someone needs to pay you back?")
total_payed = Decimal(float(input("what was the final cost, including tip? $")))
tip_amount = Decimal(float(input("how much ($) was the tip? $")))
persons_cost = Decimal(float(input("and how much did this person's portion cost? $")))

# set base bill, and find percent of base that the portion cost
base_bill = total_payed - tip_amount
persons_percent = ((persons_cost / base_bill) * 100)

print(total_payed)
print("your total was " + str(total_payed))
print("and their item was " + str(persons_percent) + "% of it")
