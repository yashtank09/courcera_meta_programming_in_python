# Neasted loop

# Outer Loop
# for i in range(10):
#     # inner loop
#     for i in range(10):
#         print(0, end=" ")
#     print()

# Example using time
import time

start_time = time.time()

# outer loop
for i in range(100):
    # inner loop
    for j in range(10000):
        print(0, end=" ")
    print()

print(round(time.time() - start_time, 2))
