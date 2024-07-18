import asyncio


# 模拟异步I/O操作的协程函数
async def async_task(task_id, delay):
    print(f"Task {task_id} started, will take {delay} seconds.")
    await asyncio.sleep(delay)  # 模拟I/O操作的延迟
    print(f"Task {task_id} completed.")


# 主函数，负责创建和调度任务
async def main():
    tasks = [async_task(1, 2), async_task(2, 3), async_task(3, 1)]
    # 并发运行所有任务
    await asyncio.gather(*tasks)


# 运行事件循环
if __name__ == "__main__":
    asyncio.run(main())
