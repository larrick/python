# coding: utf-8
def biSearch(ary, target):
    high = len(ary)
    low = -1

    while high - low > 1:
        probe = (high + low) / 2
        if ary[probe] > target:
            high = probe
        else:
            low = probe

    if low == -1 or ary[low] != target:
        return -1
    else:
        return low
