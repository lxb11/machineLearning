#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time

import numpy as np


# NumPy的ndarray：一种多维数组对象
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


def demo02():
    """
    NumPy的ndarray：一种多维数组对象
    :return:
    """
    data = np.random.randn(2, 3)
    print(data)
    print(data * 10)
    print(data + data)
    print(data.shape)
    print(data.dtype)
    return None


def demo03():
    """
    创建ndarray
    :return:
    """
    # 创建数组最简单的办法就是使用array函数。它接受一切序列型的对象（包括其他数组），
    # 然后产生一个新的含有传入数据的NumPy数组。以一个列表的转换为例
    data1 = [6, 7.5, 8, 0, 1]
    arr1 = np.array(data1)
    print(arr1)
    # 嵌套序列（比如由一组等长列表组成的列表）将会被转换为一个多维数组
    data2 = [[1, 2, 3, 4], [5, 6, 7, 8]]
    arr2 = np.array(data2)
    print(arr2)
    # 因为data2是列表的列表，NumPy数组arr2的两个维度的shape
    # 是从data2引入的。可以用属性ndim和shape验证
    print(arr2.ndim)
    print(arr2.shape)
    # 除非特别说明（稍后将会详细介绍），np.array会
    # 尝试为新建的这个数组推断出一个较为合适的数据类型。
    # 数据类型保存在一个特殊的dtype对象中。比如说，在上面的两个例子中，我们有
    print(arr1.dtype)
    print(arr2.dtype)
    # 除np.array之外，还有一些函数也可以新建数组。
    # 比如，zeros和ones分别可以创建指定长度或形状的全0或全1数组。
    # empty可以创建一个没有任何具体值的数组。要用这些方法创建多维数组，
    # 只需传入一个表示形状的元组即可
    print(np.zeros(10))
    print(np.zeros((3, 6)))
    # 注意：认为np.empty会返回全0数组的想法是不安全的。
    # 很多情况下（如前所示），它返回的都是一些未初始化的垃圾值。
    print(np.empty((2, 3, 2)))
    # 注意：认为np.empty会返回全0数组的想法是不安全的。
    # 很多情况下（如前所示），它返回的都是一些未初始化的垃圾值。
    print(np.arange(15))
    return None


def demo04():
    """
    ndarray的数据类型
    :return:
    """
    # dtype（数据类型）是一个特殊的对象，它含有ndarray将一块内存解释为特定数据类型所需的信息
    arr1 = np.array([1, 2, 3], dtype=np.float64)
    arr2 = np.array([1, 2, 3], dtype=np.int32)
    print(arr1.dtype)
    print(arr2.dtype)
    '''
    dtype是NumPy灵活交互其它系统的源泉之一。
    多数情况下，它们直接映射到相应的机器表示，
    这使得“读写磁盘上的二进制数据流”以及“集成低级语言代码
    （如C、Fortran）”等工作变得更加简单。数值型dtype的命名方式相同：
    一个类型名（如float或int），后面跟一个用于表示各元素位长的数字。
    标准的双精度浮点值（即Python中的float对象）需要占用8字节（即64位）。
    因此，该类型在NumPy中就记作float64。表4-2列出了NumPy所支持的全部数据类型。
    '''
    '''
    笔记：记不住这些NumPy的dtype也没关系，新手更是如此。
    通常只需要知道你所处理的数据的大致类型是浮点数、复数、整数、布尔值、字符串，
    还是普通的Python对象即可。当你需要控制数据在内存和磁盘中的存储方式时（尤其是对大数据集），
    那就得了解如何控制存储类型。
    '''
    # 你可以通过ndarray的astype方法明确地将一个数组从一个dtype转换成另一个dtype
    arr = np.array([1, 2, 3, 4, 5])
    print(arr.dtype)
    float_arr = arr.astype(np.float64)
    print(float_arr.dtype)
    # 在本例中，整数被转换成了浮点数。如果将浮点数转换成整数，则小数部分将会被截取删除
    arr3 = np.array([3.7, -1.2, -2.6, 0.5, 12.9, 10.1])
    print(arr3.dtype)
    print(arr3.astype(np.int32))
    # 如果某字符串数组表示的全是数字，也可以用astype将其转换为数值形式
    numeric_strings = np.array(['1.25', '-9.6', '42'], dtype=np.string_)
    print(numeric_strings.astype(float))
    # 注意：使用numpy.string_类型时，一定要小心，
    # 因为NumPy的字符串数据是大小固定的，发生截取时，
    # 不会发出警告。pandas提供了更多非数值数据的便利的处理方法。
    # 如果转换过程因为某种原因而失败了（比如某个不能被转换为float64的字符串），
    # 就会引发一个ValueError。这里，我比较懒，写的是float而不是np.float64；
    # NumPy很聪明，它会将Python类型映射到等价的dtype上

    # 数组的dtype还有另一个属性
    int_array = np.arange(10)
    calibers = np.array([.22, .270, .357, .380, .44, .50], dtype=np.float64)
    print(int_array.astype(calibers.dtype))
    # 你还可以用简洁的类型代码来表示dtype
    empty_uint32 = np.empty(8, dtype='u4')
    print(empty_uint32)
    return None


def demo05():
    """
    NumPy数组的运算
    :return:
    """
    '''
    数组很重要，因为它使你不用编写循环即可对数据执行批量运算。
    NumPy用户称其为矢量化（vectorization）。大小相等的数组
    之间的任何算术运算都会将运算应用到元素级：
    '''
    arr = np.array([[1., 2., 3.], [4., 5., 6.]])
    print(arr)
    print(arr * arr)
    print(arr - arr)
    # 数组与标量的算术运算会将标量值传播到各个元素
    print(1 / arr)
    print(arr ** 0.5)
    # 大小相同的数组之间的比较会生成布尔值数组
    arr2 = np.array([[0., 4., 1.], [7., 2., 12.]])
    print(arr2)
    print(arr2 > arr)
    return None


def demo06():
    """
    基本的索引和切片
    :return:
    """
    # NumPy数组的索引是一个内容丰富的主题，
    # 因为选取数据子集或单个元素的方式有很多。
    # 一维数组很简单。从表面上看，它们跟Python列表的功能差不多
    arr = np.arange(10)
    print(arr)
    print(arr[5])
    print(arr[5:8])
    arr[5:8] = 12
    print(arr)
    '''
    如上所示，当你将一个标量值赋值给一个切片时（如arr[5:8]=12），
    该值会自动传播（也就说后面将会讲到的“广播”）到整个选区。
    跟列表最重要的区别在于，数组切片是原始数组的视图。这意味着数据不会被复制，
    视图上的任何修改都会直接反映到源数组上。
    
    作为例子，先创建一个arr的切片：
    '''
    arr_slice = arr[5:8]
    print(arr_slice)
    # 现在，当我修改arr_slice中的值，变动也会体现在原始数组arr中：
    arr_slice[1] = 12345
    print(arr)
    # 切片[ : ]会给数组中的所有值赋值
    arr_slice[:] = 64
    print(arr)
    '''
    如果你刚开始接触NumPy，可能会对此感到惊讶（尤其是当你曾经用过其他热衷于复制数组数据的编程语言）。
    由于NumPy的设计目的是处理大数据，所以你可以想象一下，假如NumPy坚持要将数据复制来复制去的话会产生何等的性能和内存问题。
    注意：如果你想要得到的是ndarray切片的一份副本而非视图，就需要明确地进行复制操作，例如arr[5:8].copy()。
    对于高维度数组，能做的事情更多。在一个二维数组中，各索引位置上的元素不再是标量而是一维数组：
    '''
    arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(arr2d[2])
    # 因此，可以对各个元素进行递归访问，但这样需要做的事情有点多。
    # 你可以传入一个以逗号隔开的索引列表来选取单个元素。也就是说，
    # 下面两种方式是等价的：
    print(arr2d[0][2])
    print(arr2d[0, 2])
    # 在多维数组中，如果省略了后面的索引，则返回对象会是一个维度低一点的ndarray
    # （它含有高一级维度上的所有数据）。因此，在2×2×3数组arr3d中：
    arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
    print(arr3d)
    # arr3d[0]是一个2×3数组：
    print(arr3d[0])
    # 标量值和数组都可以被赋值给arr3d[0]
    old_values = arr3d[0].copy()
    arr3d[0] = 42
    print(arr3d)
    arr3d[0] = old_values
    print(arr3d)
    # 相似的，arr3d[1,0]可以访问索引以(1,0)开头的那些值（以一维数组的形式返回）:
    print(arr3d[1, 0])
    # 虽然是用两步进行索引的，表达式是相同的：
    x = arr3d[1]
    print(x)
    print(x[0])
    return None


if __name__ == "__main__":
    # demo01()
    # demo02()
    # demo03()
    # demo04()
    # demo05()
    demo06()