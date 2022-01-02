from multiprocessing.pool import ThreadPool


def stringFunction(value):
    my_str = 3 + value
    return my_str


def stringFunctio(value):
    my_str = 33 + value
    return my_str


pool = ThreadPool(processes=1)


thread1 = pool.apply_async(stringFunction, (8,))
thread2 = pool.apply_async(stringFunctio, (8,))

return_val = thread1.get()
return_val1 = thread2.get()
