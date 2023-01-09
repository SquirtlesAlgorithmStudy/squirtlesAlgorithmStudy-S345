import time
a = [0] * 100000000
current_time = time.time()
a[2:999999] = [1] * 999997
processing_time = time.time() - current_time
print(processing_time)


a = [0] * 100000000
current_time = time.time()
for i in range(999997):
    a[2 + i] = 1
processing_time = time.time() - current_time
print(processing_time)
