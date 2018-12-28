# Money Calculator #
This is a small script that helps you split an amount of money into banknotes, using a banknote stock.


## Usage ##

```python
from lib.MC import MoneyCalculator

# Amount to calculate
amount = 6342

mc = MoneyCalculator()
total_banknotes = mc.calculate(amount=amount)
```

Then make sure the transaction is not **reversed**.

```python
if not mc.revert:
    print("\nYour amount:")
    for banknote, how_many in total_banknotes.items():
        if how_many > 0:
            print("{how_many} banknote(s) of {banknote} {currency}".format(how_many=how_many, banknote=banknote, currency=mc.currency))
else:
    print(mc.revert[1])
```

See **example.py** for the full code.