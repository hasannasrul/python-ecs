#!/bin/bash

import argparse

def main():
    parser = argparse.ArgumentParser(description='Print a customized greeting message.')
    parser.add_argument('--name', default='World', help='Specify the name for the greeting.')

    args = parser.parse_args()
    greeting_message = f'Hello, {args.name}!'
    print(greeting_message)

if __name__ == '__main__':
    main()
