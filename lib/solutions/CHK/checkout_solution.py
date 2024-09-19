import collections
import math

prices = {"A": [{"price": 200, "units_required": 5}, {"price": 130, "units_required": 3}, {"price": 50, "units_required": 1}], "E": [{"price": 50, "unites_required": 2}, {"price": 40, "units_required": 1}]}

total = 0
for sku, frequency in {"A": 6, "E": 1}:
    x = 0
    for offer in prices:
        if frequency / offer["unit_required"] >= 1:
            x += offer["price"] * math.floor(frequency / offer["unit_required"])
            frequency -= math.floor(frequency / offer["unit_required"]) * offer["unit_required"] 


def get_price(item: str, frequency: int, sku_frequencies: dict) -> int:
    match item:
        case "A":
            value = 50
            special_offer = 130
            bulk_special_offer = 200

            bulk_special_offer_priced_items = 0
            if frequency / 5 >= 1:
                bulk_special_offer_priced_items = math.floor(frequency / 5) * bulk_special_offer
                frequency -= math.floor(frequency / 5) * 5
            normal_priced_items = frequency % 3 * value
            special_offer_priced_items = math.floor(frequency / 3) * special_offer
            return normal_priced_items + special_offer_priced_items + bulk_special_offer_priced_items
        case "B": 
            value = 30
            special_offer = 45
            if sku_frequencies["E"] / 2 >= 1:
                frequency -= math.floor(sku_frequencies["E"] / 2)
            normal_priced_items = frequency % 2 * value
            special_offer_priced_items = math.floor(frequency / 2) * special_offer
            return normal_priced_items + special_offer_priced_items
        case "C":
            return 20 * frequency
        case "D":
            return 15 * frequency
        case "E":
            return 40 * frequency
        case _:
            return 0

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    allowed_items = {'A', 'B', 'C', 'D', 'E'}
    if not all(char in allowed_items for char in skus):
        return -1

    result = collections.Counter(skus)
    total_price = 0
    for sku, frequency in result.items():
        total_price += get_price(sku, frequency, result)
    
    return total_price

