# noinspection PyShadowingBuiltins,PyUnusedLocal
def compute(x: int, y: int):
    if x < 0 or x > 100:
        raise ValueError("Number has to be between 0 and 100")

    if y < 0 or y > 100:
        raise ValueError("Number has to be between 0 and 100")

    return x + y