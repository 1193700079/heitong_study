import threading
import queue
import time


def thread_task(priority_queue):
    while not priority_queue.empty():
        priority, task = priority_queue.get()
        print(f"执行任务: {task}，优先级: {priority}")
        time.sleep(1)
        priority_queue.task_done()


# 创建优先级队列
priority_queue = queue.PriorityQueue()

# 添加任务（优先级越低，越先执行）
priority_queue.put((2, "优先级最高的任务"))
priority_queue.put((3, "优先级中等的任务"))
priority_queue.put((4, "优先级较高的任务"))
priority_queue.put((5, "优先级较高的任务"))
priority_queue.put((6, "优先级较高的任务"))
priority_queue.put((1, "优先级较高的任务"))

# 创建线程
threads = [
    threading.Thread(target=thread_task, args=(priority_queue,)) for _ in range(2)
]

# 启动线程
for t in threads:
    t.start()

# 等待所有任务完成
for t in threads:
    t.join()

print("所有任务已完成。")
