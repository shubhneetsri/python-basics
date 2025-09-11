import queue
import threading
import time

# Create a thread-safe queue
msg_queue = queue.Queue()

# Producer
def producer():
    for i in range(5):
        msg_queue.put(f"message-{i}")
        print(f"Produced: message-{i}")
        time.sleep(1)

# Consumer
def consumer():
    while True:
        msg = msg_queue.get()   # blocks until message is available
        print(f"Consumed: {msg}")
        msg_queue.task_done()

t1 = threading.Thread(target=producer)
t2 = threading.Thread(target=consumer, daemon=True)

t1.start()
t2.start()

t1.join()
msg_queue.join()   # wait until all messages processed
