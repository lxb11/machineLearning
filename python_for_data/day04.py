#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time

import numpy as np
import matplotlib.pyplot as plt


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


def demo07():
    """
    布尔型索引
    :return:
    """
    # 来看这样一个例子，
    # 假设我们有一个用于存储数据的数组以及一个存储姓名的数组（含有重复项）。在这里，
    # 我将使用numpy.random中的randn函数生成一些正态分布的随机数据：
    names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
    data = np.random.randn(7, 4)
    print(names)
    print(data)
    # 假设每个名字都对应data数组中的一行，而我们想要选出对应于名字"Bob"的所有行。
    # 跟算术运算一样，数组的比较运算（如==）也是矢量化的。
    # 因此，对names和字符串"Bob"的比较运算将会产生一个布尔型数组：
    print(names == 'Bob')
    # 这个布尔型数组可用于数组索引：
    print(data[names == 'Bob'])
    # 下面的例子，我选取了names == 'Bob'的行，并索引了列：
    print(data[names == 'Bob', 2:])
    print(data[names == 'Bob', 3])
    # 要选择除"Bob"以外的其他值，既可以使用不等于符号（!=），也可以通过~对条件进行否定：
    print(data[~(names == 'Bob')])
    # 通过布尔型数组设置值是一种经常用到的手段。为了将data中的所有负值都设置为0，我们只需：
    data[data < 0] = 0
    print(data)
    # 通过一维布尔数组设置整行或列的值也很简单：
    data[names != 'Joe'] = 7
    print(data)
    return None


def demo08():
    """
    花式索引
    :return:
    """
    arr = np.empty((8, 4))
    for i in range(8):
        arr[i] = i
    print(arr)
    # 为了以特定顺序选取行子集，只需传入一个用于指定顺序的整数列表或ndarray即可：
    print(arr[[4, 3, 0, 6]])
    # 这段代码确实达到我们的要求了！使用负数索引将会从末尾开始选取行：
    print(arr[[-3, -5, -7]])
    # 一次传入多个索引数组会有一点特别。它返回的是一个一维数组，其中的元素对应各个索引元组：
    arr = np.arange(32).reshape((8, 4))
    print(arr)
    # 最终选出的是元素(1,0)、(5,3)、(7,1)和(2,2)。无论数组是多少维的，花式索引总是一维的。
    # 记住，花式索引跟切片不一样，它总是将数据复制到新数组中。
    print(arr[[1, 5, 7, 2], [0, 3, 1, 2]])
    return None


def demo09():
    """
    数组转置和轴对换
    :return:
    """
    # 转置是重塑的一种特殊形式，它返回的是源数据的视图（不会进行任何复制操作）。
    # 数组不仅有transpose方法，还有一个特殊的T属性：
    arr = np.arange(15).reshape((3, 5))
    print(arr)
    print(arr.T)
    # 在进行矩阵计算时，经常需要用到该操作，比如利用np.dot计算矩阵内积：
    arr1 = np.random.randn(6, 3)
    print(arr1)
    print(np.dot(arr1.T, arr1))
    return None


def demo10():
    """
    利用数组进行数据处理
    :return:
    """
    # 作为简单的例子，假设我们想要在一组值（网格型）上计算函数sqrt(x^2+y^2)。
    # np.meshgrid函数接受两个一维数组，并产生两个二维矩阵（对应于两个数组中所有的(x,y)对）：
    points = np.arange(-5, 5, 0.01)  # 1000 equally spaced points
    print(points)
    xs, ys = np.meshgrid(points, points)
    print(ys)
    # 现在，对该函数的求值运算就好办了，把这两个数组当做两个浮点数那样编写表达式即可：
    z = np.sqrt(xs ** 2 + ys ** 2)
    print(z)
    # 作为第9章的先导，我用matplotlib创建了这个二维数组的可视化：
    plt.imshow(z, cmap=plt.cm.gray)
    plt.colorbar()
    plt.title("Image plot of $\sqrt{x^2 + y^2}$ for a grid of values")
    plt.show()
    return None


def demo11():
    """
    数学和统计方法
    :return:
    """
    arr = np.random.randn(5, 4)
    print(arr)
    print(arr.mean())
    print(np.mean(arr))
    print(arr.sum())
    # mean和sum这类的函数可以接受一个axis选项参数，用于计算该轴向上的统计值，
    # 最终结果是一个少一维的数组：
    # 这里，arr.mean(1)是“计算行的平均值”，arr.sum(0)是“计算每列的和”。
    print(arr.mean(axis=1))
    print(arr.sum(axis=0))
    # 其他如cumsum和cumprod之类的方法则不聚合，而是产生一个由中间结果组成的数组：
    arr1 = np.array([0, 1, 2, 3, 4, 5, 6, 7])
    print(arr1.cumsum())
    # 在多维数组中，累加函数（如cumsum）返回的是同样大小的数组，
    # 但是会根据每个低维的切片沿着标记轴计算部分聚类：
    arr2 = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
    print(arr2)
    print(arr2.cumsum(axis=0))
    print(arr2.cumprod(axis=1))
    return None


def demo12():
    """
    示例：随机漫步
    :return:
    """
    nsteps = 1000
    draws = np.random.randint(0, 2, size=nsteps)
    steps = np.where(draws > 0, 1, -1)
    walk = steps.cumsum()
    print(walk.min())
    print(walk.max())
    print(walk)
    print((np.abs(walk) >= 10).argmax())
    return None


if __name__ == "__main__":
    # demo01()
    # demo02()
    # demo03()
    # demo04()
    # demo05()
    # demo06()
    # demo07()
    # demo08()
    # demo09()
    # demo10()
    # demo11()
    demo12()
