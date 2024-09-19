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

BUY_X_GET_Y_FREE = {
    "B": {"item_free": "E", "units_required": 2},
    "F": {"item_free": "E", "units_required": 2},
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
        units -= math.floor(sku_units[deal["item_free"]] / deal["units_required"])
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


