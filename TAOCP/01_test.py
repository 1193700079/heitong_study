import math


def factorial_stirling(n):
    return math.sqrt(2 * math.pi * n) * (n / math.e) ** n


n = 10
print(n)
exact_factorial = math.factorial(n)
approx_factorial = factorial_stirling(n)

print(f"Exact factorial of {n}: {exact_factorial}")
print(f"Approx factorial of {n} using Stirling's approximation: {approx_factorial}")
print(type(approx_factorial))
print(1/ (exact_factorial ** 9) )
print(1 / (approx_factorial ** 9))


def middle_square_method(seed, num_iterations, num_digits):
    """
    使用平方取中法生成伪随机数列

    参数:
    seed (int): 初始种子数
    num_iterations (int): 生成伪随机数的个数
    num_digits (int): 取中间位数的位数

    返回:
    list: 生成的伪随机数列表
    """
    random_numbers = []
    current_number = seed

    for _ in range(num_iterations):
        squared_number = current_number**2
        squared_str = str(squared_number).zfill(
            2 * num_digits
        )  # 确保平方后的数字长度足够长
        start_index = (len(squared_str) - num_digits) // 2
        middle_digits = squared_str[start_index : start_index + num_digits]
        current_number = int(middle_digits)
        random_numbers.append(current_number)

    return random_numbers


# 示例使用
seed = 1010101010
num_iterations = 1
num_digits = 10
random_numbers = middle_square_method(seed, num_iterations, num_digits)
print(random_numbers)
