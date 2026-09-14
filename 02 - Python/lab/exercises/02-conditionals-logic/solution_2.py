# Exercise 2: Conditionals and Logic - Instructions

latency = 600
throughput = 2000
health_status = True


def check_system_status(latency, throughput, health_status):
    if latency > 500 or not health_status:
        status = "CRITICAL"
    elif latency > 300 and throughput < 1000:
        status = "WARN"
    elif latency > 300:
        status = "WARN"
    else:
        status = "OK"

    return status

def print_system_metrics(latency, throughput, health_status, status):
    print(f"Latency: {latency} ms")
    print(f"Throughput: {throughput} requests/sec")
    print(f"Health Status: {'Healthy' if health_status else 'Unhealthy'}")
    print(f"System Status: {status}")

status = check_system_status(latency, throughput, health_status)
print_system_metrics(latency, throughput, health_status, status)

