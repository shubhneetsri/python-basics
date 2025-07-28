import threading
import time

counter = 0
lock = threading.Lock()

def increment():
    global counter
    with lock:            # Solution for Race Condition @::>> Acquire the lock before modifying counter
        temp = counter
        time.sleep(0.0001)  # Small delay to encourage race
        counter = temp + 1      # This operation is now atomic
    # temp = counter
    # time.sleep(0.0001)  # Small delay to encourage race
    # counter = temp + 1

threads = [threading.Thread(target=increment) for _ in range(1000)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print(counter)  # Often less than 1000 now
