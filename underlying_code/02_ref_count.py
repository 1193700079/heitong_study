"""
python  通过引用计数的形式来释放内存

pyhon的 ob_refcnt 都有一个引用计数器，当引用计数为0时，python会自动释放内存

多线程存在 racing condition的问题 即竞争冒险的问题
同样引用计数等机制存在竞争冒险的问题,所以python 设计了一个全局锁 GIL

可以用多进程来避开 gil,利用多核的问题
写 c extension的方法
用 没有gil的python的解释器  如jython


"""
