#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time

import numpy as np


def demo01():
    """
    基于NumPy的算法要比纯Python快10到100倍（甚至更快），并且使用的内存更少。
    :return:
    """
    my_arr = np.arange(1000000)
    my_list = list(range(1000000))
    a = time.time_ns()
    for _ in range(10): my_arr2 = my_arr * 2
    b = time.time_ns()
    for _ in range(10): my_list2 = [x * 2 for x in my_list]
    c = time.time_ns()
    print(b - a, 'ns')
    print(c - b, 'ns')

    return None


if __name__ == "__main__":
    demo01()
