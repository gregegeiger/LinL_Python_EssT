#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/
#
# 2020-08-18:geg
#
def main():
    x = kitten()
    print(type(x),x)
    
    
def kitten():
    print('Meow.')
    return [42]

if __name__ == '__main__': main()
