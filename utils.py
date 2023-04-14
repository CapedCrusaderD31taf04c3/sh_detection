from functools import reduce
def distance_by_subtraction(elements :list[int, float]) -> float:
    """
    distance always return positive value
    """
    average_neg = abs(reduce(lambda x, y: x - y, elements) / len(elements))

    return average_neg
