import statistics


def python_functions(list data):

    """
    Calculate a few statistics from
    the numeric list using Python functions.
    Inefficient due to repeated iteration.

    This Cython implementation is no more
    efficient than the Python version
    and is only included for demonstration.
    """

    cdef int length = len(data)
    cdef double minval = min(data)
    cdef double maxval = max(data)
    cdef double total = sum(data)
    cdef double mean = statistics.mean(data)
    cdef double std_dev = statistics.pstdev(data)

    stats = {}
    stats["len"] = length
    stats["min"] = minval
    stats["max"] = maxval
    stats["sum"] = total
    stats["mean"] = mean
    stats["pstdev"] = std_dev

    return stats


def single_iteration(list data):

    """
    Calculate a few statistics from
    the numeric list using single iteration
    for increased efficiency.

    Very significant improvement on Python
    version due to typing.
    """

    cdef int length = len(data)
    cdef double minval = data[0]
    cdef double maxval = data[0]
    cdef double total = 0
    cdef double sum_of_squares = 0
    cdef double mean = 0
    cdef double std_dev = 0

    cdef double n
    for n in data:
        minval = min(minval, n)
        maxval = max(maxval, n)
        total += n
        sum_of_squares += n**2

    mean = total / length
    std_dev = ((sum_of_squares / length) - (mean**2))**0.5

    stats = {}
    stats["len"] = length
    stats["min"] = minval
    stats["max"] = maxval
    stats["sum"] = total
    stats["mean"] = mean
    stats["pstdev"] = std_dev

    return stats
