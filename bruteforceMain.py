import threading
import queue
from PwdConsumer import PwdConsumer
from PwdProducer import PwdProducer


queue = queue.Queue(maxsize=10)
condition = threading.Condition()

producer = PwdProducer(queue, condition)
consumer = PwdConsumer(queue, condition)

producer.start()
consumer.start()
