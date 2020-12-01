# Andrew McCollum, 2020
# WhoPays? Gui Prototype

# this file is not yet complete

import math
import tkinter as tk
from tkinter import *
from tkinter import ttk
from decimal import Decimal, ROUND_HALF_UP


def RoundItUp(number):
    dec_num = Decimal(number)
    return dec_num.quantize(Decimal(".01"), rounding=ROUND_HALF_UP)


def EvenSplit(bill: float, tip: float, peoples: float):
    # add tip % to bill, then div by peeps
    tip_per = ((100 + tip) / 100)
    final_cost = (bill * tip_per)
    even_raw_math = final_cost / peoples
    return even_raw_math


def Click_EvenSplit_Btn():
    # for EvenSplit; bill(f), tip(i), peoples(i)
    bill = float(EntryEvenBill.get())
    tip = float(EntryEvenTip.get())
    peoples = float(EntryEvenPeeps.get())
    EvenTempFlt = EvenSplit(bill, tip, peoples)
    EvenFinal = RoundItUp(EvenTempFlt)
    LblEvenResult.config(text=("Each person pays: $" + str(EvenFinal)))




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
LblEvenResult = ttk.Label(TabEven, text="Each person pays: $")
LblEvenResult.place(x=32, y=192)

# Fill interface for Custom-split tab
ttk.Label(TabCustom, text="Set each person's percentage").grid(column=0, row=0, padx=32, pady=32)


root.mainloop()
