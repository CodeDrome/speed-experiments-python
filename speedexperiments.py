import random
import sys
import os

import functiontimer
import statsfunctions
import statsfunctionscython


def main():

    print("---------------------")
    print("| codedrome.com     |")
    print("| Speed Experiments |")
    print("---------------------\n")

    print("Using {}\n".format(os.path.basename(sys.executable)))

    print("Generating random data...\n")
    random.seed()
    data = [random.randint(1, 100) for i in range(1000000)]

    # functiontimer.time_function(statsfunctions.python_functions,
    #                             data,
    #                             10)

    # functiontimer.time_function(statsfunctions.single_iteration,
    #                             data,
    #                             10)

    # functiontimer.time_function(statsfunctionscython.python_functions,
    #                             data,
    #                             10)

    functiontimer.time_function(statsfunctionscython.single_iteration,
                                data,
                                10)


main()
