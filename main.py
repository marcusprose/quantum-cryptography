""" 

main.py

"""
import sys
import time
import Encrypt


def main():
    e = Encrypt.Encrypt()
    items = list(range(0, 5))  # make list number of things to do
    l = len(items)

    # start conditions
    if sys.argv[1] == '-noeve':
        # Initial call to print 0% progress
        e.printProgressBar(0, l, prefix='Progress:',
                           suffix='Complete', length=50)
        for i, item in enumerate(items):
            # do stuff...
            e.run_without_intercept()
            # do stuff...
            time.sleep(0.1)
            # update progress bar
            e.printProgressBar(i + 1, l, prefix='Progress:',
                               suffix='Complete', length=50)
        e.print_info_1()

    elif sys.argv[1] == '-eve':
        e.printProgressBar(0, l, prefix='Progress:',
                           suffix='Complete', length=50)
        for i, item in enumerate(items):
            # do stuff...
            e.run_with_intercept()
            # do stuff...
            time.sleep(0.1)
            # Update progress bar
            e.printProgressBar(i + 1, l, prefix='Progress:',
                               suffix='Complete', length=50)
        e.print_info_2()
    elif sys.argv[1] == '-d' and sys.argv[2] == '-xor':
        e.decode_xor()

    elif sys.argv[1] == '-e' and sys.argv[2] == '-xor':
        e.encode_xor()
        # TODO: potentially add more encrypt/decrypt methods for demo

    else:
        print('Demo failed. Please try again')


if __name__ == "__main__":
    main()
