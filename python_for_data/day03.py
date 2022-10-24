#!/usr/bin/python
# -*- coding: UTF-8 -*-
from collections import defaultdict
import re
from functools import partial


def demo01():
    """
    zip函数
    :return:
    """
    # zip可以将多个列表、元组或其它序列成对组合成一个元组列表
    seq1 = ['foo', 'bar', 'baz']
    seq2 = ['one', 'two', 'three']
    zipped = zip(seq1, seq2)
    print(list(zipped))
    # zip可以处理任意多的序列，元素的个数取决于最短的序列：
    seq3 = [False, True]
    print(list(zip(seq1, seq2, seq3)))
    # zip的常见用法之一是同时迭代多个序列，可能结合enumerate使用：
    for i, (a, b) in enumerate(zip(seq1, seq2)):
        print('{0}: {1}, {2}'.format(i, a, b))
    # 给出一个“被压缩的”序列，zip可以被用来解压序列。也可以当作把行的列表转换为列的列表。这个方法看起来有点神奇：
    pitchers = [('Nolan', 'Ryan'), ('Roger', 'Clemens'),
                ('Schilling', 'Curt')]
    first_names, last_names = zip(*pitchers)
    print(first_names, "\n", last_names)
    return None


def demo02():
    """
    reversed函数
    :return:
    """
    # reversed可以从后向前迭代一个序列：
    # 要记住reversed是一个生成器（后面详细介绍），只有实体化（即列表或for循环）之后才能创建翻转的序列。
    print(list(reversed(range(10))))
    return None


def demo03():
    """
    字典
    :return:
    """
    # 字典可能是Python最为重要的数据结构。它更为常见的名字是哈希映射或关联数组。
    # 它是键值对的大小可变集合，键和值都是Python对象。创建字典的方法之一是使用尖括号，
    # 用冒号分隔键和值：
    d1 = {'a': 'some value', 'b': [1, 2, 3, 4]}
    print(d1)
    # 你可以像访问列表或元组中的元素一样，访问、插入或设定字典中的元素：
    d1[7] = 'an integer'
    print(d1)
    print(d1['b'])
    # 你可以用检查列表和元组是否包含某个值的方法，检查字典中是否包含某个键：
    print('b' in d1)
    # 可以用del关键字或pop方法（返回值的同时删除键）删除值：
    d1[5] = 'some value'
    print(d1)
    d1['dummy'] = 'another value'
    print(d1)
    del d1[5]
    print(d1)
    ret = d1.pop('dummy')
    print("ret:\t", ret)
    print(d1)
    # keys和values是字典的键和值的迭代器方法。
    # 虽然键值对没有顺序，这两个方法可以用相同的顺序输出键和值：
    print(list(d1.keys()))
    print(list(d1.values()))
    # 用update方法可以将一个字典与另一个融合：
    d1.update({'b': 'foo', 'c': 12})
    print(d1)
    return None


def demo04():
    """
    用序列创建字典
    :return:
    """
    # 常常，你可能想将两个序列配对组合成字典。下面是一种写法：
    # mapping = {}
    # for key, value in zip(key_list, value_list):
    #     mapping[key] = value
    # 因为字典本质上是2元元组的集合，dict可以接受2元元组的列表：
    mapping = dict(zip(range(5), reversed(range(5))))
    print(mapping)
    '''
    下面的逻辑很常见：
    if key in some_dict:
        value = some_dict[key]
    else:
        value = default_value
    '''
    # 因此，dict的方法get和pop可以取默认值进行返回，上面的if-else语句可以简写成下面：
    # get默认会返回None，如果不存在键，pop会抛出一个例外。关于设定值，
    # 常见的情况是在字典的值是属于其它集合，如列表。例如，你可以通过首字母，将一个列表中的单词分类：
    value = mapping.get(1, 1)
    print(value)
    words = ['apple', 'bat', 'bar', 'atom', 'book']
    by_letter = {}
    by_letter_2 = {}
    for word in words:
        letter = word[0]
        if letter not in by_letter.keys():
            by_letter[letter] = [word]
        else:
            by_letter[letter].append(word)
    print(by_letter)
    # setdefault方法就正是干这个的。前面的for循环可以改写为：
    for word in words:
        letter = word[0]
        by_letter_2.setdefault(letter, []).append(word)
    print(by_letter_2)
    # collections模块有一个很有用的类，defaultdict，
    # 它可以进一步简化上面。传递类型或函数以生成每个位置的默认值：
    by_letter_3 = defaultdict(list)
    for word in words:
        by_letter_3[word[0]].append(word)
    print(by_letter_3)
    return None


def demo05():
    """
    有效的键类型
    :return:
    """
    '''
    字典的值可以是任意Python对象，
    而键通常是不可变的标量类型（整数、浮点型、字符串）
    或元组（元组中的对象必须是不可变的）。这被称为“可哈希性”。
    可以用hash函数检测一个对象是否是可哈希的（可被用作字典的键）：
    '''
    ret_hash = hash('string')
    print(ret_hash)
    print(hash((1, 2, (2, 3))))
    # 要用列表当做键，一种方法是将列表转化为元组，只要内部元素可以被哈希，它也就可以被哈希：
    d = {tuple([1, 2, 3]): 5}
    print(d)
    return None


def demo06():
    """
    集合
    :return:
    """
    # 集合是无序的不可重复的元素的集合。你可以把它当做字典，
    # 但是只有键没有值。可以用两种方式创建集合：通过set函数或使用尖括号set语句：
    print(set([2, 2, 2, 1, 3, 3]))
    print({2, 2, 2, 1, 3, 3})
    # 集合支持合并、交集、差分和对称差等数学集合运算。考虑两个示例集合：
    a = {1, 2, 3, 4, 5}
    b = {3, 4, 5, 6, 7, 8}
    # 合并是取两个集合中不重复的元素。可以用union方法，或者|运算符：
    print(a.union(b))
    print(a | b)
    # 交集的元素包含在两个集合中。可以用intersection或&运算符：
    print(a.intersection(b))
    print(a & b)
    # 所有逻辑集合操作都有另外的原地实现方法，可以直接用结果替代集合的内容。对于大的集合，这么做效率更高：
    c = a.copy()
    c |= b
    print(c)
    d = a.copy()
    d &= b
    print(d)
    # 与字典类似，集合元素通常都是不可变的。要获得类似列表的元素，必须转换成元组：
    my_data = [1, 2, 3, 4]
    my_set = {tuple(my_data)}
    print(my_set)
    # 你还可以检测一个集合是否是另一个集合的子集或父集：
    a_set = {1, 2, 3, 4, 5}
    print({1, 2, 3}.issubset(a_set))
    print(a_set.issuperset({1, 2, 3}))
    print({1, 2, 3} == {3, 2, 1})
    return None


def demo07():
    """
    列表、集合和字典推导式
    :return:
    """
    # 列表推导式是Python最受喜爱的特性之一。它允许用户方便的从一个集合过滤元素，
    # 形成列表，在传递参数的过程中还可以修改元素。形式如下：
    # [expr for val in collection if condition]
    # 它等同于下面的for循环;
    # result = []
    # for val in collection:
    #     if condition:
    #         result.append(expr)
    # filter条件可以被忽略，只留下表达式就行。例如，
    # 给定一个字符串列表，我们可以过滤出长度在2及以下的字符串，并将其转换成大写：
    strings = ['a', 'as', 'bat', 'car', 'dove', 'python']
    print([x.upper() for x in strings if len(x) > 2])
    # 用相似的方法，还可以推导集合和字典。字典的推导式如下所示：
    # dict_comp = {key-expr : value-expr for value in collection if condition}
    # 集合的推导式与列表很像，只不过用的是尖括号：
    # set_comp = {expr for value in collection if condition}
    # 与列表推导式类似，集合与字典的推导也很方便，而且使代码的读写都很容易。
    # 来看前面的字符串列表。假如我们只想要字符串的长度，用集合推导式的方法非常方便：
    unique_lengths = {len(x) for x in strings}
    print(unique_lengths)
    # map函数可以进一步简化：
    print(set(map(len, strings)))
    # 作为一个字典推导式的例子，我们可以创建一个字符串的查找映射表以确定它在列表中的位置：
    loc_mapping = {val: index for index, val in enumerate(strings)}
    print(loc_mapping)
    return None


def demo08():
    """
    嵌套列表推导式
    :return:
    """
    # 假设我们有一个包含列表的列表，包含了一些英文名和西班牙名：
    all_data = [['John', 'Emily', 'Michael', 'Mary', 'Steven'],
                ['Maria', 'Juan', 'Javier', 'Natalia', 'Pilar']]
    # 你可能是从一些文件得到的这些名字，然后想按照语言进行分类。
    # 现在假设我们想用一个列表包含所有的名字，这些名字中包含两个或更多的e。可以用for循环来做：
    names_of_interest = []
    for names in all_data:
        enough_es = [name for name in names if name.count('e') >= 2]
        names_of_interest.extend(enough_es)
    print(names_of_interest)
    # 可以用嵌套列表推导式的方法，将这些写在一起，如下所示：
    result = [name for names in all_data for name in names if name.count('e') >= 2]
    print(result)
    # 嵌套列表推导式看起来有些复杂。列表推导式的for部分是根据嵌套的顺序，
    # 过滤条件还是放在最后。下面是另一个例子，我们将一个整数元组的列表扁平化成了一个整数列表：
    some_tuples = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
    flattened = [x for tup in some_tuples for x in tup]
    print(flattened)
    # 记住，for表达式的顺序是与嵌套for循环的顺序一样（而不是列表推导式的顺序）：
    flattened_02 = []
    for tup in some_tuples:
        for x in tup:
            flattened_02.append(x)
    print(flattened_02)
    # 你可以有任意多级别的嵌套，但是如果你有两三个以上的嵌套，
    # 你就应该考虑下代码可读性的问题了。分辨列表推导式的列表推导式中的语法也是很重要的：
    res = [[x for x in tup] for tup in some_tuples]
    print(res)
    return None


def my_function(x, y, z=1.5):
    """
    函数是Python中最主要也是最重要的代码组织和复用手段。
    作为最重要的原则，如果你要重复使用相同或非常类似的代码，
    就需要写一个函数。通过给函数起一个名字，还可以提高代码的可读性。
    :param x: 第一个参数 位置参数
    :param y: 第二个参数 位置参数
    :param z: 关键字参数
    :return:
    """
    if z > 1:
        return z * (x + y)
    else:
        return z / (x + y)


def demo09():
    """
    函数
    :return:
    """
    print(my_function(5, 6, z=0.7))
    print(my_function(3.14, 7, 3.5))
    print(my_function(10, 20))
    print(my_function(x=5, y=6, z=7))
    print(my_function(y=6, x=5, z=7))
    return None


def f():
    """
    返回多个值
    :return:
    """
    a = 5
    b = 6
    c = 7
    return a, b, c


def demo10():
    """

    :return:
    """
    a, b, c = f()
    print("a = {0}; b = {1}; c = {2};".format(a, b, c))
    return_value = f()
    # 在数据分析和其他科学计算应用中，你会发现自己常常这么干。
    # 该函数其实只返回了一个对象，也就是一个元组，最后该元组会被
    # 拆包到各个结果变量中。在上面的例子中，我们还可以这样写：
    print(return_value)
    return None


def demo11():
    """
    函数也是对象
    :return:
    """
    '''
    由于Python函数都是对象，因此，在其他语言中较难表达
    的一些设计思想在Python中就要简单很多了。假设我们有
    下面这样一个字符串数组，希望对其进行一些数据清理工作并执行一堆转换：
    '''
    states = ['   Alabama ', 'Georgia!', 'Georgia', 'georgia', 'FlOrIda',
              'south   carolina##', 'West virginia?']
    print(clean_strings(states))
    # 其实还有另外一种不错的办法：将需要在一组给定字符串上执行的所有运算做成一个列表：
    clean_ops = [str.strip, remove_punctuation, str.title]
    print(clean_strings_02(states, clean_ops))
    # 还可以将函数用作其他函数的参数，比如内置的map函数，它用于在一组数据上应用一个函数：
    for x in map(remove_punctuation, states):
        x = x.strip()
        print(x.title())
    return None


def remove_punctuation(value):
    return re.sub('[!#?]', '', value)


def clean_strings_02(strings, ops):
    result = []
    for value in strings:
        for function in ops:
            value = function(value)
        result.append(value)
    return result


def clean_strings(strings):
    result = []
    for value in strings:
        value = value.strip()
        value = re.sub('[!#?]', '', value)
        value = value.title()
        result.append(value)
    return result


def demo12():
    """
    匿名（lambda）函数
    :return:
    """
    '''
    Python支持一种被称为匿名的、或lambda函数。
    它仅由单条语句组成，该语句的结果就是返回值。
    它是通过lambda关键字定义的，这个关键字没有别的含义，
    仅仅是说“我们正在声明的是一个匿名函数”。
    '''
    equiv_anon = lambda x: x * 2
    print(equiv_anon)
    print(short_function(2))
    '''
    本书其余部分一般将其称为lambda函数。它们在数据分析工作中非常方便，
    因为你会发现很多数据转换函数都以函数作为参数的。直接传入lambda函数
    比编写完整函数声明要少输入很多字（也更清晰），甚至比将lambda函数赋值给
    一个变量还要少输入很多字。看看下面这个简单得有些傻的例子：
    '''
    # 虽然你可以直接编写[x *2for x in ints]，但是这里我们可以非常轻松地传入一个自定义运算给apply_to_list函数
    ints = [4, 0, 1, 5, 6]
    print(apply_to_list(ints, lambda x: x * 2))
    # 再来看另外一个例子。假设有一组字符串，你想要根据各字符串不同字母的数量对其进行排序：
    strings = ['foo', 'card', 'bar', 'aaaa', 'abab']
    strings.sort(key=lambda x: len(set(list(x))))
    print(strings)
    return None


def short_function(x):
    return x * 2


def apply_to_list(some_list, f):
    return [f(x) for x in some_list]


def demo13():
    """
    柯里化：部分参数应用
    :return:
    """
    '''
    柯里化（currying）是一个有趣的计算机科学术语，
    它指的是通过“部分参数应用”（partial argument application）
    从现有函数派生出新函数的技术。例如，假设我们有一个执行两数相加的简单函数：
    '''
    # 通过这个函数，我们可以派生出一个新的只有一个参数的函数——add_five，它用于对其参数加5：
    add_five_01 = lambda y: add_numbers(5, y)
    print(add_five_01(1))
    # add_numbers的第二个参数称为“柯里化的”（curried）。
    # 这里没什么特别花哨的东西，因为我们其实就只是定义了一个可以
    # 调用现有函数的新函数而已。内置的functools模块可以用partial函数将此过程简化：
    add_five_2 = partial(add_numbers, 5)
    print(add_five_2(2))
    return None


def add_numbers(x, y):
    return x + y


def demo14():
    """
    生成器
    :return:
    """
    '''
    能以一种一致的方式对序列进行迭代（比如列表中的对象或文件中的行）
    是Python的一个重要特点。这是通过一种叫做迭代器协议（iterator 
    protocol，它是一种使对象可迭代的通用方式）的方式实现的，一个原
    生的使对象可迭代的方法。比如说，对字典进行迭代可以得到其所有的键：
    '''
    some_dict = {'a': 1, 'b': 2, 'c': 3}
    for key in some_dict:
        print(key)
    # 当你编写for key in some_dict时，Python解释器首先会尝试从some_dict创建一个迭代器：
    dict_iterator = iter(some_dict)
    print(dict_iterator)
    # 迭代器是一种特殊对象，它可以在诸如for循环之类的上下文中向Python解释器输送对象。
    # 大部分能接受列表之类的对象的方法也都可以接受任何可迭代对象。比如min、max、sum
    # 等内置方法以及list、tuple等类型构造器：
    print(list(dict_iterator))
    # 生成器（generator）是构造新的可迭代对象的一种简单方式。
    # 一般的函数执行之后只会返回单个值，而生成器则是以延迟的
    # 方式返回一个值序列，即每返回一个值之后暂停，直到下一个值
    # 被请求时再继续。要创建一个生成器，只需将函数中的return替换为yeild即可：
    print("------------------")
    gen = squares()
    print(gen)
    for x in gen:
        print(x, end=' ')
    return None


def squares(n=10):
    print('Generating squares from 1 to {0}'.format(n ** 2))
    for i in range(1, n + 1):
        yield i ** 2


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
    # demo12()
    # demo13()
    demo14()
