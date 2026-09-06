class CashRegister:
    def __init__(self, discount=0):
        
        self.discount = discount
        self.total = 0
        self.items = []
        
        
        self._last_transaction_amount = 0
        self._last_transaction_count = 0

    def add_item(self, title, price, quantity=1):
        
        transaction_amount = price * quantity
        
        
        self.total += transaction_amount
        
        self.items.extend([title] * quantity)
        
        
        self._last_transaction_amount = transaction_amount
        self._last_transaction_count = quantity

    def apply_discount(self):
        if self.discount > 0:
          
            discount_amount = self.total * (self.discount / 100)
            self.total -= discount_amount
            
            
            print(f"After the discount, the total comes to ${int(self.total)}.")
        else:
            
            print("There is no discount to apply.")

    def void_last_transaction(self):
        
        self.total -= self._last_transaction_amount
        
        if self._last_transaction_count > 0:
            self.items = self.items[:-self._last_transaction_count]
        
        self._last_transaction_amount = 0
        self._last_transaction_count = 0