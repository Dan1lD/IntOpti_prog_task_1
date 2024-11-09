from main import TransportationProblem

#balanced case
problem = TransportationProblem(
    s=[10, 8, 17],
    d=[6, 7, 8, 14],
    c=[
        [21, 40, 30, 15],
        [60, 25, 50, 55],
        [45, 10, 60, 10]
    ]
)
problem.solve()

#balanced case
problem = TransportationProblem(
    s=[20, 65, 76],
    d=[43, 35, 23, 60],
    c=[
        [7, 8, 1, 2],
        [4, 5, 9, 8],
        [9, 2, 3, 6]
    ]
)
problem.solve()

#balanced case
problem = TransportationProblem(
    s=[27, 85, 43],
    d=[55, 42, 35, 23],
    c=[
        [13, 8, 30, 12],
        [20, 19, 5, 10],
        [11, 3, 14, 28]
    ]
)
problem.solve()

#not balanced case
problem = TransportationProblem(
    s=[20, 65, 76],
    d=[33, 10, 43, 50],
    c=[
        [7, 8, 1, 2],
        [4, 5, 9, 8],
        [9, 2, 3, 6]
    ]
)
problem.solve()