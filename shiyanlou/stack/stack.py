# -*- coding: utf-8 -*-
# @Time    : 2019-06-19 18:50
# @Author  : peiyu
# @Email   : lvegod@163.com
# @File    : stack.py
# @Software: PyCharm
'''

实现stack堆栈的功能


'''
class Stack(object):
    def __init__(self, limit=10):
        self.stack = [] #存放元素
        self.limit = limit #栈容量极限
    def push(self, data): #判断栈是否溢出
        if len(self.stack) >= self.limit:
            print('StackOverflowError')
            pass
        self.stack.append(data)
    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            raise IndexError('pop from an empty stack') #空栈不能被弹出
    def peek(self): #查看堆栈的最上面的元素
        if self.stack:
            return self.stack[-1]
    def is_empty(self): #判断栈是否为空
        return not bool(self.stack)
    def size(self): #返回栈的大小
        return len(self.stack)
if __name__ == '__main__':

    stacks=Stack()
    print("********")
    stacks.push(4)
    stacks.push(5)
    stacks.push(6)
    stacks.push(8)
    stacks.pop()


    print(stacks.is_empty())
    print(stacks.limit)
    print(stacks.size())
    print(stacks.peek())

