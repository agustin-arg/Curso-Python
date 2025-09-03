import multiprocessing
import random
def parallel_sum(numbers: list):
    result = 0
    for num in numbers:
        result += num
    return result

if __name__ == '__main__':
    big_numbers = [random.randint(1, 9) for _ in range(100000)]
    mitad = len(big_numbers) // 2
    
    with multiprocessing.Pool(2) as pool:
        results = pool.map(parallel_sum, [big_numbers[:mitad], big_numbers[mitad:]])
        result = results[0] + results[1]
    print(result)