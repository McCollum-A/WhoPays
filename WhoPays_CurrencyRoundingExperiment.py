import decimal
from decimal import Decimal

# get bill, tip %, & people
bill = float(input("price "))
tip = float(input("tip "))
ppl = int(input("ppl "))

# set bill & tip to dec, and create 1.xx tip percent
billM = Decimal(bill)
tipD = Decimal(tip)
tipM = ((tipD + 100) / 100)

# math only get mathmatical final cost
MathCost = (billM * tipM)
MathCostRND = round(MathCost, 2)

# test print the rounded final cost
print(MathCostRND)

# divide by people, round again, and test print
EachPays = MathCost/ppl
EachPaysRND = round(EachPays, 2)
print("MathCost: " + str(MathCost))
print("Rounded each: " + str(EachPaysRND))

# The final price is not mathmatically perfect, as show below
print("The total cost is $" + str((EachPaysRND * ppl)))
print("The mathematical price is $" + str(MathCost))
print("The tip in currency is +$" + str((EachPaysRND * ppl) - billM))
print("The mathematical tip is +$" + str(MathCostRND - billM))

# This small difference in cents is to allow for each person to pay an equal share, in currency,
# as opposed to e.g. two people paying $x.xx and the third paying ($x.xx + 0.01)
print("Everyone pays $" + str(EachPaysRND))

# What is the point of this app?
"""In a practical sense, this is for a scenario when a group pays with one check and everyone reimburses
the payee later. This however doesn't account for item price; if two people had a low cost item and a third person
 orders something expensive, then the other two are subsidising a part of the expensive item. However, if a group
 doesn't mind simply paying the payee back, then the group dynamic probably doesn't care about that potential
 subsidization."""