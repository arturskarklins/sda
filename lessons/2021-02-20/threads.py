import threading
import time

# set the start time of execution
start = time.time()


# define Thread with return value as by default it doesn't provide that
class ThreadsWithReturn(threading.Thread):
    def __init__(self, target, args=()):
        super().__init__()
        self.target = target
        self.args = args
        self.result = None

    # execute our function and store result
    def run(self):
        # note: result attribute should be defined in constructor
        self.result = self.target(*self.args)

    # call join() as per base class, but additionally return result of run()
    def join(self, timeout=None):
        super().join(timeout)
        return self.result


# our I/O function used for testing, simulates email sending with 1.5sec delay
def emailing(name) -> str:
    print(f'Sending email to {name}')
    time.sleep(1.5)
    return f'Email send to {name}'


# list to store thread objects, to run join() later
threads = []
for profile in ['bob', 'anna', 'tom', 'tim', 'george', 'john']:
    # create thread object for each element in list
    thread = ThreadsWithReturn(target=emailing, args=profile)
    # start thread
    thread.start()
    # append(add to list) each thread object that was initiated
    threads.append(thread)

# loop through all started threads and check if they're done
for thread in threads:
    thread.join()

#
# uncommented samples below show threading one by one
#
# t1 = ThreadsWithReturn(target=emailing, args='bob')
# t2 = ThreadsWithReturn(target=emailing, args='anna')
# t3 = ThreadsWithReturn(target=emailing, args='tom')
#
# t1.start()
# t2.start()
# t3.start()
#
# print(t1.join())
# print(t2.join())
# print(t3.join())

# print some summary
print(f'Emailing took {time.time() - start} sec(s)')
