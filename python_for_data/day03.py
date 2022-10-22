#!/usr/bin/python
# -*- coding: UTF-8 -*-
from collections import defaultdict


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


if __name__ == "__main__":
    # demo01()
    # demo02()
    # demo03()
    demo04()
