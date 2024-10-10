from typing import Literal


def solve(
        c: list[int | float],
        a: list[list[int | float]],
        signs: list[Literal[">=", "<="]],
        b: list[int | float],
        eps: float = 0,
        task: Literal["min", "max"] = "max"
):
    for i, sign in enumerate(signs):
        for j in range(len(a)):
            match sign:
                case "<=":
                    a[j] += [1 if i == j else 0]
                case ">=":
                    a[j] += [-1 if i == j else 0]
        c += [0]
    neg_c: list[int] = [-i for i in c] if task == "max" else c.copy()
    enter_dict = {i: None for i in range(len(c))}
    while any(i < 0 for i in neg_c):
        enter_var, enter_idx = 0, -1
        for idx, i in enumerate(neg_c):
            if i < enter_var:
                enter_var, enter_idx = i, idx

        k = 0
        while a[k][enter_idx] <= 0:
            k += 1
        leave_var, leave_idx = a[k][enter_idx], k
        for i in range(len(a))[k + 1:]:
            if a[i][enter_idx] > 0 and b[i] / a[i][enter_idx] < b[leave_idx] / a[leave_idx][enter_idx]:
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

        print("===================================")
        print(neg_c, "\n")
        for i in a:
            print(i)
        print()
        print(b)
        print("\n")

    solution = sum(c[i] * b[enter_dict[i]] for i in range(len(c)) if enter_dict[i] is not None)
    print(solution)


solve(
    [9, 10, 16],
    [
        [18, 15, 12],
        [6, 4, 8],
        [5, 3, 3]
    ],
    ["<=", "<=", "<="],
    [360, 192, 180]
)
print("\n")
solve(
    [-2, 2, -6],
    [
        [2, 1, -2],
        [1, 2, 4],
        [1, -1, 2]
    ],
    ["<=", "<=", "<="],
    [24, 23, 10],
    task="min"
)
