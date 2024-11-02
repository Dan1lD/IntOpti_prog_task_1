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
print(problem.solve() + problem.solve_by_simplex())
print()

problem = OptimizationProblem(
    C=[1, 1],
    A=[
        [1, 2],
        [1, 2]
    ],
    signs=["<=", ">="],
    b=[0, 0],
)
print(problem.solve() + problem.solve_by_simplex())
print()

problem = OptimizationProblem(
    C=[1, 1],
    A=[
        [2, 4],
        [1, 3]
    ],
    signs=["<=", ">="],
    b=[16, 9],
    eps=0.00001,
    initial_trial_solution=[0.5, 3.5, 1, 2]
)
print(problem.solve() + problem.solve_by_simplex())
print()
