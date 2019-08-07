import time
import statistics


def time_function(function, arguments, runcount):

    """
    Runs the function with the arguments the
    specified number of times.
    Prints the minimum, maximum and mean
    durations in milliseconds.    
    """

    print("Running " + function.__name__ + "...")

    durations = []

    for r in range(0, runcount):
        start_time = time.time()
        function(arguments)
        end_time = time.time()
        duration_ms = (end_time - start_time) * 1000
        durations.append(duration_ms)

    print("min:  {:6.0f}ms".format(min(durations)))
    print("max:  {:6.0f}ms".format(max(durations)))
    print("mean: {:6.0f}ms".format(statistics.mean(durations)))
