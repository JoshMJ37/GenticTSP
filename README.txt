Names:
    Joshua Martin-Jaffe,    jmjaffe37@gatech.edu
    Cecilia Liu,            jliu738@gatech.edu

    submitted:      04/16

Files:
    tsp-3510.py:
        This is the main file which we use to get a solution for the TSP
        problem. Here, we implement a Genetic Algorithm (with imports from
        TSP.py). We also have some helper functions implemented here like
        our breed function (breeds to parent tours to make a new child tour)
        and tournyWinner function (chooses a parent as the least cost tour
        in a random mating pool).

    TSP.py:
        This file contains the class which holds a lot of the functions used
        in our genetic algorithm. This class also holds a lot of the data
        about the algorithm so it doesn't have to be passed in each time.

    __init__.py:
        Standard python file that allows imports from same folder

    algorithm.pdf:
        PDF document which describes our algorithm in more depth and
        explains the rationale behind the design.

Running:
    example command line input:
        python3.7 tsp-3510.py mat-test.txt tour.txt 300 t

    where:
        main python file:       tsp-3510.py
        input nodes txt file:   mat-test.txt
        output nodes txt file:  tour.txt
        number of seconds to run our algorithm: 300
        verbose:    t
            -> any of the following inputs: ['true', '1', 't', 'y'] = True
            -> anything else (or leaving blank) will make verbose=False
            -> verbose will show:   currrent generation
                                    current best tour cost
                                    total time elapsed up to current generation
            -> also shows starting cost and ending cost

Limitations:
    Becasue our algorithm is based on randomness, our algorithm is more
    likely to be less effective as the number of nodes increases. Because of
    this, we recommend running for 600 seconds if the number of
    nodes >= 1000.
