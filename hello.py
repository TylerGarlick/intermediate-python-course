#!/usr/bin/env python3

import argparse


def get_args():
    parser = argparse.ArgumentParser(description='Say hello')
    parser.add_argument('-n', '--name', help='Your name', metavar='name', default='World')
    return parser.parse_args()


def main():
    args = get_args()
    print('Hello, ' + args.name)


if __name__ == '__main__':
    main()
