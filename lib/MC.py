from collections import OrderedDict

class MoneyCalculator(object):

    def __init__(self, banknotes=None, currency='RON'):
        # Set the banknotes stock
        if banknotes is None:
            self.banknotes = OrderedDict({
                500: 100,
                200: 10,
                100: 36,
                50: 12,
                10: 2,
                5: 500,
                1: 500
            })
        else:
            assert isinstance(banknotes, OrderedDict)
            self.banknotes = banknotes

        # Initialize the object keys to be 0
        items = [(key, 0) for key, value in self.banknotes.items()]
        self.total_banknotes = OrderedDict(items)
        self.revert = False
        self.currency = currency

    def calculate(self, amount):
        """

        :param amount:
        :return:
        """
        assert isinstance(amount, int)

        original_amount = amount
        while True:
            previous_amount = amount

            # Iterate all banknote types
            for banknote, stock in self.banknotes.items():
                stock, banknote = int(stock), int(banknote)
                how_many = int(amount / banknote)

                # If the division is more than 0 and we have a valid stock
                if how_many != 0:
                    # If the stock is lower than how much we will need, take all available
                    if stock <= how_many:
                        # Take all from the stock
                        how_many = stock
                        self.banknotes[banknote] = 0
                    elif stock > how_many:
                        # Update the new stock (extracting the difference)
                        self.banknotes[banknote] = int(stock - how_many)

                    # Update the total banknotes
                    self.total_banknotes[banknote] = self.total_banknotes[banknote] + how_many

                    # Update the new amount (difference remained)
                    amount = amount - (how_many * banknote)

            # If we reached 0, then stop the infinite loop
            if amount == 0:
                break
            else:
                if amount == previous_amount:
                    if amount == original_amount:
                        self.revert = True, "We do not have enough money!"
                    else:
                        self.revert = True, "We don't have all the money required! Amount remained: {amount}".format(amount=amount)
                    break

        return self.total_banknotes