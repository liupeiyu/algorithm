# -*- coding: utf-8 -*-
# @Time    : 2019-06-18 20:11
# @Author  : peiyu
# @Email   : lvegod@163.com
# @File    : 1-1-StringSubject.py
# @Software: PyCharm

'''
Question 1
leetcode: Implement strStr() | LeetCode OJ
lintcode: lintcode - (13) strstr
Problem Statement
For a given source string and a target string, you should output the first index(from 0) of target string in source string.

If target does not exist in source, just return -1.

Example
If source = "source" and target = "target", return -1.

If source = "abcdabcdefg" and target = "bcd", return 1.

Challenge
O(n2) is acceptable. Can you implement an O(n) algorithm? (hint: KMP)

Clarification
Do I need to implement KMP Algorithm in a real interview?

Not necessary. When you meet this problem in a real interview, the interviewer may just want to test your basic implementation ability. But make sure your confirm with the interviewer first.

题解

对于字符串查找问题，可使用双重 for 循环解决，效率更高的则为 KMP 算法。
双重 for 循环的使用较有讲究，因为这里需要考虑目标字符串比源字符串短的可能。
对目标字符串的循环肯定是必要的，所以可以优化的地方就在于如何访问源字符串了。
简单直观的解法是利用源字符串的长度作为 for 循环的截止索引，这种方法需要处理源字符串中剩余长度不足以匹配目标字符串的情况，
而更为高效的方案则为仅遍历源字符串中有可能和目标字符串匹配的部分索引。

'''
#method 1
class Solution:
    def strStr(self, source, target):
        if source is None or target is None:
            return -1

        for i in range(len(source) - len(target) + 1):
            for j in range(len(target)):
                if source[i + j] != target[j]:
                    break
            else:  # no break
                return i
        return -1

if __name__ == '__main__':

    s=Solution()
    source="abcdefgde"
    target="defg"
    print(s.strStr(source,target))









'''
Compare two strings A and B, determine whether A contains all of the characters in B.

The characters in string A and B are all Upper Case letters.

Example
For A = "ABCD", B = "ABC", return true.

For A = "ABCD" B = "AABC", return false.



题解
 Two Strings Are Anagrams | Data Structure and Algorithm 的变形题。
题目意思是问B中的所有字符是否都在A中，而不是单个字符。比如B="AABC"包含两个「A」，而A="ABCD"只包含一个「A」，
故返回false. 做题时注意题意，必要时可向面试官确认。
既然不是类似 strstr 那样的匹配，直接使用两重循环就不太合适了。
题目中另外给的条件则是A和B都是全大写单词，理解题意后容易想到的方案就是先遍历 A 和 B 统计各字符出现的频次，
然后比较频次大小即可。嗯，祭出万能的哈希表。
'''

