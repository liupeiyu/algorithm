# -*- coding: utf-8 -*-
# @Time    : 2019-06-19 18:57
# @Author  : peiyu
# @Email   : lvegod@163.com
# @File    : work.py
# @Software: PyCharm

'''


检查括号是否完全匹配

在这个实验中，我们要求使用一个堆栈检查括号字符串是否平衡

下新建一个文件balanced_parentheses.py。根据栈的结构特点，结合 stack 代码，完成以下功能的实现。

有效括号字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。
举例：

((())): True

((()): False

(())): False

目标：

使用一个堆栈作为数据结构
来检查括号字符串是否完全匹配

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
def balanced_parentheses(parentheses):
    stack = Stack(len(parentheses))
    for parenthesis in parentheses:
        if parenthesis == '(':
            stack.push(parenthesis)
        elif parenthesis == ')':
            if stack.is_empty():
                return False
            stack.pop()
    return stack.is_empty()
if __name__ == '__main__':
    examples = ['((()))', '((())', '(()))']
    print('Balanced parentheses demonstration:\n')
    for example in examples:
        print(example + ': ' + str(balanced_parentheses(example)))