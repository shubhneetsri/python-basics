import multiprocessing
import time

def sum_of_squares(n):
    return sum(i*i for i in range(n))

if __name__ == "__main__":
    numbers = [10_000_000, 15_000_000, 20_000_000, 25_000_000]

    start_time = time.time()

    # Create a pool of processes
    with multiprocessing.Pool(processes=4) as pool:
        results = pool.map(sum_of_squares, numbers)

    end_time = time.time()

    print("Results:", results)
    print("Time taken:", end_time - start_time)
