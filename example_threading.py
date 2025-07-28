import threading
import time

def print_numbers(name,n):
    for i in range(n):
        print(f"Thread {name} count number: {i}")
        time.sleep(0.5)

thread1 = threading.Thread(target=print_numbers, args=('thread1', 5))
thread2 = threading.Thread(target=print_numbers, args=('thread2', 5))

thread1.start()
thread2.start()


thread1.join()
thread2.join()

print("Finished printing from both threads.")