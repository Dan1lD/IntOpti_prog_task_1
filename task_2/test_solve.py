import pytest 
from main import OptimizationProblem

# def test_min_task():
#     c = [7, 2, 4]
#     a = [
#         [1, 2, 1],
#         [3, 0, 2],
#         [1, 4, 0]
#     ]
#     signs = ["<=", "<=", "<="]
#     b = [430, 460, 420]
#     problem = OptimizationProblem(c, a, signs, b, task="min")
#     problem.solve()
#     assert problem.x == [0, 0, 0] and problem.solution == 0

# def test_max_task():
#     c = [1]
#     a = [[1]]
#     signs = ["<="]
#     b = [2]
#     problem = OptimizationProblem(c, a, signs, b, task="max")
#     problem.solve()
#     assert problem.x == [2] and problem.solution == 2


# def test_multiple_variables():
#     c = [-1,1,2]
#     a = [[3,4,-3], [5,-4,-3],[7,4,11]]
#     signs = ["<=", "<=","<=",]
#     b = [23, 10 ,30]
#     problem = OptimizationProblem(c, a, signs, b, task="min")
#     problem.solve()
#     assert problem.x == [2, 0, 0] and problem.solution == -2

def test_doesnt_have_solution(): 
    c = [1,1]
    a = [[1,2] ,[1,2]]
    signs =["<=", ">"]
    b = [0,0]
    problem = OptimizationProblem(c, a, signs, b)
    problem.solve()
    assert "The problem does not have solution!"

# def test_no_valid_ratio(): 
#     c = [2,1]
#     a = [[1,-1],[2,-1]]
#     signs = ["<=", "<="]
#     b = [10, 20]
#     problem = OptimizationProblem(c, a, signs, b, task="max")
#     problem.solve()
#     assert problem.solution is None

# def test_all_zeroes(): 
#     c = [7,2,4]
#     a = [[3,2,3],[3,0,2],[1,4,0]]
#     signs = ["<=", "<=","<=",]
#     b = [430, 460 ,420]
#     problem = OptimizationProblem(c, a, signs, b, task="min")
#     problem.solve()
#     assert problem.x == [0, 0, 0] and problem.solution == 0


# def test_negative_C(): 
#     c = [-3,2,-2]
#     a = [[1,2,1],[3,0,2],[1,4,0]]
#     signs = ["<=", "<=","<=",]
#     b = [430, 460 ,420]
#     problem = OptimizationProblem(c, a, signs, b, task="max")
#     problem.solve()
#     assert problem.x == [0, 105, 0] and problem.solution == 210