# Andrew McCollum, 2020
# WhoPays, Ideas for implementing custom split percentages

# This file is a work-in-progress

from decimal import Decimal, ROUND_UP_HALF
import math


# create dictionary and percentage tracker for split percentages, etc
PplPercents = {}
PplPays = {}
Pof100 = 100
Tof100 = 0   # Used for checking that the custom splits equal to 100%

# Gather needed inputs
Ppl_C = int(input("How many people are paying? "))
Bill_C = float(input("What is the bill? "))
Tip_C = int(input("What percent tip?"))

# Convert to decimals, except tip
Ppl_C_D = Decimal(Ppl_C)
Bill_C_D = Decimal(Bill_C)

# Create Tip percentage and compute appx tip, and create decimal-appx-tip
Tip_C_P = ((Tip_C + 100) / 100)
Total_C_M = (Bill_C_D * Tip_C_P)
Tip_C_D = Decimal(Total_C_M - Bill_C_D)

# Round up final bill, tip, total
BillCustomFinal = Bill_C_D
TipCustomFinal = round(Tip_C_D, 2)
TotalCustomFinal = (BillCustomFinal + TipCustomFinal)

# Create loop to store percentages by name
for P in range(Ppl_C):
    TempName = input("Payee name: ")
    print("Percent of bill remaining: " + str(Pof100))
    TempPer = float(input("What percent will " + TempName + " pay?"))
    PplPercents[TempName] = TempPer
    Pof100 -= TempPer

# check that the custom percentages equal to 100%
CheckPers = PplPercents.values()
for T in range(len(CheckPers)):
    Tof100 += CheckPers[T]

if Tof100 == 100:
    pass
elif Tof100 != 100:
    print("Everyone's portions do not add up to 100%")


print("Results:   --------")
for Persons in PplPercents:
    TempTotal_AsHundredths = TotalCustomFinal / 100
    TempPaying_C_M = PplPercents[Persons] * TempTotal_AsHundredths



