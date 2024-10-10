import pytest 
from typing import List, Union
from main import solve

def test_min_task():
    c = [10]
    a = [[1]]
    signs = [">="]
    b = [2]
    result = solve(c, a, signs, b, task="min")
    assert result[0] == [2] and result[1] == 20

def test_max_task():
    c = [1]
    a = [[1]]
    signs = ["<="]
    b = [2]
    result = solve(c, a, signs, b, task="max")
    assert result[0] == [2] and result[1] == 2

def test_empty_lists():
    c = []
    a = [[]]
    signs = []
    b = []
    eps = 0.00001
    result = solve(c, a, signs, b, task="max")
    assert result == "- solver_state: unbounded"

def test_multiple_variables():
    c = [-1,1,2]
    a = [[3,4,-3], [5,-4,-3],[7,4,11]]
    signs = ["<=", "<=","<=",]
    b = [23, 10 ,30]
    result = solve(c, a, signs, b, task="min")
    assert result[0] == [2, 0, 0] and result[1] == -2

def test_multiple_solutions(): 
    c = [4,14]
    a = [[2,7] ,[7,2]]
    signs =["<=", "<="]
    b = [21,21]
    result = solve(c, a, signs, b, task="min")
    assert result[0] == [0, 3] and result[1] == 42

def test_no_valid_ratio(): 
    c = [2,1]
    a = [[1,-1],[2,-1]]
    signs = ["<=", "<="]
    b = [10, 20]
    result = solve(c, a, signs, b, task="max")
    assert result == "- solver_state: unbounded"

def test_all_zeroes(): 
    c = [7,2,4]
    a = [[3,2,3],[3,0,2],[1,4,0]]
    signs = ["<=", "<=","<=",]
    b = [430, 460 ,420]
    result = solve(c, a, signs, b, task="min")
    assert result[0] == [0, 0, 0] and result[1] == 0


def test_negative_C(): 
    c = [-3,2,-2]
    a = [[1,2,1],[3,0,2],[1,4,0]]
    signs = ["<=", "<=","<=",]
    b = [430, 460 ,420]
    result = solve(c, a, signs, b, task="max")
    assert result[0] == [0, 105, 0] and result[1] == 210


def test_precision_error():
    #черновик - не разобралась как тестить пока
    c = [1e-10]
    a = [[1]]
    signs = [">="]
    b = [1e-10]
    eps = 1e-12
    result = solve(c, a, signs, b, eps, task="max")
    assert abs(result - 1e-10) < eps