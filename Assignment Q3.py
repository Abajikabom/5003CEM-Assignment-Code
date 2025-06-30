import threading
import random
import time

def generate_random_numbers():
    return [random.randint(0, 10000) for _ in range(100)]

def threaded_generation(times, index):
    start = time.time_ns()
    _ = generate_random_numbers()
    end = time.time_ns()
    times[index] = (start, end)

# Multithreaded version
def multithreaded_test(rounds=10):
    total_times = []
    print("=== Multithreaded Execution ===")
    for round_num in range(1, rounds + 1):
        times = [None] * 3
        threads = []

        for i in range(3):
            t = threading.Thread(target=threaded_generation, args=(times, i))
            threads.append(t)

        for t in threads:
            t.start()
        for t in threads:
            t.join()

        start_times = [start for start, _ in times]
        end_times = [end for _, end in times]

        t1 = min(start_times)
        t2 = max(end_times)
        T = t2 - t1
        total_times.append(T)

        print(f"Round {round_num}: T = {T} ns")

    avg_time = sum(total_times) // rounds
    print(f"\nAverage Time (T) over {rounds} rounds: {avg_time} ns")
    return total_times, avg_time

# Single-threaded version
def single_threaded_test(rounds=10):
    total_times = []
    print("\n=== Single-threaded Execution ===")
    for round_num in range(1, rounds + 1):
        t1 = time.time_ns()
        generate_random_numbers()
        generate_random_numbers()
        generate_random_numbers()
        t2 = time.time_ns()
        T = t2 - t1
        total_times.append(T)
        print(f"Round {round_num}: T = {T} ns")

    avg_time = sum(total_times) // rounds
    print(f"\nAverage Time (T) over {rounds} rounds: {avg_time} ns")
    return total_times, avg_time

def show_time_difference(multi_avg, single_avg):
    diff = abs(multi_avg - single_avg)
    print(f"The difference = {diff} ns")

multi_total_times, multi_avg = multithreaded_test()
single_total_times, single_avg = single_threaded_test()

print("\n========== Summary ==========")
print(f"Multithreaded Average Time: {multi_avg} ns")
print(f"Single-threaded Average Time: {single_avg} ns")
show_time_difference(multi_avg, single_avg)

if multi_avg < single_avg:
    print("✅ Multithreaded version is faster.")
else:
    print("✅ Single-threaded version is faster.")
print("================================")
