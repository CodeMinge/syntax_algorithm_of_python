#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):
	def __init__(self, name, score):
		self.__name = name
		self.__score = score
		
	def print_score(self):
		print('%s:%s' %(self.__name, self.__score))
		
	def get_grade(self):
		if self.__score >= 90:
			return 'A'
		elif self.__score >= 60:
			return 'B'
		else:
			return 'C'
			
	def get_name(self):
		return self.__name
		
	def set_name(self, name):
		self.__name = name
		
	def get_score(self):
		return self.__score
		
	def set_score(self, score):
		if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')
			
bart = Student('Bart Simpson', 59)
# print('bart.name =', bart.name)      # 外部直接访问会出错

print('bart.get_name() =', bart.get_name())
bart.set_score(60)
print('bart.get_score() =', bart.get_score())

# 双下划线开头的实例变量是不是一定不能从外部访问呢？
# 其实也不是。不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name，
# 所以，仍然可以通过_Student__name来访问__name变量
print('DO NOT use bart._Student__name:', bart._Student__name) 