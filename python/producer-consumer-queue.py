from threading import Thread
import time
import random
from queue import Queue

queue = Queue(10)
SENTINEL = 100000

class ProducerThread(Thread):
    def run(self):
        nums = range(5)
        global queue
        for x in range(10):
            num = random.choice(nums)
            queue.put(num)
            print("Produced", num)
            time.sleep(random.random())

        queue.put(SENTINEL)
        print("SENTINEL entered queue")


class ConsumerThread(Thread):
    def run(self):
        global queue
        global SENTINEL
        while True:
            num = queue.get()
            try:
                if num is SENTINEL:
                    return
            finally:
                queue.task_done()

            print("Consumed", num)
            time.sleep(random.random())

producer = ProducerThread()
consumer = ConsumerThread()

producer.start()
consumer.start()
print("Threads started")
producer.join()
print("Producer joined")
consumer.join()
print("Consumer joined")