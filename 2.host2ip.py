import socket
import sys


def main():
    if len(sys.argv) != 2:
        print('Usage python3 host2ip.py [hostname]')
        return
    res = socket.gethostbyname(sys.argv[1])
    print(f'IPv4: {res}')


if __name__ == '__main__':
    main()
