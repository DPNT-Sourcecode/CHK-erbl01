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
        ],
    "G": [{"price": 20, "units_required": 1}],    
    "H": [
            {"price": 80, "units_required": 10},
            {"price": 45, "units_required": 5},
            {"price": 10, "units_required": 1},
        ], 
    "I": [{"price": 35, "units_required": 1}],    
    "J": [{"price": 60, "units_required": 1}], 
    "K": [
            {"price": 120, "units_required": 2},
            {"price": 70, "units_required": 1},
        ],   
    "L": [{"price": 90, "units_required": 1}], 
    "M": [{"price": 15, "units_required": 1}], 
    "N": [
            {"price": 40, "units_required": 1},
        ], 
    "O": [{"price": 10, "units_required": 1}], 
    "P": [
            {"price": 200, "units_required": 5},
            {"price": 50, "units_required": 1},
        ], 
    "Q": [
            {"price": 80, "units_required": 3},
            {"price": 30, "units_required": 1},
        ], 
    "R": [{"price": 50, "units_required": 1}], 
    "S": [{"price": 20, "units_required": 1}], 
    "T": [{"price": 20, "units_required": 1}], 
    "U": [
            {"price": 120, "units_required": 4},
            {"price": 40, "units_required": 1},
        ],
    "V": [
            {"price": 130, "units_required": 3},
            {"price": 90, "units_required": 2},
            {"price": 50, "units_required": 1},
        ], 
    "W": [{"price": 20, "units_required": 1}], 
    "X": [{"price": 17, "units_required": 1}], 
    "Y": [{"price": 20, "units_required": 1}], 
    "Z": [{"price": 21, "units_required": 1}], 
    }

BUY_X_GET_Y_FREE = {
    "B": {"item_required": "E", "units_required": 2},
    "M": {"item_required": "N", "units_required": 3},
    "Q": {"item_required": "R", "units_required": 3},
}

def get_item_price(sku: str, units: int) -> int:
    item_total = 0
    for offer in PRICES[sku]:
        units_with_offer = units / offer["units_required"]
        if units_with_offer >= 1:
            item_total += offer["price"] * math.floor(units_with_offer)
            units -= math.floor(units_with_offer) * offer["units_required"] 
    return item_total

def get_price(item: str, units: int, sku_units: dict) -> int:
    if item in BUY_X_GET_Y_FREE.keys():
        deal = BUY_X_GET_Y_FREE[item]
        units -= math.floor(sku_units[deal["item_required"]] / deal["units_required"])
    return get_item_price(item, units)
        



# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:
    allowed_items = set(PRICES.keys())
    if not all(char in allowed_items for char in skus):
        return -1

    result = collections.Counter(skus)
    total_price = 0
    for sku, frequency in result.items():
        total_price += get_price(sku, frequency, result)
    
    return total_price


