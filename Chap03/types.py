#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/
#
# 2020-04-19:geg
# demo of difference in float vs decimal
#
# You don't want to use floating point for money - instead use the
#

from decimal import *

a = Decimal("0.10")

b = Decimal("0.30")

# x = .1 + .1 + .1 - .3

x = a + a + a - b

print(type(x))
