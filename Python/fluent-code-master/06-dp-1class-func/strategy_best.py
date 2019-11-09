# strategy_best.py
# Strategy pattern -- function-based implementation
# selecting best promotion from static list of functions

# START STRATEGY_BEST
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
            discount = self.promotion(self)
        return self.total() - discount

    def __repr__(self):
        fmt = '<Order total: {:.2f} due: {:.2f}>'
        return fmt.format(self.total(), self.due())


def fidelity_promo(order):
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

# BEGIN STRATEGY_BEST

promos = [fidelity_promo, bulk_item_promo, large_order_promo]  # <1>

def best_promo(order):  # <2>
    """Select best discount available
    """
    return max(promo(order) for promo in promos)  # <3>
# END STRATEGY_BEST

# BEGIN STRATEGY_BEST_TESTS
joe = Customer('John Doe', 0)
ann = Customer('Ann Smith', 1100)

cart = [LineItem('banana', 4, .5), LineItem('apple', 10, 1.5), LineItem('watermellon', 5, 5.0)]

banana_cart = [LineItem('banana', 30, .5), LineItem('apple', 10, 1.5)]

long_order = [LineItem(str(item_code), 1, 1.0) for item_code in range(10)]
    
joe_long_order_best = Order(joe, long_order, best_promo)  # <1>
print('joe_long_order_best = \n{0}'.format(joe_long_order_best))
print()

joe_bana_cart_best = Order(joe, banana_cart, best_promo)  # <2>
print('joe_banana_cart_best = \n{0}'.format(joe_bana_cart_best))
print()

ann_cart_best = Order(ann, cart, best_promo)  # <3>
print('ann_cart_best = \n{0}'.format(ann_cart_best))
print()
# END STRATEGY_BEST_TESTS