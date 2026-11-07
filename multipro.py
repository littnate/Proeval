import time
import multiprocessing

def basic_func(x):
    if x == 0:
        return 'zero'
    elif x%2 == 0:
        return 'even'
    else:
        return 'odd'

if __name__ == '__main__':
    starttime = time.time()
    pool = multiprocessing.Pool()
    results = pool.map(basic_func, [i*i for i in range(0,10)])
    pool.close()
    print('That took {} seconds'.format(time.time() - starttime))