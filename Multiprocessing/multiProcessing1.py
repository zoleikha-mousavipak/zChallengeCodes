import multiprocessing


def cub(number):
    print("cub is: {}".format(number*number*number))


def square(number):
    print("square is: {}".format(number*number))


if __name__ == "__main__":

    p1 = multiprocessing.Process(target=cub, args=(10,))
    p2 = multiprocessing.Process(target=square, args=(10,))


    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Done Successfully! ")