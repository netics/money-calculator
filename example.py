import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "lib"))

from lib.MC import MoneyCalculator

# Amount to calculate
amount = 6342

mc = MoneyCalculator()
total_banknotes = mc.calculate(amount=amount)

if not mc.revert:
    print("\nYour amount:")
    for banknote, how_many in total_banknotes.items():
        if how_many > 0:
            print("{how_many} banknote(s) of {banknote} {currency}".format(how_many=how_many, banknote=banknote, currency=mc.currency))
else:
    print(mc.revert[1])