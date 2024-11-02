import pytest
from main import OptimizationProblem


def test_1():
    eps = 0.0001
    problem = OptimizationProblem(
        C=[9, 10, 16],
        A=[
            [18, 15, 12],
            [6, 4, 8],
            [5, 3, 3],
        ],
        signs=["<=", "<=", "<="],
        b=[360, 192, 180],
        eps=eps,
    )
    solution = [0, 8, 20, 0, 0, 96]
    problem.solve()
    problem.solve_by_simplex()
    assert all(abs(problem.solutions_by_interior_point[0.5][i] - solution[i]) <= eps for i in range(len(solution)))
    assert all(abs(problem.solutions_by_interior_point[0.9][i] - solution[i]) <= eps for i in range(len(solution)))
    assert all(abs(problem.solution_by_simplex[i] - solution[i]) <= eps for i in range(len(problem.solution_by_simplex)))


def test_2():
    eps = 0.0001
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
    solution = [6, 1, 0, 0]
    problem.solve()
    assert all(abs(problem.solutions_by_interior_point[0.5][i] - solution[i]) <= eps for i in range(len(solution)))
    assert all(abs(problem.solutions_by_interior_point[0.9][i] - solution[i]) <= eps for i in range(len(solution)))


def test_3():
    eps = 0.0001
    problem = OptimizationProblem(
        C=[1],
        A=[[1]],
        signs=["<="],
        b=[2],
        eps=eps,
    )
    solution = [2]
    problem.solve()
    assert all(abs(problem.solutions_by_interior_point[0.5][i] - solution[i]) <= eps for i in range(len(solution)))
    assert all(abs(problem.solutions_by_interior_point[0.9][i] - solution[i]) <= eps for i in range(len(solution)))


def test_doesnt_have_solution():
    c = [1, 1]
    a = [[1, 2], [1, 2]]
    signs = ["<=", ">="]
    b = [0, 0]
    problem = OptimizationProblem(c, a, signs, b)
    res = problem.solve()
    assert res == "The problem does not have solution!\n"


def test_doesnt_have_solution1():
    c = [1, 1, 1/7]
    a = [[0, 1/3, 1/7], [2, 0, 1/7], [2, 2/3, 3/7]]
    signs = ["<=", "<=", "<="]
    b = [2, 3, 7]
    problem = OptimizationProblem(c, a, signs, b)
    res = problem.solve()
    assert res == "The problem does not have solution!\n"
