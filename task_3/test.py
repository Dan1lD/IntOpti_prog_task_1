import pytest
from main import TransportationProblem

def test_1():
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
  expected_solution_by_north_west = [
    [6, 4, 0, 0],
    [0, 3, 5, 0],
    [0, 0, 3, 14]
  ]
  expected_solution_by_vogel = [
      [6, 0, 4, 0],
      [0, 7, 1, 0],
      [0, 0, 3, 14]
  ]
  expected_solution_by_russell = [
      [0, 7, 0, 3],
      [0, 0, 0, 8],
      [6, 0, 8, 3]
  ]
  assert problem.solution_by_north_west == expected_solution_by_north_west
  assert problem.solution_by_vogel == expected_solution_by_vogel
  assert problem.solution_by_russell == expected_solution_by_russell


def test_2():
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
  expected_solution_by_north_west = [
    [20, 0, 0, 0],
    [23, 35, 7, 0],
    [0, 0, 16, 60]
  ]
  expected_solution_by_vogel = [
      [0, 0, 0, 20],
      [43, 0, 0, 22],
      [0, 35, 23, 18]
  ]
  expected_solution_by_russell = [
      [0, 20, 0, 0],
      [0, 0, 5, 60],
      [43, 15, 18, 0]
  ]
  assert problem.solution_by_north_west == expected_solution_by_north_west
  assert problem.solution_by_vogel == expected_solution_by_vogel
  assert problem.solution_by_russell == expected_solution_by_russell


def test_3():
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
  expected_solution_by_north_west = [
    [27, 0, 0, 0],
    [28, 42, 15, 0],
    [0, 0, 20, 23]
  ]
  expected_solution_by_vogel = [
      [27, 0, 0, 0],
      [27, 0, 35, 23],
      [1, 42, 0, 0]
  ]
  expected_solution_by_russell = [
      [0, 0, 27, 0],
      [43, 42, 0, 0],
      [12, 0, 8, 23]
  ]
  assert problem.solution_by_north_west == expected_solution_by_north_west
  assert problem.solution_by_vogel == expected_solution_by_vogel
  assert problem.solution_by_russell == expected_solution_by_russell


def test_not_balanced():
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
  assert problem.solution_by_north_west is None
  assert problem.solution_by_vogel is None
  assert problem.solution_by_russell is None