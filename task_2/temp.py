from main import OptimizationProblem

problem = OptimizationProblem(
    C=[9, 10, 16],
    A=[
        [18, 15, 12],
        [6, 4, 8],
        [5, 3, 3],
    ],
    signs=["<=", "<=", "<="],
    b=[360, 192, 180],
    eps=0.0001,
)
problem.solve()
