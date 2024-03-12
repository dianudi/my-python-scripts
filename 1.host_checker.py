import os
import sys


def main():
    if (len(sys.argv) != 2):
        print('Usage python3 host_checker.py [host]')
        return
    res = os.system(f'ping -c 1 ${str(sys.argv[1])} > /dev/null')
    if res == 0:
        print('Host is Up')
    else:
        print('Host is down')


if __name__ == '__main__':
    main()
