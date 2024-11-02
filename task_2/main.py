from typing import Literal

import numpy as np


class OptimizationProblem:
    def __init__(
            self,
            C: list[int | float],
            A: list[list[int | float]],
            signs: list[Literal[">=", "<=", "="]],
            b: list[int | float],
            eps: float = 0,
            task: Literal["min", "max"] = "max"
    ):
        self.C = C
        self.A = A
        self.signs = signs
        self.b = b
        self.eps = eps
        self.task = task

        self.solved: bool = False
        self.x: list[int | float] | None = None
        self.solution: int | None = None

    def solve(self, alpha=0.5):
        x = [1] * len(self.C)
        for i, line in enumerate(self.A):
            if self.signs[i] == "<=":
                x.append(self.b[i] - sum(line))
                self.C.append(0)
                line.append(1)
            elif self.signs[i] == ">=":
                x.append(sum(line) - self.b[i])
                self.C.append(0)
                line.append(-1)

            if self.signs[i] != "=":
                for k in range(len(self.A)):
                    if i != k:
                        self.A[k].append(0)

        x = np.array(x, float)
        A = np.array(self.A, float)
        c = np.array(self.C, float)

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

            x_str = [format(k, ".2f") for k in x]
            print(f"In iteration {i} we have x = {x_str},\n")
            i += 1

            if np.linalg.norm(np.subtract(yy, v), ord=2) < self.eps:
                break
