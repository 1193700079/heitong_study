import heapq
import threading
import time


class DynamicPriorityQueue:
    def __init__(self):
        self.lock = threading.Lock()
        self.pq = []
        self.counter = 0  # 用于保持稳定的排序

    def put(self, priority, task):
        with self.lock:
            heapq.heappush(self.pq, (priority, self.counter, task))
            self.counter += 1

    def get(self):
        with self.lock:
            if self.pq:
                return heapq.heappop(self.pq)[2]
            raise queue.Empty

    def empty(self):
        with self.lock:
            return not self.pq


def worker_task(pq, control_event):
    while not pq.empty():
        task = pq.get()
        print(f"开始执行任务: {task}")

        if task == "优先级4的任务" and not control_event.is_set():
            print(f"任务 {task} 暂停，插入新任务并重新调度")
            pq.put(1, "优先级1的任务")
            control_event.set()  # 防止重复插入
            continue

        time.sleep(1)  # 模拟任务执行时间
        print(f"任务 {task} 完成")


# 创建动态优先级队列
pq = DynamicPriorityQueue()
tasks = [
    (2, "优先级2的任务"),
    (3, "优先级3的任务"),
    (4, "优先级4的任务"),
    (6, "优先级6的任务"),
    (5, "优先级5的任务"),
]

for priority, task in tasks:
    pq.put(priority, task)

control_event = threading.Event()
worker = threading.Thread(target=worker_task, args=(pq, control_event))
worker.start()
worker.join()

print("所有任务已完成。")
