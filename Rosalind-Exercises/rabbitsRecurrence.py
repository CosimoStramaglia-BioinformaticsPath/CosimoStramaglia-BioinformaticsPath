def rabbits_recurrence(months: int, litter: int) -> str:
    """
    Calculates the total rabbit population using a modified Fibonacci sequence.

    Args:
        months (int): The number of months to simulate.
        litter (int): The litter of offspring pairs produced by each mature pair.

    Returns:
        int: The total number of rabbits.
    """
    # Base case: The population starts with 1 pair for the first two months
    # as they need time to reach reproductive maturity.
    total_rabbit_pairs = {1: 1, 2: 1}

    for m in range(3, months+1):
        # Recurrence formula:
        # Current Total = (Existing pairs from the previous generation) + (Mature pairs from 2 months ago * litter size)
        total_rabbit_pairs[m] = total_rabbit_pairs[m-1] + total_rabbit_pairs[m-2] * litter

    return "Total rabbit pairs: " + str(total_rabbit_pairs.popitem()[1])

rabbits_recurrence(int(input("Number of months: ")), int(input("Number of litter pairs: ")))