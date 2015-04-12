class Bill:

    def __init__(self, amount):

        if not isinstance(amount, int):
            raise TypeError

        if amount < 0:
            raise ValueError

        self.amount = amount

    def __str__(self):
        return "A {}$ bill".format(self.amount)

    def __repr__(self):
        return "{}$ bills".format(self.amount)

    def __int__(self):
        return self.amount

    def __eq__(self, other):
        return self.amount == other.amount

    def __hash__(self):
        return hash(str(self.amount))

    def __lt__(self, other):
        return int(self) < int(other)


class BatchBill:

    def __init__(self, bills):
        self.bills = bills

    def total(self):
        return sum([int(bill) for bill in self.bills])

    # len() върху инстанцията извиква __len__
    def __len__(self):
        return len(self.bills)

# Когато обхождаме клас с for се извиква getitem, но е нужно да има и __len__
    def __getitem__(self, index):
        return self.bills[index]


class CashDesk:

    def __init__(self):
        self.gold = 0
        self.bank = {}

    def add_in_bank(self, money):
        if money in self.bank:
            self.bank[money] += 1
        else:
            self.bank[money] = 1

    def take_money(self, money):
        if isinstance(money, Bill):
            self.gold += int(money)
            self.add_in_bank(money)
        elif isinstance(money, BatchBill):
            self.gold += money.total()
            for bill in money:
                self.add_in_bank(bill)

    def total(self):
        return "We have a total of {}$ in the bank".format(self.gold)

    def inspect(self):
        sorted_bills = sorted(self.bank)
        print("We have the following count of bills,\
 sorted in ascending order:")
        for bill in sorted_bills:
            print("{} - {}".format(repr(bill), self.bank[bill]))
