import collections
import math

PRICES = {
    "A": [
            {"price": 200, "units_required": 5}, 
            {"price": 130, "units_required": 3}, 
            {"price": 50, "units_required": 1}
        ], 
    "B": [
            {"price": 45, "units_required": 2}, 
            {"price": 30, "units_required": 1}
        ],
    "C": [{"price": 20, "units_required": 1}],
    "D": [{"price": 15, "units_required": 1}],
    "E": [{"price": 40, "units_required": 1}],
    "F": [
            {"price": 20, "units_required": 3},
            {"price": 10, "units_required": 1}
        ]}

def get_item_price(sku: str, units: int):
    item_total = 0
    for offer in PRICES[sku]:
        units_with_offer = units / offer["units_required"]
        if units_with_offer >= 1:
            item_total += offer["price"] * math.floor(units_with_offer)
            units -= math.floor(units_with_offer) * offer["units_required"] 
    return item_total

def get_price(item: str, units: int, sku_units: dict) -> int:
    if item == "B":
        units -= math.floor(sku_units["E"] / 2)
    return get_item_price(item, units)
        

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




