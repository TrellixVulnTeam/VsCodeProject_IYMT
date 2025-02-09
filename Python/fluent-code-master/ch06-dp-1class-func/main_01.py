# common library
#import os, sys
#sys.path.append(os.path.dirname(__file__))

#class
from collections import namedtuple

Customer = namedtuple('Customer', 'name fidelity')


class LineItem:

    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.price * self.quantity


class Order:  # the Context

    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion

    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total

    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion(self)  # <1>
        return self.total() - discount

    def __repr__(self):
        fmt = '<Order total: {:.2f} due: {:.2f}>'
        return fmt.format(self.total(), self.due())

# <2>

def fidelity_promo(order):  # <3>
    """5% discount for customers with 1000 or more fidelity points"""
    return order.total() * .05 if order.customer.fidelity >= 1000 else 0


def bulk_item_promo(order):
    """10% discount for each LineItem with 20 or more units"""
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * .1
    return discount


def large_order_promo(order):
    """7% discount for orders with 10 or more distinct items"""
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * .07
    return 0

'''
------------------------------------------------------------------------------------------------------------------------
6.1.2 Function-oriented strategy pattern
------------------------------------------------------------------------------------------------------------------------
'''
print('-----------------------------------------------------------------------------------------------------------------\n'
      '                           6.1.2 Function-oriented strategy pattern                                              \n'
      '-----------------------------------------------------------------------------------------------------------------\n')
joe = Customer('John Doe', 0)
ann = Customer('Ann Smith', 1100)
cart = [LineItem('banana', 4, .5),
        LineItem('apple', 10, 1.5),
        LineItem('watermellon', 5, 5.0)]

print('Order(joe, cart, fidelity_promo) = {0}'.format(Order(joe, cart, fidelity_promo)))

print('Order(ann, cart, fidelity_promo) = {0}'.format(Order(ann, cart, fidelity_promo)))

banana_cart = [LineItem('banana', 30, .5),
               LineItem('apple', 10, 1.5)]

print('Order(joe, banana_cart, bulk_item_promo) = {0}'.format(Order(joe, banana_cart, bulk_item_promo)))

long_order = [LineItem(str(item_code), 1, 1.0) for item_code in range(10)]

print('Order(joe, long_order, large_order_promo) = {0}'.format(Order(joe, long_order, large_order_promo)))

print('Order(joe, cart, large_order_promo) = {0}'.format(Order(joe, cart, large_order_promo)))
print()
