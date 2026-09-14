# step 2

events = [
    {"id": 1, "status": "ok", "latency_ms": 120},
    {"id": 2, "status": "error", "latency_ms": 900},
    {"id": 3, "status": "ok", "latency_ms": 450},
    {"id": 4, "status": "ok", "latency_ms": 200},
    {"id": 5, "status": "error", "latency_ms": 1100},
]

# step 3

def count_errors(events):
    return sum(1 for event in events if event["status"] == "error")

count_of_errors = count_errors(events)
print(f"Count of error events: {count_of_errors}")

#step 4 and step 5
def average_latency(events):
    total_latency = sum(event["latency_ms"] for event in events)
    return total_latency / len(events) if events else 0

avg_latency = average_latency(events)
print(f"Average latency: {avg_latency:.2f} ms")

# step 6 and step 7
def get_slow_events(events, threshold=500):
    return [event for event in events if event["latency_ms"] > threshold]

def print_slow_events(slow_events):
    for event in slow_events:
        print(f"Slow event ID: {event['id']}, Latency: {event['latency_ms']} ms")

slow_events = get_slow_events(events)
print(f"Number of slow events: {len(slow_events)}")
print_slow_events(slow_events)
