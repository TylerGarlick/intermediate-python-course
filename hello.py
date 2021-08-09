#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser(description='Say hello')
parser.add_argument('-n', '--name', help='Your name', metavar='name', default='World')
args = parser.parse_args()
print('Hello, ' + args.name)
