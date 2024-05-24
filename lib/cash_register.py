#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0, total=0, items=[], last_transaction=0):
    self.discount = discount
    self.total = total
    self.items = items
    self.last_transaction = last_transaction

  def add_item(self, title, price, quantity=1):
    self.items.append({'title': title, 'price': price, 'quantity': quantity})
    self.total += price * quantity

  def apply_discount(self):
    if self.discount > 0:
      discount_amount = self.total * (self.discount / 100)
      self.total -= discount_amount
      print(f"After the discount, the total comes to ${int(self.total)}.")
    else:
      print("There is no discount to apply.")

  
  
  pass
