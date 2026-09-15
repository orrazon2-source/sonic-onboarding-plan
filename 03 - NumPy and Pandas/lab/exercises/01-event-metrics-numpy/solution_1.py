import numpy as np

from exercise_01_sample_data import generate_latencies

latencies = generate_latencies(1000)

print("First 10 latencies:")
print(latencies[:10])
print(f"\nTotal events: {len(latencies)}")
print(f"Data type: {latencies.dtype}")


# Step 2: Explore the Array
print(f"Shape: {latencies.shape}")
print(f"Size: {latencies.size}")
print(f"Data type: {latencies.dtype}")
print(f"Min value: {latencies.min()}")
print(f"Max value: {latencies.max()}")


# Step 3: Calculate Central Tendency
print("Mean latency: {:.2f}".format(latencies.mean()))
print("Median latency: {:.2f}".format(np.median(latencies)))
print("Standard deviation: {:.2f}".format(latencies.std()))


# Step 4: Calculate Percentiles
print("50th percentile (median): {:.2f}".format(np.percentile(latencies, 50)))
print("95th percentile: {:.2f}".format(np.percentile(latencies, 95)))
print("99th percentile: {:.2f}".format(np.percentile(latencies, 99)))


# Step 5: Find Slow Events
slow_500 = latencies[latencies > 500]
slow_1000 = latencies[latencies > 1000]

print(f"Events slower than 500 ms: {len(slow_500)}")
print(f"Events slower than 1000 ms: {len(slow_1000)}")


# Step 6: Categorize All Events
categorized_events = np.select(
    [latencies <= 200, latencies <= 500, latencies <= 1000],
    ["Fast", "Normal", "Slow"],
    default="Very Slow"
)

print("\nEvent categories:")
print(f"Fast events: {np.sum(categorized_events == 'Fast')}")
print(f"Normal events: {np.sum(categorized_events == 'Normal')}")
print(f"Slow events: {np.sum(categorized_events == 'Slow')}")
print(f"Very Slow events: {np.sum(categorized_events == 'Very Slow')}")


# Step 7: Calculate Z-Scores 
z_scores = (latencies - latencies.mean()) / latencies.std()
z_scores_above_2 = z_scores[z_scores > 2]
print(f"latencies with z-score above 2: {z_scores_above_2}")


# Step 9: NumPy vs Python Loops
import timeit

def python_mean():
    total = 0
    for value in latencies:
        total += value
    return total / len(latencies)

def numpy_mean():
    return latencies.mean()

python_time = min(timeit.repeat(python_mean, repeat=5, number=10_000))
numpy_time = min(timeit.repeat(numpy_mean, repeat=5, number=10_000))

print(f"Python loop mean: {python_mean():.2f}")
print(f"NumPy mean: {numpy_mean():.2f}")
print(f"Python loop time: {python_time:.6f}s")
print(f"NumPy time: {numpy_time:.6f}s")