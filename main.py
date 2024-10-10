from typing import Literal


def solve(
        c: list[int | float],
        a: list[list[int | float]],
        signs: list[Literal[">=", "<="]],
        b: list[int | float],
        eps: float = 0,
        task: Literal["min", "max"] = "max"
) -> str:
    problem = f"- {task} z = "
    for i, coefficient in enumerate(c):
        problem += f"{coefficient} * x{i + 1} + "
    problem = problem[:-3] + "\n"
    problem += "- subject to the constraints:\n"
    for i, row in enumerate(a):
        problem += f"\t- {row} * x {signs[i]} {b[i]}\n"
    problem = problem[:-1]
    print(problem)

    orig_c = c.copy()
    orig_task = task

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
        return "- solver_state: unbounded"

    neg_c: list[int] = [-i for i in c] if task == "max" else c.copy()
    enter_dict = {i: None for i in range(len(orig_c))}
    while any(i < 0 for i in neg_c):
        enter_var, enter_idx = 0, -1
        for idx, i in enumerate(neg_c):
            if i < enter_var:
                enter_var, enter_idx = i, idx

        k = 0
        while k < len(b) and (a[k][enter_idx] == 0 or a[k][enter_idx] < 0):
            k += 1
        if k == len(b):
            return "- solver_state: unbounded"
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

    x = [0] * len(orig_c)
    for i in range(len(orig_c)):
        if enter_dict[i] is not None:
            x[i] = b[enter_dict[i]]
    solution = sum(x[i] * orig_c[i] for i in range(len(orig_c)))

    return (
        f"- solver_state: solved\n"
        f"- x*: {x}\n"
        f"- z: {solution}"
    )
