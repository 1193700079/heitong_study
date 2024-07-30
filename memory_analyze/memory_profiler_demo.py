from memory_profiler import profile


@profile
def my_function():
    a = [i for i in range(10000)]
    b = [i**2 for i in range(10000)]
    return a, b


if __name__ == "__main__":
    while True:
        my_function()


"""
python -m memory_profiler test2.py
"""
