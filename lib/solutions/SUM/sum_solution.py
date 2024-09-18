# noinspection PyShadowingBuiltins,PyUnusedLocal
def compute(x: int, y: int):
    if x < 0 or x > 100:
        raise ValueError
    return x + y
