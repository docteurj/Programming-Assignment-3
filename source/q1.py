import sys
import time
import subprocess
import os
import matplotlib.pyplot as plt

def plot_runtimes():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    test_dir = os.path.join(base_dir, 'q1-tests')
    target_script = os.path.join(base_dir, 'main.py')
    
    test_numbers = list(range(1, 16))
    runtimes = []

    print("Measuring runtimes")
    for i in test_numbers:
        test_file = os.path.join(test_dir, f"test{i}.in")
        
        if not os.path.exists(test_file):
            print(f"Warning: {test_file} not found. Defaulting to 0 seconds.")
            runtimes.append(0)
            continue
        
        start_time = time.perf_counter()
        with open(test_file, 'r') as f:
            subprocess.run([sys.executable, target_script], stdin=f, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        end_time = time.perf_counter()
        
        elapsed_time = end_time - start_time
        runtimes.append(elapsed_time)
        print(f"Test {i}: {elapsed_time:.5f} seconds")

    plt.figure(figsize=(10, 6))
    plt.plot(test_numbers, runtimes, marker='o', linestyle='-', color='b')
    plt.title('Runtime of main.py Across 15 Test Files')
    plt.xlabel('Test File Number (test#.in)')
    plt.ylabel('Execution Time (seconds)')
    plt.xticks(test_numbers)
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    plot_runtimes()