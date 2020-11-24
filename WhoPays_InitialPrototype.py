# Created by Andrew McCollum
# Project: "WhoPays?", started Nov 22nd 2020

"""This console based script is the prototype for a cost splitting app for android, IPhone, and LinuxPhone.
It's intended purpose is to provide a quick way to determine how to split a [restaurant] bill quickly
when the party doesn't want to do math. This prototype is only to infer functionality, and so comments will
explain code and intended app UI features"""

import math  # For the rounding function "RoundItUp"


def RoundItUp(number: float, decimals: int = 2):  # Function is only ever sent the "number" args.
    factor = 10 ** decimals
    return math.ceil(number * factor) / factor


CustomSplit = False  # defaults to an even split, This will be replaced by a UI RadioButton or Toggle
Bill = float(input("What is the total bill? $"))  # This will be a CharField + Label
Tip = float(input("What percent Tip are you providing? %"))  # This will be a CharField + Label
Peeps = int(input("How many people are splitting? "))  # This will be a CharField + Label
EvenSplit = input("Are you doing an even split per person? ")  # This will be replaced by a UI RadioButton or Toggle

if EvenSplit == "yes" or "Yes" or "YES" or "y" or "Y":
    CustomSplit = False
elif EvenSplit == "no" or "No" or "NO" or "n" or "N":
    CustomSplit = True
else:
    CustomSplit = False
# The entire above if/elif/else will be replaced by a UI RadioButton or Toggle


if CustomSplit:  # for custom splitting of the bill
    RemainingPer = 100
    PeepSplits = {}
    TotalCost = (Bill + (Bill / Tip))  # Total monies owed
    for x in range(0, Peeps):
        print("Remaining percent: " + str(RemainingPer) + "%")  # Will be replaced with a graphic visualization
        PeepName = input("Person's name: ")  # Will be a tapped CharField
        PeepPer = float(input("Percent of the bill " + PeepName + " is paying: "))  # Will be a tapped CharField
        PeepPays = (TotalCost * (PeepPer / 100))
        PeepSplits[PeepName] = RoundItUp(PeepPays)  # Adds person + their owed amount to dictionary
        RemainingPer -= PeepPer  # Will be replaced with a graphic visualization

    for peep in PeepSplits.keys():  # Prints out custom split results
        print(peep + " pays $" + str(PeepSplits[peep]))
elif not CustomSplit:  # Simple math and print for even bill splitting
    TotalCost = (Bill + (Bill / Tip))
    MathSplit = TotalCost/Peeps
    FinalSplit = RoundItUp(MathSplit)
    print("Each person pays $" + (str(FinalSplit)))
