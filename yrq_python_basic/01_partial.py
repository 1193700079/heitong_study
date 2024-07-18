from functools import partial


# 假设你有一个函数，它接受三个参数
def my_function(a, b, c):
    return a + b + c


# 现在，你想要创建一个新的函数，它总是将第一个参数设置为某个值，
# 例如10，而保持其他参数不变
new_function = partial(my_function, 10)

# 使用新的函数
result = new_function(20, 30)
print(result)  # 输出：60
