import math
from typing import List, Tuple


def calc_fame(fame_gained: int, gold: int, gold_fame_price: int = 30, max_fame: int = 200) -> int:
    if fame_gained > max_fame:
        return -1

    base_fame = math.floor(gold / gold_fame_price)

    if base_fame + fame_gained > max_fame:
        base_fame = max_fame - fame_gained

    gold_fame_price *= 0.7 + 1.8 * (base_fame+fame_gained) / max_fame

    fame = math.floor(gold / gold_fame_price)

    if fame_gained + fame > max_fame:
        return -1

    return fame


def simulate_donations(row: List[int], paid: int = 0, gained: int = 0) -> Tuple[int, int]:
    for amount in row:
        fame = calc_fame(gained, amount)
        if fame > 0:
            gained += fame
            paid += amount

    return paid, gained


donations = [255, 262, 260, 251, 268, 250, 263, 278, 291, 259, 269, 280, 290, 250, 255, 262, 269, 277, 284, 290, 297, 305, 312, 253, 257, 262, 266, 271, 276, 280, 284, 289, 293, 297, 300, 300]

print(simulate_donations(donations))
