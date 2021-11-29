import doctest

EPS = 0.01


def payments(values: list[float], choice_role) -> list[float]:
    """
    To demonstrate a variety of algo i made that the function gets both value and weight of each candidate

    :param values:
    :param choice_role:
    :return:
    >>> l = [(100, 100), (20, 2), (20, 2)]
    >>> l2 = [(100, 100), (50, 2), (60, 2)]
    >>> print(payments(l,lambda x: greedy(x, 100, lambda y: y[0])[0]))
    [20.00999999998608, 0, 0]
    >>> print(payments(l, lambda x: greedy_a_b(x, 100)[0]))
    [40.00999999998636, 0, 0]
    >>> print(payments(l2, lambda x: greedy_a_b(x, 100)[0]))
    [0, 40.00000000000199, 50.00000000000199]
    >>> l = [ (20, 2),(100, 100), (20, 2),(20, 2),(20, 2),(20, 2),(20, 2),(20, 2),(20, 2),(20, 2)]
    >>> print(payments(l,lambda x: greedy(x, 100, lambda y: y[0])[0]))
    [0, 20.00999999998608, 0, 0, 0, 0, 0, 0, 0, 0]
    >>> print(payments(l, lambda x: greedy(x, 100, lambda y: y[0]/y[1])[0]))
    [2.0099999999996747, 0, 2.0099999999996747, 2.0099999999996747, 2.0099999999996747, 2.0099999999996747, 2.0099999999996747, 2.0099999999996747, 2.0099999999996747, 2.0099999999996747]
    >>> print(payments(l, lambda x: greedy_a_b(x, 100)[0]))
    [2.0099999999996747, 0, 2.0099999999996747, 2.0099999999996747, 2.0099999999996747, 2.0099999999996747, 2.0099999999996747, 2.0099999999996747, 2.0099999999996747, 2.0099999999996747]
    >>> print(payments(l2, lambda x: greedy(x, 100, lambda y: y[0]/y[1])[0]))
    [0, 2.0000000000013785, 2.000000000003368]
    >>> l = [ (50,70),(8,1),(8,1),(50,30),(8,1),(8,1),(8,1),(8,1),(8,1),(8,1),(8,1),(8,1),(8,1)]
    >>> print(payments(l, lambda x: greedy(x, 100, lambda y: y[0])[0]))
    [8.00000000000125, 0, 0, 8.00000000000125, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    >>> print(payments(l, lambda x: greedy_a_b(x, 100)[0]))
    [0, 0.7200000000001268, 0.7200000000001268, 21.43000000000193, 0.7200000000001268, 0.7200000000001268, 0.7200000000001268, 0.7200000000001268, 0.7200000000001268, 0.7200000000001268, 0.7200000000001268, 0.7200000000001268, 0.7200000000001268]
    >>> print(payments(l, lambda x: greedy(x, 100, lambda y: y[0]/y[1])[0]))
    [0, 0.7200000000001268, 0.7200000000001268, 21.43000000000193, 0.7200000000001268, 0.7200000000001268, 0.7200000000001268, 0.7200000000001268, 0.7200000000001268, 0.7200000000001268, 0.7200000000001268, 0.7200000000001268, 0.7200000000001268]

    """
    chosen = choice_role(values)
    ans = []

    val_choose = list(zip(values, chosen))
    for i in range(len(chosen)):
        t_val = list(map(lambda x: [x[0], x[1]], values))
        t_val[i][0] -= EPS
        v, c = val_choose[i]
        if c:
            while choice_role(t_val)[i]:
                t_val[i][0] -= EPS
            ans.append(t_val[i][0] + EPS)
        else:
            ans.append(0)
    return ans


def greedy(val_w: list[tuple], max_w: float, key):
    copy_val_w = val_w.copy()
    sort_val_w = sorted(val_w, key=key, reverse=True)
    sum = 0
    w_sum = 0
    ans = [False] * len(val_w)
    for i in sort_val_w:
        index = copy_val_w.index(i)
        copy_val_w[index] = "-"
        w_sum += i[1]
        if w_sum <= max_w:
            sum += i[0]
            ans[index] = True
        else:
            return ans, sum
    return ans, sum


def greedy_a_b(val_w: list[tuple], max_w: float):
    res_a = greedy(val_w, max_w, lambda x: x[0])
    res_b = greedy(val_w, max_w, lambda x: x[0] / x[1])
    return res_a if res_a[1] > res_b[1] else res_b


if __name__ == '__main__':
    (failures, tests) = doctest.testmod(report=True)
    print("{} failures, {} tests".format(failures, tests))
