# Exercise 3: Loops and Aggregations - Instructions

#step 2
def print_1_to_10():
    for i in range(1, 11):
        print(i)

print_1_to_10()

#step 3
def sum_1_to_10():
    total = 0
    for i in range(1, 11):
        total += i
    return total

print(sum_1_to_10())


#step 4
response_times = [120, 340, 95, 610, 450, 280, 190]

def calculate_response_time(response_times_list):
    length = len(response_times_list)
    sum_response_times = sum(response_times_list)
    average = sum_response_times / length if length > 0 else 0
    return length, sum_response_times, average

def print_response_time_stats(length, sum_response_times, average):
    print(f"Number of response times: {length}")
    print(f"Sum of response times: {sum_response_times}")
    print(f"Average response time: {average:.2f}")

length, sum_response_times, average = calculate_response_time(response_times)
print_response_time_stats(length, sum_response_times, average)

#step 5 and step 6
def slow_response_times(response_times_list):
    count = 0
    for response_time in response_times_list:
        if response_time > 300:
            count += 1
            print(f"Slow response time {count}: {response_time} ms")
    print(f"Total number of slow response times: {count}")

slow_response_times(response_times)

#step 7
def countdown_blastoff():
    number = 5
    while number > 0:
        print(f"Countdown: {number}")
        number -= 1
    print("Blastoff!")

countdown_blastoff()