import asyncio

# future 比 task 更加底层
# future 机会 都不用手写，主要是await对象


async def set_after(fut):
    await asyncio.sleep(2)
    fut.set_result("666")


async def main():
    # 获取当前事件循环
    loop = asyncio.get_running_loop()
    # 创建一个任务（Future对象）,没绑定任何行为，则这个任务永远不知道什么时候结束。
    fut = loop.create_future()
    # 创建一个任务（Task对象）,绑定了set_after函数，函数内部在2s之后，会给fut赋值。
    # 即手动设置future任务的最终结果，那么fut就可以结束了
    await loop.create_task(set_after(fut))
    # 等待Future对象获取最终结果，否则一直等下去
    data = await fut
    print(data)


asyncio.run(main())
