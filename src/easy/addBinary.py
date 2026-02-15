"""
67. Add Binary
Easy
Given two binary strings a and b, return their sum as a binary string.

 

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
 

Constraints:

1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.
"""


from dataclasses import dataclass


@dataclass
class Digit:
    value: int # 0 or 1
    position: int 

class Solution:
    def addBinaryForNoobs(self, a: str, b: str) -> str:
        return(bin(int(a, 2) + int(b, 2))[2::])
    
    def addBinary(self, a: str, b: str) -> str:
        a_int: int = int(self.binaryToDecimal(a))
        b_int: int = int(self.binaryToDecimal(b))
        sum: int = a_int + b_int
        return self.decimalToBinary(sum)

    def binaryToDecimal(self, a: str) -> str:
        sum: int = 0
        reversed_a: str = a[::-1]

        for digit in range(0, len(reversed_a), 1):
            currentDigit: Digit = Digit(value = int(reversed_a[digit]), position = int(digit))

            # If digit is 0 result is 0
            result = currentDigit.value * (2 ** currentDigit.position)
            sum += int(result)

        return str(sum)
    
    def decimalToBinary(self, a: str) -> str:
        current = int(a)
        if current == 0:
            return "0"
        
        result_int: int = 0
        result_str: str = ""

        while(current != 0):
            result_int = current % 2
            current = current // 2
            result_str = result_str + str(result_int)

        return result_str[::-1] # Result reversed
                    
    
    
mySolution = Solution()


solutions = [
    {"a": "11", "b": "1", "expected": "100"},
    {"a": "1010", "b": "1011", "expected": "10101"},
    {"a": "0", "b": "0", "expected": "0"},
    {"a": "0", "b": "1", "expected": "1"},
    {"a": "1", "b": "0", "expected": "1"},
    {"a": "1", "b": "1", "expected": "10"},
    {"a": "10", "b": "1", "expected": "11"},
    {"a": "100", "b": "1", "expected": "101"},
    {"a": "111", "b": "1", "expected": "1000"},
    {"a": "1111", "b": "1", "expected": "10000"},
    {"a": "111", "b": "111", "expected": "1110"},
    {"a": "1011", "b": "1101", "expected": "11000"},
    {"a": "100000", "b": "1", "expected": "100001"},
    {"a": "1", "b": "100000", "expected": "100001"},
    {"a": "1010101010101010", "b": "1100110011001100", "expected": "10111011101110110"},
    {"a": "11111111", "b": "11111111", "expected": "111111110"},
    {"a": "0", "b": "1111", "expected": "1111"},
    {"a": "1111", "b": "0", "expected": "1111"},
    {"a": "1" * 32,"b": "1","expected": "1" + "0" * 32},
]


for solution in solutions:
    result = mySolution.addBinary(solution['a'], solution['b'])
    assert result == solution['expected'], (
        f"Error: {solution['a']} + {solution['b']} "
        f"expected {solution['expected']} but got {result}"
    )

print("All tests passed")

