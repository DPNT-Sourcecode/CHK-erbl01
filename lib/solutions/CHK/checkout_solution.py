import collections
import math

def get_price(item, frequency):
    match item:
        case "A":
            value = 50
            special_offer = 130
            normal_priced_items = frequency % 3 * value
            special_offer_priced_items = math.floor(frequency / 3) * special_offer
            return normal_priced_items + special_offer_priced_items
        case "B": 
            value = 30
            special_offer = 45
            normal_priced_items = frequency % 2 * value
            special_offer_priced_items = math.floor(frequency / 2) * special_offer
            return normal_priced_items + special_offer_priced_items
        case "C":
            return 20 * frequency
        case "D":
            return 15 * frequency
        case _:
            return 0

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    if not all(char in {'A', 'B', 'C', 'D'} for char in skus):
        return -1

    result = collections.Counter(skus)
    total_price = 0
    for sku, frequency in result.items():
        total_price += get_price(sku, frequency)
    
    return total_price



