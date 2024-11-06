from main import TransportationProblem

problem = TransportationProblem(
    s=[140, 180, 160],
    d=[60, 70, 120, 130, 100],
    c=[
        [2, 3, 4, 2, 4],
        [8, 4, 1, 4, 1],
        [9, 7, 3, 7, 2]
    ]
)
problem.solve()
print(*problem.solution_by_north_west)
print(sum(problem.solution_by_north_west[i][j] * problem.c[i][j] for i in range(len(problem.c)) for j in range(len(problem.c[0]))))
print(*problem.solution_by_vogel)
print(sum(problem.solution_by_vogel[i][j] * problem.c[i][j] for i in range(len(problem.c)) for j in range(len(problem.c[0]))))
print(*problem.solution_by_russell)
print(sum(problem.solution_by_russell[i][j] * problem.c[i][j] for i in range(len(problem.c)) for j in range(len(problem.c[0]))))
print()

problem = TransportationProblem(
    s=[160, 140, 170],
    d=[120, 50, 190, 110],
    c=[
        [7, 8, 1, 2],
        [4, 5, 9, 8],
        [9, 2, 3, 6]
    ]
)
problem.solve()
print(*problem.solution_by_north_west)
print(sum(problem.solution_by_north_west[i][j] * problem.c[i][j] for i in range(len(problem.c)) for j in range(len(problem.c[0]))))
print(*problem.solution_by_vogel)
print(sum(problem.solution_by_vogel[i][j] * problem.c[i][j] for i in range(len(problem.c)) for j in range(len(problem.c[0]))))
print(*problem.solution_by_russell)
print(sum(problem.solution_by_russell[i][j] * problem.c[i][j] for i in range(len(problem.c)) for j in range(len(problem.c[0]))))
print()
