import collections

def get_price(item, frequency):
    match item:
        case "A":
            return 50
        case _:
            return 0

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    result = collections.Counter(skus)
    total_price = 0
    for sku, frequency in result.items():
        total_price += get_price(sku, frequency)
    
    return total_price


