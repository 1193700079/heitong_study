import asyncio


async def func():
    print(1)
    await asyncio.sleep(2)
    print(2)
    return "返回值"


async def main():
    print("main start")
    task1 = asyncio.create_task(func())
    task2 = asyncio.create_task(func())
    print("main end")
    return_value1 = await task1
    return_value2 = await task2
    print("return value:", return_value1, return_value2)


async def main():
    print("main start")

    task1 = asyncio.create_task(func(), name="t1")
    task2 = asyncio.create_task(func(), name="t2")
    task_list = [task1, task2]
    print("main end")
    done, pending = await asyncio.wait(task_list, return_when=asyncio.FIRST_COMPLETED)
    print("done:", done)
    """
    done: {<Task finished name='t1' coro=<func() done, defined at /root/hgln_project/heitong_study/yrq_async/01_task_demo.py:4> result='返回值'>, <Task finished name='t2' coro=<func() done, defined at /root/hgln_project/heitong_study/yrq_async/01_task_demo.py:4> result='返回值'>}
    """
    # print("return value:", return_value1, return_value2)


# 两种方式等价
# loop = asyncio.get_event_loop()
# loop.run_until_complete(main())

# asyncio.run(main())

task_list = [func(), func()]
# task_list = [
#     asyncio.create_task(func(), name="t1"),
#     asyncio.create_task(func(), name="t2"),
# ] 这种写法会报错 ，因为会自动创建task
done, pending = asyncio.run(
    asyncio.wait(task_list, return_when=asyncio.FIRST_COMPLETED)
)
