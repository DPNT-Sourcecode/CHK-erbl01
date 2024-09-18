import collections

def get_price(item, frequency):
    match item:
        case "A":
            value = 50
            special_offer = 130
            if frequency > 3:
                frequency % 3
            return 50
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



