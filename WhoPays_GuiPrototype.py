# Andrew McCollum, 2020
# WhoPays? Gui Prototype. Once this works with an interface, I will move on to actual mobil wireframes

# this file is not yet complete. The new math seems to be working well for even splits.
# next working on the math ideas for custom splits

import math
import tkinter as tk
from tkinter import *
from tkinter import ttk
from decimal import Decimal, ROUND_HALF_UP


def RoundItUp(number):
    dec_num = Decimal(number)
    return dec_num.quantize(Decimal(".01"), rounding=ROUND_HALF_UP)


def EvenSplit(bill: float, tip: float, peoples: float):
    # insert logic from WhoPays_CurrencyRoundingExperiment
    BillMath = round(Decimal(bill), 2)
    TipDec = Decimal(tip)
    TipMath = ((TipDec + 100) / 100)
    PplMath = Decimal(peoples)
    MathCost_Rounded = round((BillMath * TipMath), 2)
    EachPays = round((MathCost_Rounded / PplMath), 2)
    # function returs a list: Amount everyone pays, the bill, and the value of the tip
    PayList = [EachPays, (EachPays * PplMath), ((EachPays * PplMath) - BillMath)]
    return PayList


def Click_EvenSplit_Btn():
    bill = float(EntryEvenBill.get())
    tip = float(EntryEvenTip.get())
    peoples = float(EntryEvenPeeps.get())
    EvenSplitResults = EvenSplit(bill, tip, peoples)
    LblEvenResultPays.config(text=("Each person pays $" + str(EvenSplitResults[0])))
    LblEvenResultTotal.config(text=("The total cost is $" + str(EvenSplitResults[1])))
    LblEvenResultTipVal.config(text=("Write in a tip for $" + str(EvenSplitResults[2])))



root = tk.Tk()

root.wm_title("WhoPays?")
root.geometry("320x600")


TabControl = ttk.Notebook(root)

TabEven = ttk.Frame(TabControl)
TabCustom = ttk.Frame(TabControl)

TabControl.add(TabEven, text="Even split")
TabControl.add(TabCustom, text="Custom Split")
TabControl.pack(expand=1, fill="both")


# Fill interface for Even-split tab
LblEvenTitle = ttk.Label(TabEven, text="Everyone pays the same")
LblEvenTitle.place(x=32, y=16)
LblEvenBill = ttk.Label(TabEven, text="What is the total bill?")
LblEvenBill.place(x=32, y=64)
EntryEvenBill = ttk.Entry(TabEven, justify=LEFT)
EntryEvenBill.place(x=200, y=64)
LblEvenTip = ttk.Label(TabEven, text="What % do you want to tip?")
LblEvenTip.place(x=32, y=96)
EntryEvenTip = ttk.Entry(TabEven, justify=LEFT)
EntryEvenTip.place(x=200, y=96)
LblEvenPeeps = ttk.Label(TabEven, text="How many people are splitting?")
LblEvenPeeps.place(x=32, y=128)
EntryEvenPeeps = ttk.Entry(TabEven, justify=LEFT)
EntryEvenPeeps.place(x=200, y=128)
EvenSplit_GO = ttk.Button(TabEven, text="Split!", command=Click_EvenSplit_Btn)
EvenSplit_GO.place(x=32, y=160)
LblEvenResultPays = ttk.Label(TabEven, text="Each person pays $")
LblEvenResultPays.place(x=32, y=192)
LblEvenResultTotal = ttk.Label(TabEven, text="The total cost is $")
LblEvenResultTotal.place(x=32, y=224)
LblEvenResultTipVal = ttk.Label(TabEven, text="Write in a tip for $")
LblEvenResultTipVal.place(x=32, y=256)

# Fill interface for Custom-split tab
ttk.Label(TabCustom, text="Set each person's percentage").grid(column=0, row=0, padx=32, pady=32)


root.mainloop()
