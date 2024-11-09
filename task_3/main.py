from math import inf
import pprint

import numpy as np


class TransportationProblem:
    def __init__(
        self,
        s: list[int | float],
        c: list[list[int | float]],
        d: list[int: float],
    ):
        self.s = s
        self.c = c
        self.d = d

        self.balanced: bool = sum(s) == sum(d)

        self.solved_by_north_west: bool = False
        self.solution_by_north_west: list[list[int | float]] | None = None

        self.solved_by_vogel: bool = False
        self.solution_by_vogel: list[list[int | float]] | None = None

        self.solved_by_russell: bool = False
        self.solution_by_russell: list[list[int | float]] | None = None

    def _solve_by_north_west(self):
        if self.solved_by_north_west:
            return self.solution_by_north_west

        s = self.s.copy()
        d = self.d.copy()
        c = [line.copy() for line in self.c]
        res = [[0] * len(c[0]) for _ in range(len(c))]

        i, j = 0, 0
        while not (sum(s) == sum(d) == 0):
            if s[i] == 0:
                i += 1
                continue
            if d[j] == 0:
                j += 1
                continue

            res[i][j] = min(s[i], d[j])
            s[i] -= res[i][j]
            d[j] -= res[i][j]

        self.solution_by_north_west = res
        self.solved_by_north_west = True
        return res

    def _solve_by_vogel(self):
        if self.solved_by_vogel:
            return self.solution_by_vogel

        s = self.s.copy()
        d = self.d.copy()
        c = [line.copy() for line in self.c]
        res = [[0] * len(c[0]) for _ in range(len(c))]

        while not (sum(s) == sum(d) == 0):
            diffs_by_rows = []
            for i, row in enumerate(c):
                if s[i] == 0:
                    diffs_by_rows.append(-inf)
                else:
                    sorted_row = sorted([num for num in row if num is not None])
                    diffs_by_rows.append(sorted_row[1] - sorted_row[0] if len(sorted_row) > 1 else 0)

            diffs_by_columns = []
            for j in range(len(c[0])):
                if d[j] == 0:
                    diffs_by_columns.append(-inf)
                else:
                    sorted_column = sorted([row[j] for row in c if row[j] is not None])
                    diffs_by_columns.append(sorted_column[1] - sorted_column[0] if len(sorted_column) > 1 else 0)

            max_diff_by_rows = max(diffs_by_rows)
            max_diff_by_columns = max(diffs_by_columns)
            if max_diff_by_rows >= max_diff_by_columns:
                i = diffs_by_rows.index(max_diff_by_rows)
                j = c[i].index(min(num for num in c[i] if num is not None))
            else:
                j = diffs_by_columns.index(max_diff_by_columns)
                column = [row[j] for row in c]
                i = column.index(min(num for num in column if num is not None))
            res[i][j] = min(s[i], d[j])
            s[i] -= res[i][j]
            d[j] -= res[i][j]
            if s[i] == 0:
                c[i] = [None] * len(c[i])
            if d[j] == 0:
                for i in range(len(c)):
                    c[i][j] = None

        self.solution_by_vogel = res
        self.solved_by_vogel = True
        return res

    def _solve_by_russell(self):
        if self.solved_by_russell:
            return self.solution_by_russell

        s = self.s.copy()
        d = self.d.copy()
        c = [line.copy() for line in self.c]
        res = [[0] * len(c[0]) for _ in range(len(c))]

        row_max_list = [max([num for num in row if num is not None] or 0) for row in c]
        columns = [[c[i][j] for i in range(len(c))] for j in range(len(c[0]))]
        column_max_list = [max([num for num in column if num is not None] or 0) for column in columns]

        diffs = []
        for i in range(len(c)):
            for j, num in enumerate(c[i]):
                cur_diff = num - row_max_list[i] - column_max_list[j]
                diffs.append((cur_diff, i, j))

        diffs.sort(key=lambda x: x[0])

        while not (sum(s) == sum(d) == 0):
            _, i, j = diffs.pop()
            if c[i][j] is None:
                continue
            res[i][j] = min(s[i], d[j])
            s[i] -= res[i][j]
            d[j] -= res[i][j]
            if s[i] == 0:
                c[i] = [None] * len(c[i])
            if d[j] == 0:
                for i in range(len(c)):
                    c[i][j] = None

        self.solution_by_russell = res
        self.solved_by_russell = True
        return res

    def solve(self):
        if not self.balanced:
            print("The problem is not balanced!")
            return
        self._solve_by_north_west()
        self._solve_by_vogel()
        self._solve_by_russell()

        result_matrix = []
        for i, row in enumerate(self.c):
            result_matrix.append(row + [str("|") + str(self.s[i])])
        result_matrix.append(["_"] * len(self.c[0]))
        result_matrix.append(self.d)

        print("The problem matrix:")
        pprint.pprint(result_matrix)

        print("The North-West method:", self.solution_by_north_west)
        print("The Vogel method:", self.solution_by_vogel)        
        print("The Russell method:", self.solution_by_russell)
        print()
