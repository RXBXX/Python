#!/usr/bin/env python
# -*- coding: utf-8 -*-
class F1:
    def func(self):
    	print self.show()

class S1(F1):
    def show(self):
        print 'S1.show'

class S2(F1):
    def show(self):
        print 'S2.show'

s1_obj = S1()
s2_obj = S2()

s1_obj.func()
s2_obj.func()

