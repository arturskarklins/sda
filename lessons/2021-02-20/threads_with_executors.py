#
# sample illustrates concurrent.futures offered way of dealing wih threads and multiproceses
#
import concurrent.futures
import time

start = time.time()


def emailing(name) -> str:
    print(f'Sending email to {name}')
    time.sleep(1.5)
    return f'Email send to {name}'


# create context manager and loop through list
# for threads use ThreadPoolExecutor()
with concurrent.futures.ProcessPoolExecutor() as executor:
    results = executor.map(emailing, ['bob', 'anna', 'tom', 'tim', 'george', 'john'])

    for result in results:
        print(result)

print(f'Emailing took {time.time() - start} sec(s)')
