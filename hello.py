#!/usr/bin/env python3

import argparse


def get_args():
    """
    Gets the arguments from the command line
    :return:  list of parse arguments
    """
    parser = argparse.ArgumentParser(description="Crow's nest -- choose the correct article")
    parser.add_argument('word',
                        help='word',
                        metavar='word')
    return parser.parse_args()


def main():
    args = get_args()
    word = args.word
    article = ''
    print(f'Ahoy, Captain, {article} {word} off the larboard bow!')


if __name__ == '__main__':
    main()
