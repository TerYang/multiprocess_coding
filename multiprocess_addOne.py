import multiprocessing as mp
import threading as td
import time as tm
from queue import Queue


"""add one process"""
# def job(a,b):#q,
#     res = 0
#     for _ in range(100000):
#         res += a**2+b**2
#     return res
#     # q.put(res)


"""efficiency"""

# def multhread(a,b):
#     q = mp.Queue()
#     # a,b = 3, 4
#     # t1 = td.Thread(target=job,args=(a,b))
#     t1 = td.Thread(target=job,args=(q,a,b))#args=(q,)
#     t2 = td.Thread(target=job,args=(q,a,b))#args=(q,)
#     # t1.start()
#     t1.start()
#     t2.start()
#
#     t1.join()
#     t2.join()
#     res1 = q.get()
#     res2 = q.get()
#     print("multhreads:",res1+res2)
#
# def multcore(a,b):
#     q = mp.Queue()
#     # t1 = td.Thread(target=job,args=(a,b))
#     p1 = mp.Process(target=job,args=(q,a,b))#args=(q,)
#     p2 = mp.Process(target=job,args=(q,a,b))#args=(q,)
#     # t1.start()
#     p1.start()
#     p2.start()
#     # t1.join()
#     p1.join()
#     p2.join()
#     res1 = q.get()
#     res2 = q.get()
#     print("mulprocess:", res1 + res2)
#
# def normal(a,b):
#     res = 0
#     for _ in range(2):
#         for i in range(100000):
#             res += a ** 2 + b ** 2
#     return res

"""pool,pool have return func"""
# def job(x):#q,
#     return x*x
#     # q.put(res)
#
# def multcore():
#     # q = mp.Queue()
#     pool = mp.Pool(processes=2)
#     #default using all core, processes=3,using 3 numbers processes
#     res = pool.map(job,range(10))#map processing seq
#     print(res)
#
#     """multi args"""
#     res = pool.apply_async(job,(2,))#',' must had,args (,)
#     print(res.get())
#     multi_res = [pool.apply_async(job,(i,)) for i in range(10)]
#     print([res.get() for res in multi_res])
#     # p.terminate()：结束工作进程，不再处理未完成的任务
#     pool.close()#close pool, avoid more tasks put into pool
#     pool.join()#wait called by father process
#
#     #apply_async不用等待当前进程执行完毕，
#     # 随时根据系统调度来进行进程切换,每个进程都不需要等带执行完成
#     # apply是阻塞式的

"""lock"""
def job(v,num,l):
    l.acquire()
    for _ in range(10):
       tm.sleep(0.1)
       v.value += num
       print(v.value)
    l.release()

def multicore():
    lock = mp.Lock()
    v = mp.Value('i',0)
    p1 = mp.Process(target=job,args=(v,1,lock))
    p2 = mp.Process(target=job,args=(v,3,lock))
    p1.start()
    p2.start()
    p1.join()
    p2.join()

if __name__ == '__main__':
    # a, b = 3, 4
    """add one process"""
    # q = mp.Queue()
    # a,b = 3, 4
    # # t1 = td.Thread(target=job,args=(a,b))
    # p1 = mp.Process(target=job,args=(q,a,b))#args=(q,)
    # p2 = mp.Process(target=job,args=(q,5,6))#args=(q,)
    # # t1.start()
    # p1.start()
    # p2.start()
    # # t1.join()
    # p1.join()
    # p2.join()
    # res1 = q.get()
    # res2 = q.get()
    # print("res1:",res1)
    # print("res2:",res2)
    # print(res1+res2)

    """efficiency"""
    # a, b = 3, 4
    # t1 = tm.time()
    # re1 = normal(a,b)
    # # re2 = normal(a,b)
    # print("normal:",re1)
    # t2 = tm.time()
    # print("normal_time:",t2-t1)

    # t1 = tm.time()
    # multcore(a,b)
    # t2 = tm.time()
    # print("multiprocess_time:",t2-t1)
    #
    # t1 = tm.time()
    # multhread(a,b)
    # t2 = tm.time()
    # print("multithread_time:",t2-t1)

    """pool"""
    # t1 = tm.time()
    # multcore()
    # t2 = tm.time()
    # # print("multiprocess_time:",t2-t1)
    """shared memory"""
    # value = mp.Value('d',l)
    # array = mp.Array('i',[1,2,3])
    """reference"""
    """
        | Type code | C Type             | Python Type       | Minimum size in bytes |
    | --------- | ------------------ | ----------------- | --------------------- |
    | `'b'`     | signed char        | int               | 1                     |
    | `'B'`     | unsigned char      | int               | 1                     |
    | `'u'`     | Py_UNICODE         | Unicode character | 2                     |
    | `'h'`     | signed short       | int               | 2                     |
    | `'H'`     | unsigned short     | int               | 2                     |
    | `'i'`     | signed int         | int               | 2                     |
    | `'I'`     | unsigned int       | int               | 2                     |
    | `'l'`     | signed long        | int               | 4                     |
    | `'L'`     | unsigned long      | int               | 4                     |
    | `'q'`     | signed long long   | int               | 8                     |
    | `'Q'`     | unsigned long long | int               | 8                     |
    | `'f'`     | float              | float             | 4                     |
    | `'d'`     | double             | float             | 8                     |
    """

    """lock"""
    multicore()