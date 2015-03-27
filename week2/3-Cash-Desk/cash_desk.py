class Bill:

    def __init__(self, amount):
        self.amount = amount

    def __str__(self):
        return "A {}$ bill".format(self.amount)

    def __repr__(self):
        return self.__str__()

    def __int__(self):
        return self.amount

    def __eq__(self, other):
        return self.amount == other.amount

    def __hash__(self):
        return hash(str(self.amount))


class BatchBill:

    def __init__(self, bills):
        self.bills = bills

    def total(self):
        return sum([int(bill) for bill in bills])

    # len() върху инстанцията извиква __len__
    def __len__(self):
        return len(self.bills)

    # Когато обхождаме клас с for се извиква getitem__, но е нужда да има и len
    def __getitem__(self, index):
        return self.bills[index]


class CashDesk:

    def __init__(self):
        self.gold = 0
        self.bank = {}

    def add_in_bank(self, money):
        if isinstance(money, Bill):
            if money in self.bank:
                self.bank[money] += 1
            else:
                self.bank[money] = 1
        elif isinstance(money, BatchBill):
            for bill in money:
                if bill in self.bank:
                    self.bank[bill] += 1
                else:
                    self.bank[bill] = 1

    def take_money(self, money):
        self.add_in_bank(money)
        if isinstance(money, Bill):
            self.gold += int(money)
        elif isinstance(money, BatchBill):
            self.gold += money.total()

    def total(self):
        return self.gold

    def inspect(self):
        return self.bank

values = [10, 20, 50, 100]
bills = [Bill(value) for value in values]

batch = BatchBill(bills)

desk = CashDesk()

desk.take_money(batch)
desk.take_money(Bill(10))

print(desk.total())
print(desk.inspect())
