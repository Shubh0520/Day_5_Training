from datetime import datetime
from multiprocessing import Pool
import random
import operator

start = datetime.now()


def wrapper_add(args):
    operators = [("+", operator.add), ("-", operator.sub), ("*", operator.mul)]
    for i in range(100):
        number_1 = random.randint(1, 20)
        number_2 = random.randint(1, 20)
        op, fn = random.choice(operators)
        answer = ("{} {} {} = {}".format(number_1, op, number_2, fn(number_1, number_2)))
        print(answer)


if __name__ == "__main__":
    with Pool(processes=3) as pool:
        number = 100
        result = pool.apply_async(wrapper_add, args=(number,))
        pool = Pool(10)
        end_time = datetime.now()
        print("Duration of multi-Process operation is {}:".format(end_time - start))
