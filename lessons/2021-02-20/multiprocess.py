#
# same logic as per threads.py file, check that for details
#

import multiprocessing
import time

start = time.time()


# here we use CPU-bound function, a lot of math opearations
def square(number):
    print('Starting ..')
    result = 0
    for num in range(1, number):
        result += num ** 2
    print(result)


processes = []
# we just care about 3 iterations, so _(underscore) is used
for _ in range(3):
    process = multiprocessing.Process(target=square, args=(30000000,))
    process.start()
    processes.append(process)

for process in processes:
    process.join()

print(f'Process took {time.time() - start} sec(s)')
