import statistics


def python_functions(data):

    """
    Calculate a few statistics from
    the numeric list using Python functions.
    Inefficient due to repeated iteration.
    """

    stats = {}

    stats["len"] = len(data)
    stats["min"] = min(data)
    stats["max"] = max(data)
    stats["sum"] = sum(data)
    stats["mean"] = statistics.mean(data)
    stats["pstdev"] = statistics.pstdev(data)

    return stats


def single_iteration(data):

    """
    Calculate a few statistics from
    the numeric list using single iteration
    for increased efficiency.
    """

    sum_of_squares = 0

    stats = {}

    stats["len"] = len(data)
    stats["min"] = data[0]
    stats["max"] = data[0]
    stats["sum"] = 0

    for n in data:
        stats["min"] = min(stats["min"], n)
        stats["max"] = max(stats["max"], n)
        stats["sum"] += n
        sum_of_squares += n**2

    stats["mean"] = stats["sum"] / stats["len"]

    stats["pstdev"] = ((sum_of_squares / stats["len"]) - (stats["mean"]**2))**0.5

    return stats
