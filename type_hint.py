#!/usr/bin/python3
# -*- coding:utf-8 -*-

def twoSum(num1: int, num2: int = 100) -> int:
    sum = num1 + num2
    return sum


if __name__ == "__main__":
    print(twoSum.__annotations__)
    print(twoSum(1, 2))
    print(twoSum(1))
    print(twoSum('I love ', 'Zijing'))
    # print(twoSum('Arsenal'))
