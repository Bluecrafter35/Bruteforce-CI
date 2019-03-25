import threading
import queue
import time
import itertools


class PwdConsumer(threading.Thread):

    def init(self, queue, condition):
        threading.Thread.__init__(self)
        self.queue = queue
        self.condition = condition

    def run(self):
        password = None
        while True:
            self.condition.acquire()
            try:
                password = self.queue.get(block=False)
                self.condition.notify()
            except queue.Empty:
                self.condition.wait()
            self.condition.release()

            your_list = 'abc'
            complete_list = []
            for current in range(5):
                a = [i for i in your_list]
                for y in range(current):
                    a = [x + i for i in your_list for x in a]
                complete_list = complete_list + a

        print(len(complete_list))
