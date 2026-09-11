class CashRegister:
    """Model a cash register that tracks items, totals and discounts."""

    def __init__(self, discount=0):
        # backing value for the validated discount property
        self._discount = 0
        # goes through the property setter so invalid input is rejected
        self.discount = discount

        self.total = 0
        self.items = []
        # each entry records the item, price and quantity of one add_item call
        self.previous_transactions = []

    @property
    def discount(self):
        """Percentage taken off the total (0-100)."""
        return self._discount

    @discount.setter
    def discount(self, value):
        # a discount must be a whole percentage between 0 and 100 inclusive
        if isinstance(value, int) and 0 <= value <= 100:
            self._discount = value
        else:
            print("Not valid discount")

    def add_item(self, item, price, quantity=1):
        """Add `quantity` of `item` at `price` each to the register."""
        transaction_amount = price * quantity
        self.total = round(self.total + transaction_amount, 2)

        # one entry in items per unit purchased
        self.items.extend([item] * quantity)

        # keep the transaction so it can be voided later
        self.previous_transactions.append({
            "item": item,
            "price": price,
            "quantity": quantity,
        })

    def apply_discount(self):
        """Reduce the total by the register's discount percentage."""
        if self.discount > 0:
            reduction = self.total * (self.discount / 100)
            self.total = round(self.total - reduction, 2)
            print(f"After the discount, the total comes to ${int(self.total)}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        """Undo the most recent add_item call."""
        if not self.previous_transactions:
            print("There is no transaction to void.")
            return

        last = self.previous_transactions.pop()

        # roll back the total
        self.total = round(self.total - last["price"] * last["quantity"], 2)

        # roll back the items added by that transaction
        if last["quantity"] > 0:
            del self.items[-last["quantity"]:]
