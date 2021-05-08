#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Obj():
	#构造函数，特殊字符 __init__ 声明构造函数
	#self:特殊字符串，代表类的实例
	def __init__(self, name, age):
		self._name = name
		self._age = age

	#打印出用户基本信息
	#self:特殊字符串，代表类的实例
	def printInfos(self):
		print "name:", self._name, " age:", self._age


class Obj1(Obj):
	def __init__(self, name, age):
		super(Obj1, self).__init__(name, age)

objInstance = Obj1("John", 18)
objInstance.printInfos()