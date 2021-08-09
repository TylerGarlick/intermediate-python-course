#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser(description='Say hello')
parser.add_argument('name', help='Your name')
args = parser.parse_args()
print('Hello, ' + args.name)
