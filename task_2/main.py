from math import inf
from typing import Literal

import numpy as np


class OptimizationProblem:
    def __init__(
            self,
            C: list[int | float],
            A: list[list[int | float]],
            signs: list[Literal[">=", "<=", "="]],
            b: list[int | float],
            eps: float = 0.0001,
            task: Literal["min", "max"] = "max",
            initial_trial_solution: list[float | int] | None = None
    ):
        self.C = C
        self.A = A
        self.signs = signs
        self.b = b
        self.eps = eps
        self.task = task
        self.initial_trial_solution = initial_trial_solution

        self.solutions_by_interior_point: dict[float, list[float]] = {}
        self.values_by_interior_point: dict[float, float] = {}

        self.solution_by_simplex: list[float | int] | None = None
        self.value_by_simplex: float | None = None

    def solve(self, alphas: list[float] | None = None):
        C = self.C.copy()
        A = [line.copy() for line in self.A]

        if alphas is None:
            alphas = [0.5, 0.9]
        if self.initial_trial_solution is None:
            x = [1] * len(C)
            for i, line in enumerate(A):
                if self.signs[i] != "=":
                    x.append(self.b[i] - sum(line) if self.signs[i] == "<=" else sum(line) - self.b[i])
                    C.append(0)
                    line.append(1 if self.signs[i] == "<=" else -1)
                    for k in range(len(A)):
                        if i != k:
                            A[k].append(0)
        else:
            x = self.initial_trial_solution
            for i, line in enumerate(A):
                if self.signs[i] != "=":
                    C.append(0)
                    line.append(1 if self.signs[i] == "<=" else -1)
                    for k in range(len(A)):
                        if i != k:
                            A[k].append(0)

        x = np.array(x, float)
        A = np.array(A, float)
        c = np.array(C, float)

        res = ""

        for alpha in alphas:
            i = 1
            while True:
                v = x
                D = np.diag(x)

                AA = np.dot(A, D)
                cc = np.dot(D, c)

                I = np.eye(len(c))

                F = np.dot(AA, np.transpose(AA))
                FI = np.linalg.inv(F)
                H = np.dot(np.transpose(AA), FI)

                P = np.subtract(I, np.dot(H, AA))

                cp = np.dot(P, cc)

                nu = np.absolute(np.min(cp))

                y = np.add(np.ones(len(c), float), (alpha / nu) * cp)

                yy = np.dot(D, y)

                x = yy

                temp = np.linalg.norm(np.subtract(x, v), ord=2)
                if temp < self.eps:
                    self.solutions_by_interior_point[alpha] = x
                    x_str = [float(format(k, ".5f")) for k in x]
                    res += f"alpha = {alpha}, iteration {i}: x = {x_str}\n"
                    break

                i += 1

                if i > 100:
                    return "The problem does not have solution!\n"

        if self.task == "max":
            for alpha, solution in self.solutions_by_interior_point.items():
                value = sum(c[i] * solution[i] for i in range(len(solution)))
                self.values_by_interior_point[alpha] = value
                res += (f"{'Maximum' if self.task == "max" else 'Minimum'} value of the "
                        f"objective function for alpha = {alpha} is {value}\n")

        return res

    def solve_by_simplex(self):
        if "=" in self.signs:
            return "Simplex method is not applicable"
        task = self.task
        c = self.C.copy()
        a = [i.copy() for i in self.A]
        b = self.b.copy()
        signs = self.signs.copy()

        if task == "max" and all(c[i] < 0 for i in range(len(c))):
            c = [-c[i] for i in range(len(c))]
            task = "min" if task == "max" else "max"

        for i, sign in enumerate(signs):
            for j in range(len(a)):
                match sign:
                    case "<=":
                        a[j] += [1 if i == j else 0]
                    case ">=":
                        a[j] += [-1 if i == j else 0]
            c += [0]

        for i, num in enumerate(b):
            if num < 0:
                b[i] = -b[i]
                a[i] = [-j for j in a[i]]
                signs[i] = "<=" if signs[i] == ">=" else ">="

        if task == "min" and any(b[i] > 0 and signs[i] == ">=" for i in range(len(b))):
            self.solved = True
            return "Simplex method is not applicable"

        neg_c: list[int] = [-i for i in c] if task == "max" else c.copy()
        enter_dict = {i: None for i in range(len(self.C))}
        while any(i < 0 for i in neg_c):
            enter_var, enter_idx = 0, -1
            for idx, i in enumerate(neg_c):
                if i < enter_var:
                    enter_var, enter_idx = i, idx

            k = 0
            while k < len(b) and (a[k][enter_idx] == 0 or a[k][enter_idx] < 0):
                k += 1
            if k == len(b):
                self.solved = True
                return "Simplex method is not applicable"
            leave_var, leave_idx = a[k][enter_idx], k
            for i in range(len(a))[k + 1:]:
                if a[i][enter_idx] != 0 and 0 <= b[i] / a[i][enter_idx] < b[leave_idx] / a[leave_idx][enter_idx]:
                    leave_var, leave_idx = a[i][enter_idx], i

            a[leave_idx] = [a[leave_idx][i] / leave_var for i in range(len(a[leave_idx]))]
            b[leave_idx] /= leave_var

            for i in range(len(a)):
                if i == leave_idx:
                    continue

                b[i] = b[i] - b[leave_idx] * a[i][enter_idx]
                a[i] = [a[i][j] - a[i][enter_idx] * a[leave_idx][j] for j in range(len(a[i]))]

            neg_c = [neg_c[i] - a[leave_idx][i] * enter_var for i in range(len(neg_c))]

            enter_dict[enter_idx] = leave_idx

        x = [0] * len(self.C)
        for i in range(len(self.C)):
            if enter_dict[i] is not None:
                x[i] = b[enter_dict[i]]

        self.value_by_simplex = sum(x[i] * self.C[i] for i in range(len(self.C)))
        self.solution_by_simplex = x

        return f"Solution by Simplex method: {x}"
