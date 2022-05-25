import random
import logging

logging.basicConfig(level=logging.DEBUG, filename="logs.log",filemode="w",format="We have next log: %(asctime)s%(levelname)s - %(message)s")
r = range(0, 10)
it = iter(r)


l = [1+5*(next(it)) for i in r]
it = iter(l)
print(l)
for i in l:
    try:
        print( l[next(it)]/random.randint(-5, 5))
    except:
        logging.error("Division Zero")