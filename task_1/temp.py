from main import OptimizationProblem


print(OptimizationProblem(
    [9, 10, 16],
    [
        [18, 15, 12],
        [6, 4, 8],
        [5, 3, 3]
    ],
    ["<=", "<=", "<="],
    [360, 192, 180]
))
print("\n")

print(OptimizationProblem(
    [-2, 2, -6],
    [
        [2, 1, -2],
        [1, 2, 4],
        [1, -1, 2]
    ],
    ["<=", "<=", "<="],
    [24, 23, 10],
    task="min"
))
print("\n")

print(OptimizationProblem(
    [7, 2, 4],
    [
        [1, 2, 1],
        [3, 0, 2],
        [1, 4, 0]
    ],
    [">=", "<=", "<="],
    [430, 460, 420],
    task="min"
))
print("\n")

print(OptimizationProblem(
    [4, 14],
    [
        [2, 7],
        [7, 2]
    ],
    ["<=", "<="],
    [21, 21]
))
print("\n")
