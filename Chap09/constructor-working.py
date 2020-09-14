#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/
#
# 2020-08-23:geg
# First object oriented code that I modified in this training class
#

class Animal:
    #
    # __init__ is a special class method name
    # This is a Constructor - operates as an intiializer
    # note the first parameter is always self
    # Initialize object variables
    #
    #
    # Original code
    # def __init__(self, type, name, sound):
    #
    # Convert to use **kwargs - dictionary
    def __init__(self, **kwargs):
        #
        # _ at beginning of name is a convention to show this is an object variable
        # The object variable does not exist until the object is creates
        #
        # Original code
        # self._type = type
        # self._name = name
        # self._sound = sound
        #
        # Convert to use **kwargs
        #
        
        self._type = kwargs['type']
        self._name = kwargs['name']
        self._sound = kwargs['sound']

    def type(self):
        return self._type

    def name(self):
        return self._name

    def sound(self):
        return self._sound

def print_animal(o):
    if not isinstance(o, Animal):
        raise TypeError('print_animal(): requires an Animal')
    #
    # Accessors or "gettors" to access the variables
    #
    print('The {} is named "{}" and says "{}".'.format(o.type(), o.name(), o.sound()))


def main():
    # Create the objects
    # Original - you had to recall the position of the object variables
    #
    # a0 = Animal('kitten', 'fluffy', 'rwar')
    #
    a0 = Animal(type='kitten', name='fluffy', sound='rwar')
    a1 = Animal(type='duck', name='donald', sound='quack')
    print_animal(a0)
    print_animal(a1)
    print_animal(Animal(type='velociraptor', name='veronica', sound='hello'))

if __name__ == '__main__': main()
