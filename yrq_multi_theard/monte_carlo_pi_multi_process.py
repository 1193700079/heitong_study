import multiprocessing
import random
import time

"""
多进程计算蒙特卡洛
"""


def monte_carlo_pi_part(num_samples):
    count_inside_circle = 0
    for _ in range(num_samples):
        x, y = random.random(), random.random()
        if x**2 + y**2 <= 1:
            count_inside_circle += 1
    return count_inside_circle


def compute_pi(num_samples, num_processes):
    # Split the work between the processes
    samples_per_process = num_samples // num_processes
    processes = []
    pool = multiprocessing.Pool(processes=num_processes)

    # Start the processes
    results = [
        pool.apply_async(monte_carlo_pi_part, (samples_per_process,))
        for _ in range(num_processes)
    ]

    # Collect the results
    count_inside_circle = sum(result.get() for result in results)

    # Calculate the estimated value of pi
    pi_estimate = 4 * count_inside_circle / num_samples
    return pi_estimate


if __name__ == "__main__":
    num_samples = 100000000000  # Total number of samples
    num_processes = multiprocessing.cpu_count()  # Number of processes to use

    start_time = time.time()
    pi_estimate = compute_pi(num_samples, num_processes)
    end_time = time.time()

    print(f"Estimated value of Pi: {pi_estimate}")
    print(f"Time taken: {end_time - start_time} seconds")
