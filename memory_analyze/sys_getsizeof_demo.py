import tracemalloc


# 开始跟踪内存分配
tracemalloc.start()

# 创建一个空列表
lst = []

# 添加元素到列表中
for i in range(10000):
    lst.append(i)

# 移除元素
for i in range(10000):
    lst.pop()

# 获取当前和峰值内存使用情况
current, peak = tracemalloc.get_traced_memory()
print(f"当前内存使用：{current / 1024 / 1024:.2f} MB")
print(f"峰值内存使用：{peak / 1024 / 1024:.2f} MB")

# 停止跟踪内存分配
tracemalloc.stop()

import sys

# 查看整数的内存占用
x = 10
print(f"x 的内存占用: {sys.getsizeof(x)} bytes")

# 查看列表的内存占用
lst = []
for i in range(5):
    lst.append(i)
    print(f"lst 的内存占用: {sys.getsizeof(lst)} bytes")

# 查看字典的内存占用
d = {"a": 1, "b": 2, "c": 3}
print(f"d 的内存占用: {sys.getsizeof(d)} bytes")


import sys
from collections import deque


def get_total_size(obj, seen=None):
    """返回对象及其引用对象的内存大小（以字节为单位）"""
    size = sys.getsizeof(obj)
    if seen is None:
        seen = set()

    obj_id = id(obj)
    if obj_id in seen:
        return 0

    seen.add(obj_id)

    if isinstance(obj, dict):
        size += sum([get_total_size(v, seen) for v in obj.values()])
        size += sum([get_total_size(k, seen) for k in obj.keys()])
    elif hasattr(obj, "__dict__"):
        size += get_total_size(obj.__dict__, seen)
    elif hasattr(obj, "__iter__") and not isinstance(obj, (str, bytes, bytearray)):
        size += sum([get_total_size(i, seen) for i in obj])

    return size


# 示例使用
x = [1, 2, 3, {"a": 4, "b": 5}]
print(f"x 的总内存占用: {get_total_size(x)} bytes")
