"""
python 如何模拟一个场景 ，就是任务A，任务B，任务C，都有一个优先级，为了当资源分配不够，火紧急事件发生这两种情况去手动调度执行？
"""

import asyncio
import heapq


class Task:
    def __init__(self, priority, task_id, duration):
        self.priority = priority
        self.task_id = task_id
        self.duration = duration

    def __lt__(self, other):
        return self.priority < other.priority

    async def run(self):
        print(f"Running task {self.task_id} with priority {self.priority}.")
        await asyncio.sleep(self.duration)
        print(f"Task {self.task_id} completed.")


async def scheduler(task_queue, emergency_event, resource_event):
    while task_queue or not emergency_event.is_set():
        if emergency_event.is_set():
            print("Handling emergency event.")
            await asyncio.sleep(2)
            emergency_event.clear()
            print("Emergency event handled.")
            continue

        if resource_event.is_set():
            if task_queue:
                task = heapq.heappop(task_queue)
                print(f"Scheduling task {task.task_id} due to resource allocation.")
                await task.run()
            resource_event.clear()
        else:
            if task_queue:
                task = heapq.heappop(task_queue)
                await task.run()
            else:
                await asyncio.sleep(1)


async def main():
    task_queue = []
    tasks = [Task(1, "A", 3), Task(2, "B", 2), Task(3, "C", 1)]

    for task in tasks:
        heapq.heappush(task_queue, task)

    emergency_event = asyncio.Event()
    resource_event = asyncio.Event()

    scheduler_task = asyncio.create_task(
        scheduler(task_queue, emergency_event, resource_event)
    )

    await asyncio.sleep(5)
    emergency_event.set()

    await asyncio.sleep(3)
    resource_event.set()

    await scheduler_task


if __name__ == "__main__":
    asyncio.run(main())
