#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author:    george wang
@datetime:  2019-06-05
@file:      test_lock.py
@contact:   georgewang1994@163.com
@desc:      测试锁
"""

from mredis.tests.test_basic import TestBasic


class TestLock(TestBasic):
    """
    测试锁
    """
    def setUp(self):
        super(TestLock, self).setUp()

    def test_lock_release(self):
        """
        测试加锁和释放锁
        """
        @self.mredis.func_mutex(lock_params=('a', 'b'))
        def get_sum(a, b):
            return a + b

        result = get_sum(1, 1)
        self.assertEqual(result, 2)
