from django.core.management.base import BaseCommand
from problems.models import Tag, Problem, Example, TestCases


problems_data = [
        {
                "title": "Two Sum",
                "description": """Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

You may assume that each input would have **exactly one solution**, and you may not use the same element twice.

You can return the answer in any order.""",
                "input_format": """The first line contains an integer `n`, the size of the array.
The second line contains `n` space-separated integers.
The third line contains the target integer.""",
                "output_format": "Print two space-separated integers representing the indices of the two numbers that add up to target.",
                "difficulty": "Easy",
                "tags": ["Arrays"],
                "constraints": """- \\(2 \\leq \\text{n} \\leq 10^4\\)
- \\(-10^9 \\leq \\text{nums}[i] \\leq 10^9\\)
- \\(-10^9 \\leq \\text{target} \\leq 10^9\\)
- Only one valid answer exists.""",
                "time_limit": 1.0,
                "memory_limit": 256,
                "examples": [
                        {"input": "4\n2 7 11 15\n9", "output": "0 1", "explanation": "Because nums[0] + nums[1] == 9, we return [0, 1]."},
                        {"input": "3\n3 2 4\n6", "output": "1 2", "explanation": "nums[1] + nums[2] == 6."},
                        {"input": "2\n3 3\n6", "output": "0 1", "explanation": "The only pair is (0, 1)."},
                ],
                "testcases": [
                        {"input": "4\n2 7 11 15\n9", "output": "0 1"},
                        {"input": "3\n3 2 4\n6", "output": "1 2"},
                        {"input": "2\n3 3\n6", "output": "0 1"},
                        {"input": "5\n1 5 8 3 9\n11", "output": "1 3"},
                        {"input": "4\n-1 -2 -3 -4\n-5", "output": "0 3"},
                ],
        },
        {
                "title": "Reverse a Linked List",
                "description": """Given the head of a singly linked list, reverse the list, and return the reversed list.

The input is given as space-separated integers representing the linked list values. Output should be the reversed list as space-separated integers.""",
                "input_format": "The first line contains an integer `n`, the number of nodes. The second line contains `n` space-separated integers representing the values of the linked list.",
                "output_format": "Print `n` space-separated integers representing the reversed linked list.",
                "difficulty": "Easy",
                "tags": ["Linked Lists"],
                "constraints": """- The number of nodes in the list is in the range \\([0, 5000]\\).
- \\(-5000 \\leq \\text{Node.val} \\leq 5000\\)
- **Follow up:** Can you solve it iteratively and recursively?""",
                "time_limit": 1.0,
                "memory_limit": 256,
                "examples": [
                        {"input": "5\n1 2 3 4 5", "output": "5 4 3 2 1", "explanation": "The list 1→2→3→4→5 reversed is 5→4→3→2→1."},
                        {"input": "2\n1 2", "output": "2 1", "explanation": "Two node list reversed."},
                        {"input": "1\n5", "output": "5", "explanation": "Single node list reversed is itself."},
                ],
                "testcases": [
                        {"input": "5\n1 2 3 4 5", "output": "5 4 3 2 1"},
                        {"input": "2\n1 2", "output": "2 1"},
                        {"input": "1\n5", "output": "5"},
                        {"input": "0\n", "output": ""},
                        {"input": "6\n10 20 30 40 50 60", "output": "60 50 40 30 20 10"},
                ],
        },
        {
                "title": "Valid Parentheses",
                "description": """Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.""",
                "input_format": "A single line containing the string `s` consisting of brackets only.",
                "output_format": "Print `true` if the string is valid, otherwise print `false`.",
                "difficulty": "Easy",
                "tags": ["Strings", "Stacks"],
                "constraints": """- \\(1 \\leq |s| \\leq 10^4\\)
- \\(s\\) consists of parentheses only: `'()[]{}'`""",
                "time_limit": 1.0,
                "memory_limit": 256,
                "examples": [
                        {"input": "()", "output": "true", "explanation": "Simple matching parentheses."},
                        {"input": "()[]{}", "output": "true", "explanation": "Multiple bracket types in order."},
                        {"input": "(]", "output": "false", "explanation": "Mismatched brackets."},
                ],
                "testcases": [
                        {"input": "()", "output": "true"},
                        {"input": "()[]{}", "output": "true"},
                        {"input": "(]", "output": "false"},
                        {"input": "([)]", "output": "false"},
                        {"input": "{[]}", "output": "true"},
                        {"input": "", "output": "true"},
                ],
        },
        {
                "title": "Maximum Subarray",
                "description": """Given an integer array `nums`, find the contiguous subarray (containing at least one number) which has the largest sum and return **its sum**.

A **subarray** is a contiguous part of an array.""",
                "input_format": "The first line contains an integer `n`, the size of the array. The second line contains `n` space-separated integers.",
                "output_format": "Print a single integer — the maximum subarray sum.",
                "difficulty": "Medium",
                "tags": ["Arrays", "Dynamic Programming"],
                "constraints": """- \\(1 \\leq n \\leq 10^5\\)
- \\(-10^4 \\leq \\text{nums}[i] \\leq 10^4\\)
- Expected time complexity: \\(O(n)\\)""",
                "time_limit": 1.0,
                "memory_limit": 256,
                "examples": [
                        {"input": "9\n-2 1 -3 4 -1 2 1 -5 4", "output": "6", "explanation": "The subarray [4,-1,2,1] has the largest sum 6."},
                        {"input": "1\n1", "output": "1", "explanation": "Single element array."},
                        {"input": "5\n5 4 -1 7 8", "output": "23", "explanation": "The subarray [5,4,-1,7,8] has sum 23."},
                ],
                "testcases": [
                        {"input": "9\n-2 1 -3 4 -1 2 1 -5 4", "output": "6"},
                        {"input": "1\n1", "output": "1"},
                        {"input": "5\n5 4 -1 7 8", "output": "23"},
                        {"input": "5\n-1 -2 -3 -4 -5", "output": "-1"},
                        {"input": "4\n-2 1 -3 4", "output": "4"},
                ],
        },
        {
                "title": "Binary Search",
                "description": """Given an array of integers `nums` which is sorted in ascending order, and an integer `target`, write a function to search `target` in `nums`. If `target` exists, then return its index. Otherwise, return `-1`.

You must write an algorithm with **O(log n)** runtime complexity.""",
                "input_format": "The first line contains an integer `n`, the size of the sorted array. The second line contains `n` space-separated integers in ascending order. The third line contains the target integer.",
                "output_format": "Print the index of the target if found, otherwise print `-1`.",
                "difficulty": "Easy",
                "tags": ["Arrays", "Binary Search"],
                "constraints": """- \\(1 \\leq n \\leq 10^5\\)
- \\(-10^4 \\leq \\text{nums}[i] \\leq 10^4\\)
- All integers in `nums` are unique and sorted in ascending order.
- \\(-10^4 \\leq \\text{target} \\leq 10^4\\)""",
                "time_limit": 1.0,
                "memory_limit": 256,
                "examples": [
                        {"input": "6\n-1 0 3 5 9 12\n9", "output": "4", "explanation": "9 exists in nums and its index is 4."},
                        {"input": "6\n-1 0 3 5 9 12\n2", "output": "-1", "explanation": "2 does not exist in nums so return -1."},
                        {"input": "3\n2 5 7\n7", "output": "2", "explanation": "7 is at index 2."},
                ],
                "testcases": [
                        {"input": "6\n-1 0 3 5 9 12\n9", "output": "4"},
                        {"input": "6\n-1 0 3 5 9 12\n2", "output": "-1"},
                        {"input": "3\n2 5 7\n7", "output": "2"},
                        {"input": "1\n5\n5", "output": "0"},
                        {"input": "4\n1 3 5 7\n8", "output": "-1"},
                ],
        },
        {
                "title": "Fibonacci Number",
                "description": """The **Fibonacci numbers**, commonly denoted `F(n)` form a sequence, called the **Fibonacci sequence**, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is:

- F(0) = 0, F(1) = 1
- F(n) = F(n - 1) + F(n - 2), for n > 1.

Given `n`, calculate `F(n)`.""",
                "input_format": "A single line containing an integer `n`.",
                "output_format": "Print the nth Fibonacci number.",
                "difficulty": "Easy",
                "tags": ["Dynamic Programming", "Math"],
                "constraints": """- \\(0 \\leq n \\leq 30\\)""",
                "time_limit": 1.0,
                "memory_limit": 256,
                "examples": [
                        {"input": "2", "output": "1", "explanation": "F(2) = F(1) + F(0) = 1 + 0 = 1."},
                        {"input": "3", "output": "2", "explanation": "F(3) = F(2) + F(1) = 1 + 1 = 2."},
                        {"input": "4", "output": "3", "explanation": "F(4) = F(3) + F(2) = 2 + 1 = 3."},
                ],
                "testcases": [
                        {"input": "0", "output": "0"},
                        {"input": "1", "output": "1"},
                        {"input": "2", "output": "1"},
                        {"input": "5", "output": "5"},
                        {"input": "10", "output": "55"},
                ],
        },
        {
                "title": "Fizz Buzz",
                "description": """Given an integer `n`, return a string array `answer` (1-indexed) where:

- `answer[i] == "FizzBuzz"` if `i` is divisible by 3 and 5.
- `answer[i] == "Fizz"` if `i` is divisible by 3.
- `answer[i] == "Buzz"` if `i` is divisible by 5.
- `answer[i] == i` (as a string) otherwise.

Output each element on a new line.""",
                "input_format": "A single line containing an integer `n`.",
                "output_format": "Print `n` lines, each containing the corresponding FizzBuzz output.",
                "difficulty": "Easy",
                "tags": ["Strings", "Math"],
                "constraints": """- \\(1 \\leq n \\leq 10^4\\)""",
                "time_limit": 1.0,
                "memory_limit": 256,
                "examples": [
                        {"input": "3", "output": "1\n2\nFizz", "explanation": "1, 2, Fizz."},
                        {"input": "5", "output": "1\n2\nFizz\n4\nBuzz", "explanation": "Standard FizzBuzz up to 5."},
                        {"input": "15", "output": "1\n2\nFizz\n4\nBuzz\nFizz\n7\n8\nFizz\nBuzz\n11\nFizz\n13\n14\nFizzBuzz", "explanation": "FizzBuzz at 15."},
                ],
                "testcases": [
                        {"input": "3", "output": "1\n2\nFizz"},
                        {"input": "5", "output": "1\n2\nFizz\n4\nBuzz"},
                        {"input": "15", "output": "1\n2\nFizz\n4\nBuzz\nFizz\n7\n8\nFizz\nBuzz\n11\nFizz\n13\n14\nFizzBuzz"},
                        {"input": "1", "output": "1"},
                        {"input": "7", "output": "1\n2\nFizz\n4\nBuzz\nFizz\n7"},
                ],
        },
        {
                "title": "Climbing Stairs",
                "description": """You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?""",
                "input_format": "A single integer `n` — the number of steps.",
                "output_format": "A single integer — the number of distinct ways to climb to the top.",
                "difficulty": "Easy",
                "tags": ["Dynamic Programming", "Math"],
                "constraints": """- \\(1 \\leq n \\leq 45\\)""",
                "time_limit": 1.0,
                "memory_limit": 256,
                "examples": [
                        {"input": "2", "output": "2", "explanation": "1 step + 1 step, 2 steps."},
                        {"input": "3", "output": "3", "explanation": "1+1+1, 1+2, 2+1."},
                        {"input": "4", "output": "5", "explanation": "1+1+1+1, 1+1+2, 1+2+1, 2+1+1, 2+2."},
                ],
                "testcases": [
                        {"input": "1", "output": "1"},
                        {"input": "2", "output": "2"},
                        {"input": "3", "output": "3"},
                        {"input": "4", "output": "5"},
                        {"input": "5", "output": "8"},
                ],
        },
        {
                "title": "Print Hello World",
                "description": """Print `Hello, World!` to the standard output.""",
                "input_format": "No input.",
                "output_format": "Print `Hello, World!` exactly as shown.",
                "difficulty": "Easy",
                "tags": ["Strings"],
                "constraints": "- No constraints.",
                "time_limit": 1.0,
                "memory_limit": 256,
                "examples": [
                        {"input": "", "output": "Hello, World!", "explanation": "Standard greeting."},
                ],
                "testcases": [
                        {"input": "", "output": "Hello, World!"},
                ],
        },
        {
                "title": "Find Maximum",
                "description": """Given an array of integers, find and return the maximum element.""",
                "input_format": "The first line contains an integer `n`, the size of the array. The second line contains `n` space-separated integers.",
                "output_format": "Print a single integer — the maximum element in the array.",
                "difficulty": "Easy",
                "tags": ["Arrays"],
                "constraints": "- \\(1 \\leq n \\leq 10^5\\)\n- \\(-10^9 \\leq \\text{arr}[i] \\leq 10^9\\)",
                "time_limit": 1.0,
                "memory_limit": 256,
                "examples": [
                        {"input": "5\n1 8 3 2 5", "output": "8", "explanation": "8 is the largest element."},
                        {"input": "3\n-1 -5 -2", "output": "-1", "explanation": "-1 is the largest (least negative)."},
                        {"input": "1\n42", "output": "42", "explanation": "Single element."},
                ],
                "testcases": [
                        {"input": "5\n1 8 3 2 5", "output": "8"},
                        {"input": "3\n-1 -5 -2", "output": "-1"},
                        {"input": "1\n42", "output": "42"},
                        {"input": "6\n100 200 50 300 150 250", "output": "300"},
                        {"input": "4\n-10 -20 -30 -5", "output": "-5"},
                ],
        },
        {
                "title": "Palindrome Number",
                "description": """Given an integer `x`, return `true` if `x` is a **palindrome**, and `false` otherwise.

An integer is a palindrome when it reads the same forward and backward.""",
                "input_format": "A single line containing an integer `x`.",
                "output_format": "Print `true` if the integer is a palindrome, otherwise print `false`.",
                "difficulty": "Easy",
                "tags": ["Math"],
                "constraints": """- \\(-2^{31} \\leq x \\leq 2^{31} - 1\\)
- **Follow up:** Could you solve it without converting the integer to a string?""",
                "time_limit": 1.0,
                "memory_limit": 256,
                "examples": [
                        {"input": "121", "output": "true", "explanation": "121 reads as 121 from left to right and from right to left."},
                        {"input": "-121", "output": "false", "explanation": "-121 reads as 121- from right to left."},
                        {"input": "10", "output": "false", "explanation": "10 reads as 01 from right to left."},
                ],
                "testcases": [
                        {"input": "121", "output": "true"},
                        {"input": "-121", "output": "false"},
                        {"input": "10", "output": "false"},
                        {"input": "0", "output": "true"},
                        {"input": "12321", "output": "true"},
                        {"input": "100", "output": "false"},
                ],
        },
        {
                "title": "Merge Two Sorted Lists",
                "description": """You are given the heads of two sorted linked lists `list1` and `list2`.

Merge the two lists into one **sorted** list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

The input is given as space-separated integers for each list.""",
                "input_format": "The first line contains an integer `n`, the size of the first list. The second line contains `n` space-separated integers in ascending order. The third line contains an integer `m`, the size of the second list. The fourth line contains `m` space-separated integers in ascending order.",
                "output_format": "Print the merged sorted list as space-separated integers.",
                "difficulty": "Easy",
                "tags": ["Linked Lists"],
                "constraints": """- The number of nodes in both lists is in the range \\([0, 50]\\).
- \\(-100 \\leq \\text{Node.val} \\leq 100\\)
- Both lists are sorted in non-decreasing order.""",
                "time_limit": 1.0,
                "memory_limit": 256,
                "examples": [
                        {"input": "3\n1 2 4\n3\n1 3 4", "output": "1 1 2 3 4 4", "explanation": "Merging [1,2,4] and [1,3,4] gives [1,1,2,3,4,4]."},
                        {"input": "0\n\n0\n", "output": "", "explanation": "Both lists are empty."},
                        {"input": "1\n0\n0\n", "output": "0", "explanation": "One list is empty, the other has a single node 0."},
                ],
                "testcases": [
                        {"input": "3\n1 2 4\n3\n1 3 4", "output": "1 1 2 3 4 4"},
                        {"input": "0\n\n0\n", "output": ""},
                        {"input": "1\n0\n0\n", "output": "0"},
                        {"input": "3\n1 5 9\n2\n2 6", "output": "1 2 5 6 9"},
                        {"input": "0\n\n2\n-5 0", "output": "-5 0"},
                        {"input": "2\n-10 -5\n3\n-8 -3 0", "output": "-10 -8 -5 -3 0"},
                ],
        },
        {
                "title": "Maximum Depth of Binary Tree",
                "description": """Given the `root` of a binary tree, return its maximum depth.

A binary tree's **maximum depth** is the number of nodes along the longest path from the root node down to the farthest leaf node.

The input is given as space-separated integers representing the level-order traversal of the tree. Use `null` for missing nodes.""",
                "input_format": "The first line contains an integer `n`, the number of elements in the level-order representation. The second line contains `n` space-separated values, where `null` represents a missing node.",
                "output_format": "Print a single integer — the maximum depth of the tree.",
                "difficulty": "Easy",
                "tags": ["Trees", "Binary Tree"],
                "constraints": """- The number of nodes in the tree is in the range \\([0, 10^4]\\).
- \\(-100 \\leq \\text{Node.val} \\leq 100\\)""",
                "time_limit": 1.0,
                "memory_limit": 256,
                "examples": [
                        {"input": "7\n3 9 20 null null 15 7", "output": "3", "explanation": "The maximum depth is 3 (root → 20 → 15 or root → 20 → 7)."},
                        {"input": "1\n1", "output": "1", "explanation": "Single node tree has depth 1."},
                        {"input": "2\n1 null", "output": "1", "explanation": "Root with only a left null child (effectively just root)."},
                ],
                "testcases": [
                        {"input": "7\n3 9 20 null null 15 7", "output": "3"},
                        {"input": "1\n1", "output": "1"},
                        {"input": "2\n1 null", "output": "1"},
                        {"input": "0\n", "output": "0"},
                        {"input": "10\n1 2 3 4 null null 5 null null null null", "output": "3"},
                ],
        },
        {
                "title": "Contains Duplicate",
                "description": """Given an integer array `nums`, return `true` if any value appears **at least twice** in the array, and return `false` if every element is distinct.""",
                "input_format": "The first line contains an integer `n`, the size of the array. The second line contains `n` space-separated integers.",
                "output_format": "Print `true` if there is any duplicate, otherwise print `false`.",
                "difficulty": "Easy",
                "tags": ["Arrays", "Hash Set"],
                "constraints": """- \\(1 \\leq n \\leq 10^5\\)
- \\(-10^9 \\leq \\text{nums}[i] \\leq 10^9\\)""",
                "time_limit": 1.0,
                "memory_limit": 256,
                "examples": [
                        {"input": "4\n1 2 3 1", "output": "true", "explanation": "The value 1 appears twice."},
                        {"input": "4\n1 2 3 4", "output": "false", "explanation": "All elements are distinct."},
                        {"input": "3\n1 1 1", "output": "true", "explanation": "All elements are the same."},
                ],
                "testcases": [
                        {"input": "4\n1 2 3 1", "output": "true"},
                        {"input": "4\n1 2 3 4", "output": "false"},
                        {"input": "3\n1 1 1", "output": "true"},
                        {"input": "1\n5", "output": "false"},
                        {"input": "5\n-1 -2 -3 -1 -4", "output": "true"},
                ],
        },
        {
                "title": "Missing Number",
                "description": """Given an array `nums` containing `n` distinct numbers in the range `[0, n]`, return the only number in the range that is missing from the array.""",
                "input_format": "The first line contains an integer `n`, the size of the array. The second line contains `n` space-separated integers (distinct, each in \\([0, n]\\)).",
                "output_format": "Print the missing number.",
                "difficulty": "Easy",
                "tags": ["Arrays", "Math", "Bit Manipulation"],
                "constraints": """- \\(1 \\leq n \\leq 10^5\\)
- \\(0 \\leq \\text{nums}[i] \\leq n\\)
- All numbers in `nums` are unique.
- **Follow up:** Can you do it in \\(O(1)\\) extra space and \\(O(n)\\) runtime?""",
                "time_limit": 1.0,
                "memory_limit": 256,
                "examples": [
                        {"input": "3\n3 0 1", "output": "2", "explanation": "n = 3, numbers in [0,3]. 2 is missing."},
                        {"input": "2\n0 1", "output": "2", "explanation": "n = 2, numbers in [0,2]. 2 is missing."},
                        {"input": "1\n0", "output": "1", "explanation": "n = 1, numbers in [0,1]. 1 is missing."},
                ],
                "testcases": [
                        {"input": "3\n3 0 1", "output": "2"},
                        {"input": "2\n0 1", "output": "2"},
                        {"input": "1\n0", "output": "1"},
                        {"input": "9\n9 6 4 2 3 5 7 0 1", "output": "8"},
                        {"input": "1\n1", "output": "0"},
                        {"input": "5\n5 4 3 2 1", "output": "0"},
                ],
        },
        {
                "title": "Intersection of Two Arrays",
                "description": """Given two integer arrays `nums1` and `nums2`, return an array of their intersection. Each element in the result must be **unique** and you may return the result in **any order**.""",
                "input_format": "The first line contains an integer `n`, the size of the first array. The second line contains `n` space-separated integers. The third line contains an integer `m`, the size of the second array. The fourth line contains `m` space-separated integers.",
                "output_format": "Print the intersection elements as space-separated integers. If no intersection, print nothing.",
                "difficulty": "Easy",
                "tags": ["Arrays", "Hash Set"],
                "constraints": """- \\(1 \\leq n, m \\leq 1000\\)
- \\(0 \\leq \\text{nums}[i] \\leq 1000\\)
- **Follow up:** What if the arrays are sorted? How would you optimize?""",
                "time_limit": 1.0,
                "memory_limit": 256,
                "examples": [
                        {"input": "4\n1 2 2 1\n2\n2 2", "output": "2", "explanation": "Intersection of [1,2,2,1] and [2,2] is [2]."},
                        {"input": "3\n4 9 5\n5\n9 4 9 8 4", "output": "9 4", "explanation": "Intersection of [4,9,5] and [9,4,9,8,4] is {9,4}."},
                        {"input": "2\n1 2\n2\n3 4", "output": "", "explanation": "No common elements."},
                ],
                "testcases": [
                        {"input": "4\n1 2 2 1\n2\n2 2", "output": "2"},
                        {"input": "3\n4 9 5\n5\n9 4 9 8 4", "output": "9 4"},
                        {"input": "2\n1 2\n2\n3 4", "output": ""},
                        {"input": "1\n1\n1\n1", "output": "1"},
                        {"input": "1\n7\n1\n3", "output": ""},
                        {"input": "3\n1 2 3\n3\n1 2 3", "output": "1 2 3"},
                ],
        },
        {
                "title": "Find the Difference",
                "description": """You are given two strings `s` and `t`.

String `t` is generated by random shuffling string `s` and then adding one more letter at a random position.

Return the letter that was added to `t`.""",
                "input_format": "The first line contains the string `s`. The second line contains the string `t`.",
                "output_format": "Print the character that was added.",
                "difficulty": "Easy",
                "tags": ["Strings", "Bit Manipulation", "Hash Table"],
                "constraints": """- \\(0 \\leq |s| \\leq 1000\\)
- \\(|t| = |s| + 1\\)
- \\(s\\) and \\(t\\) consist of lowercase English letters.""",
                "time_limit": 1.0,
                "memory_limit": 256,
                "examples": [
                        {"input": "abcd\nabcde", "output": "e", "explanation": "e is the letter that was added."},
                        {"input": "\ny", "output": "y", "explanation": "s is empty, t is 'y'."},
                        {"input": "a\naa", "output": "a", "explanation": "One 'a' was added to 'a' to make 'aa'."},
                ],
                "testcases": [
                        {"input": "abcd\nabcde", "output": "e"},
                        {"input": "\ny", "output": "y"},
                        {"input": "a\naa", "output": "a"},
                        {"input": "xyz\nxyzu", "output": "u"},
                        {"input": "hello\nhelloo", "output": "o"},
                        {"input": "listen\nlistena", "output": "a"},
                ],
        },
        {
                "title": "Is Subsequence",
                "description": """Given two strings `s` and `t`, return `true` if `s` is a **subsequence** of `t`, or `false` otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters.""",
                "input_format": "The first line contains the string `s`. The second line contains the string `t`.",
                "output_format": "Print `true` if `s` is a subsequence of `t`, otherwise print `false`.",
                "difficulty": "Easy",
                "tags": ["Strings", "Two Pointers"],
                "constraints": """- \\(0 \\leq |s| \\leq 100\\)
- \\(0 \\leq |t| \\leq 10^4\\)
- Both strings consist only of lowercase English letters.
- **Follow up:** If there are many incoming `s` queries, how would you optimize?""",
                "time_limit": 1.0,
                "memory_limit": 256,
                "examples": [
                        {"input": "abc\nahbgdc", "output": "true", "explanation": "abc is a subsequence of ahbgdc."},
                        {"input": "axc\nahbgdc", "output": "false", "explanation": "axc is not a subsequence."},
                        {"input": "\nahbgdc", "output": "true", "explanation": "Empty string is always a subsequence."},
                ],
                "testcases": [
                        {"input": "abc\nahbgdc", "output": "true"},
                        {"input": "axc\nahbgdc", "output": "false"},
                        {"input": "\nahbgdc", "output": "true"},
                        {"input": "b\nabc", "output": "true"},
                        {"input": "z\nabc", "output": "false"},
                        {"input": "aaaa\nbbaaaa", "output": "true"},
                ],
        },
        {
                "title": "Add Two Numbers",
                "description": """You are given two non-empty linked lists representing two non-negative integers. The digits are stored in **reverse order**, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

The input is given as space-separated integers for each linked list.""",
                "input_format": "The first line contains an integer `n`, the size of the first list. The second line contains `n` space-separated integers (digits in reverse order). The third line contains an integer `m`, the size of the second list. The fourth line contains `m` space-separated integers (digits in reverse order).",
                "output_format": "Print the resulting linked list as space-separated integers (digits in reverse order).",
                "difficulty": "Medium",
                "tags": ["Linked Lists", "Math"],
                "constraints": """- The number of nodes in each list is in the range \\([1, 100]\\).
- \\(0 \\leq \\text{Node.val} \\leq 9\\)
- It is guaranteed that the list represents a number that does not have leading zeros.""",
                "time_limit": 1.0,
                "memory_limit": 256,
                "examples": [
                        {"input": "3\n2 4 3\n3\n5 6 4", "output": "7 0 8", "explanation": "342 + 465 = 807, represented as [7,0,8]."},
                        {"input": "1\n0\n1\n0", "output": "0", "explanation": "0 + 0 = 0."},
                        {"input": "7\n9 9 9 9 9 9 9\n3\n9 9 9", "output": "8 9 9 9 0 0 0 1", "explanation": "9999999 + 999 = 10000998, represented as [8,9,9,9,0,0,0,1]."},
                ],
                "testcases": [
                        {"input": "3\n2 4 3\n3\n5 6 4", "output": "7 0 8"},
                        {"input": "1\n0\n1\n0", "output": "0"},
                        {"input": "7\n9 9 9 9 9 9 9\n3\n9 9 9", "output": "8 9 9 9 0 0 0 1"},
                        {"input": "1\n5\n1\n5", "output": "0 1"},
                        {"input": "2\n1 8\n1\n0", "output": "1 8"},
                        {"input": "3\n1 2 3\n3\n4 5 6", "output": "5 7 9"},
                ],
        },
        {
                "title": "Longest Substring Without Repeating Characters",
                "description": """Given a string `s`, find the length of the **longest substring** without repeating characters.""",
                "input_format": "A single line containing the string `s`.",
                "output_format": "Print a single integer — the length of the longest substring without repeating characters.",
                "difficulty": "Medium",
                "tags": ["Strings", "Sliding Window", "Hash Table"],
                "constraints": """- \\(0 \\leq |s| \\leq 5 \\times 10^4\\)
- \\(s\\) consists of English letters, digits, symbols and spaces.""",
                "time_limit": 1.0,
                "memory_limit": 256,
                "examples": [
                        {"input": "abcabcbb", "output": "3", "explanation": "The answer is 'abc', with the length of 3."},
                        {"input": "bbbbb", "output": "1", "explanation": "The answer is 'b', with the length of 1."},
                        {"input": "pwwkew", "output": "3", "explanation": "The answer is 'wke', with length 3."},
                ],
                "testcases": [
                        {"input": "abcabcbb", "output": "3"},
                        {"input": "bbbbb", "output": "1"},
                        {"input": "pwwkew", "output": "3"},
                        {"input": "", "output": "0"},
                        {"input": " ", "output": "1"},
                        {"input": "au", "output": "2"},
                        {"input": "dvdf", "output": "3"},
                ],
        },
        {
                "title": "3Sum",
                "description": """Given an integer array `nums`, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`.

The solution set must not contain duplicate triplets.

Print each triplet on a new line, with its elements space-separated and sorted in ascending order.""",
                "input_format": "The first line contains an integer `n`, the size of the array. The second line contains `n` space-separated integers.",
                "output_format": "Print each triplet on a new line, with its three integers space-separated and sorted in ascending order. If no triplets exist, print nothing.",
                "difficulty": "Medium",
                "tags": ["Arrays", "Two Pointers", "Sorting"],
                "constraints": """- \\(3 \\leq n \\leq 3000\\)
- \\(-10^5 \\leq \\text{nums}[i] \\leq 10^5\\)
- Expected time complexity: \\(O(n^2)\\)""",
                "time_limit": 1.0,
                "memory_limit": 256,
                "examples": [
                        {"input": "6\n-1 0 1 2 -1 -4", "output": "-1 -1 2\n-1 0 1", "explanation": "The distinct triplets that sum to 0 are [-1,-1,2] and [-1,0,1]."},
                        {"input": "3\n0 1 1", "output": "", "explanation": "No triplet sums to 0."},
                        {"input": "3\n0 0 0", "output": "0 0 0", "explanation": "The only triplet is [0,0,0]."},
                ],
                "testcases": [
                        {"input": "6\n-1 0 1 2 -1 -4", "output": "-1 -1 2\n-1 0 1"},
                        {"input": "3\n0 1 1", "output": ""},
                        {"input": "3\n0 0 0", "output": "0 0 0"},
                        {"input": "5\n1 2 -2 -1 0", "output": "-2 0 2\n-1 0 1"},
                        {"input": "4\n-2 0 0 2", "output": "-2 0 2"},
                        {"input": "7\n-1 0 1 2 -1 -4 -2", "output": "-2 -1 3\n-1 -1 2\n-1 0 1"},
                ],
        },
        {
                "title": "Group Anagrams",
                "description": """Given an array of strings `strs`, group the anagrams together. You can return the answer in **any order**.

An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Print each group on a new line, with the strings space-separated.""",
                "input_format": "The first line contains an integer `n`, the number of strings. The next `n` lines each contain one string.",
                "output_format": "Print each group of anagrams on a new line, with the strings space-separated. Groups can be in any order.",
                "difficulty": "Medium",
                "tags": ["Strings", "Hash Table", "Sorting"],
                "constraints": """- \\(1 \\leq n \\leq 10^4\\)
- \\(0 \\leq |s_i| \\leq 100\\)
- \\(s_i\\) consists of lowercase English letters.""",
                "time_limit": 1.0,
                "memory_limit": 256,
                "examples": [
                        {"input": "6\n eat tea tan ate nat bat", "output": "tan nat\nbat\neat tea ate", "explanation": "Anagram groups: [tan, nat], [bat], [eat, tea, ate]."},
                        {"input": "1\n", "output": "", "explanation": "Single empty string."},
                        {"input": "3\n a a a", "output": "a a a", "explanation": "All identical strings are anagrams."},
                ],
                "testcases": [
                        {"input": "6\n eat tea tan ate nat bat", "output": "tan nat\nbat\neat tea ate"},
                        {"input": "1\n\n", "output": ""},
                        {"input": "3\n a a a", "output": "a a a"},
                        {"input": "0", "output": ""},
                        {"input": "2\n ab ba", "output": "ab ba"},
                ],
        },
        {
                "title": "Product of Array Except Self",
                "description": """Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`.

You must write an algorithm that runs in **O(n)** time without using the division operation.""",
                "input_format": "The first line contains an integer `n`, the size of the array. The second line contains `n` space-separated integers.",
                "output_format": "Print `n` space-separated integers — the product array where each element is the product of all elements except itself.",
                "difficulty": "Medium",
                "tags": ["Arrays", "Prefix Sum"],
                "constraints": """- \\(2 \\leq n \\leq 10^5\\)
- \\(-30 \\leq \\text{nums}[i] \\leq 30\\)
- The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
- **Follow up:** Can you solve it in \\(O(1)\\) extra space (excluding the output array)?""",
                "time_limit": 1.0,
                "memory_limit": 256,
                "examples": [
                        {"input": "4\n1 2 3 4", "output": "24 12 8 6", "explanation": "Products: [2*3*4, 1*3*4, 1*2*4, 1*2*3]."},
                        {"input": "3\n-1 1 0", "output": "0 0 -1", "explanation": "Products: [1*0, -1*0, -1*1]."},
                        {"input": "2\n0 0", "output": "0 0", "explanation": "Both products are 0."},
                ],
                "testcases": [
                        {"input": "4\n1 2 3 4", "output": "24 12 8 6"},
                        {"input": "3\n-1 1 0", "output": "0 0 -1"},
                        {"input": "2\n0 0", "output": "0 0"},
                        {"input": "2\n1 2", "output": "2 1"},
                        {"input": "5\n5 2 3 4 5", "output": "120 300 200 150 120"},
                ],
        },
        {
                "title": "Search in Rotated Sorted Array",
                "description": """There is an integer array `nums` sorted in ascending order (with **distinct** values).

Prior to being passed to your function, `nums` is **possibly rotated** at an unknown pivot index `k` such that the resulting array is `[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]`.

Given the array `nums` after the possible rotation and an integer `target`, return the index of `target` if it is in `nums`, or `-1` if it is not in `nums`.

You must write an algorithm with **O(log n)** runtime complexity.""",
                "input_format": "The first line contains an integer `n`, the size of the array. The second line contains `n` space-separated integers (the rotated sorted array). The third line contains the target integer.",
                "output_format": "Print the index of the target if found, otherwise print `-1`.",
                "difficulty": "Medium",
                "tags": ["Arrays", "Binary Search"],
                "constraints": """- \\(1 \\leq n \\leq 5000\\)
- \\(-10^4 \\leq \\text{nums}[i] \\leq 10^4\\)
- All values of `nums` are **unique**.
- \\(-10^4 \\leq \\text{target} \\leq 10^4\\)""",
                "time_limit": 1.0,
                "memory_limit": 256,
                "examples": [
                        {"input": "7\n4 5 6 7 0 1 2\n0", "output": "4", "explanation": "Target 0 is at index 4."},
                        {"input": "7\n4 5 6 7 0 1 2\n3", "output": "-1", "explanation": "Target 3 is not in the array."},
                        {"input": "1\n1\n0", "output": "-1", "explanation": "Single element array, target not found."},
                ],
                "testcases": [
                        {"input": "7\n4 5 6 7 0 1 2\n0", "output": "4"},
                        {"input": "7\n4 5 6 7 0 1 2\n3", "output": "-1"},
                        {"input": "1\n1\n0", "output": "-1"},
                        {"input": "6\n5 1 2 3 4\n5", "output": "0"},
                        {"input": "6\n5 1 2 3 4\n1", "output": "1"},
                        {"input": "4\n3 4 5 1\n2", "output": "-1"},
                ],
        },
        {
                "title": "Container With Most Water",
                "description": """You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the ith line are `(i, 0)` and `(i, height[i])`.

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

**Notice** that you may not slant the container.""",
                "input_format": "The first line contains an integer `n`, the size of the array. The second line contains `n` space-separated integers representing heights.",
                "output_format": "Print a single integer — the maximum area.",
                "difficulty": "Medium",
                "tags": ["Arrays", "Two Pointers"],
                "constraints": """- \\(2 \\leq n \\leq 10^5\\)
- \\(0 \\leq \\text{height}[i] \\leq 10^4\\)""",
                "time_limit": 1.0,
                "memory_limit": 256,
                "examples": [
                        {"input": "9\n1 8 6 2 5 4 8 3 7", "output": "49", "explanation": "Max area is 49, between indices 1 and 8 (height 8 and 7, width 7)."},
                        {"input": "2\n1 1", "output": "1", "explanation": "Only two lines, area = min(1,1)*1 = 1."},
                        {"input": "4\n4 3 2 1", "output": "4", "explanation": "Max area is between 4 and 1 (height 1, width 3) or 4 and 2 (height 2, width 2)."},
                ],
                "testcases": [
                        {"input": "9\n1 8 6 2 5 4 8 3 7", "output": "49"},
                        {"input": "2\n1 1", "output": "1"},
                        {"input": "4\n4 3 2 1", "output": "4"},
                        {"input": "5\n1 3 2 5 4", "output": "12"},
                        {"input": "10\n0 1 0 2 0 3 0 4 0 5", "output": "10"},
                ],
        },
        {
                "title": "Longest Palindromic Substring",
                "description": """Given a string `s`, return the **longest palindromic substring** in `s`.""",
                "input_format": "A single line containing the string `s`.",
                "output_format": "Print the longest palindromic substring. If multiple exist, return any.",
                "difficulty": "Medium",
                "tags": ["Strings", "Dynamic Programming"],
                "constraints": """- \\(1 \\leq |s| \\leq 1000\\)
- \\(s\\) consists of only digits and English letters.""",
                "time_limit": 1.0,
                "memory_limit": 256,
                "examples": [
                        {"input": "babad", "output": "bab", "explanation": "Both 'bab' and 'aba' are valid palindromic substrings."},
                        {"input": "cbbd", "output": "bb", "explanation": "'bb' is the longest palindromic substring."},
                        {"input": "a", "output": "a", "explanation": "Single character is trivially a palindrome."},
                ],
                "testcases": [
                        {"input": "babad", "output": "bab"},
                        {"input": "cbbd", "output": "bb"},
                        {"input": "a", "output": "a"},
                        {"input": "ac", "output": "a"},
                        {"input": "abb", "output": "bb"},
                        {"input": "racecar", "output": "racecar"},
                ],
        },
        {
                "title": "Find All Duplicates in an Array",
                "description": """Given an integer array `nums` of length `n` where all the integers of `nums` are in the range `[1, n]` and each integer appears **at most twice**, return an array of all the integers that appear **twice**.

You must write an algorithm that runs in **O(n)** time and uses only **constant extra space**.""",
                "input_format": "The first line contains an integer `n`, the size of the array. The second line contains `n` space-separated integers.",
                "output_format": "Print the duplicate integers as space-separated values. If no duplicates, print nothing.",
                "difficulty": "Medium",
                "tags": ["Arrays", "Hash Table"],
                "constraints": """- \\(1 \\leq n \\leq 10^5\\)
- \\(1 \\leq \\text{nums}[i] \\leq n\\)
- Each integer appears once or twice.""",
                "time_limit": 1.0,
                "memory_limit": 256,
                "examples": [
                        {"input": "8\n4 3 2 7 8 2 3 1", "output": "2 3", "explanation": "2 and 3 appear twice."},
                        {"input": "1\n1", "output": "", "explanation": "No duplicates."},
                        {"input": "2\n1 1", "output": "1", "explanation": "1 appears twice."},
                ],
                "testcases": [
                        {"input": "8\n4 3 2 7 8 2 3 1", "output": "2 3"},
                        {"input": "1\n1", "output": ""},
                        {"input": "2\n1 1", "output": "1"},
                        {"input": "5\n5 4 3 2 1", "output": ""},
                        {"input": "10\n1 2 3 4 5 6 7 8 9 9", "output": "9"},
                ],
        },
        {
                "title": "Rotate Image",
                "description": """You are given an `n x n` 2D matrix representing an image. Rotate the image by **90 degrees** (clockwise).

You have to rotate the image **in-place**, which means you have to modify the input 2D matrix directly.

The input matrix is given as `n` rows, each with `n` space-separated integers.""",
                "input_format": "The first line contains an integer `n` (size of the matrix). The next `n` lines each contain `n` space-separated integers representing a row of the matrix.",
                "output_format": "Print the rotated matrix, with each row on a new line and the integers space-separated.",
                "difficulty": "Medium",
                "tags": ["Arrays", "Matrix"],
                "constraints": """- \\(1 \\leq n \\leq 20\\)
- \\(-1000 \\leq \\text{matrix}[i][j] \\leq 1000\\)""",
                "time_limit": 1.0,
                "memory_limit": 256,
                "examples": [
                        {"input": "3\n1 2 3\n4 5 6\n7 8 9", "output": "7 4 1\n8 5 2\n9 6 3", "explanation": "Rotate the matrix 90 degrees clockwise."},
                        {"input": "4\n5 1 9 11\n2 4 8 10\n13 3 6 7\n15 14 12 16", "output": "15 13 2 5\n14 3 4 1\n12 6 8 9\n16 7 10 11", "explanation": "90 degree rotation of a 4x4 matrix."},
                        {"input": "1\n1", "output": "1", "explanation": "Single element matrix stays the same."},
                ],
                "testcases": [
                        {"input": "3\n1 2 3\n4 5 6\n7 8 9", "output": "7 4 1\n8 5 2\n9 6 3"},
                        {"input": "4\n5 1 9 11\n2 4 8 10\n13 3 6 7\n15 14 12 16", "output": "15 13 2 5\n14 3 4 1\n12 6 8 9\n16 7 10 11"},
                        {"input": "1\n1", "output": "1"},
                        {"input": "2\n1 2\n3 4", "output": "3 1\n4 2"},
                        {"input": "3\n-1 -2 -3\n-4 -5 -6\n-7 -8 -9", "output": "-7 -4 -1\n-8 -5 -2\n-9 -6 -3"},
                ],
        },
        {
                "title": "Permutations",
                "description": """Given an array `nums` of distinct integers, return all the possible permutations. You can return the answer in **any order**.

Print each permutation on a new line, with its elements space-separated.""",
                "input_format": "The first line contains an integer `n`, the size of the array. The second line contains `n` space-separated distinct integers.",
                "output_format": "Print each permutation on a new line, with elements space-separated.",
                "difficulty": "Medium",
                "tags": ["Backtracking"],
                "constraints": """- \\(1 \\leq n \\leq 6\\)
- \\(-10 \\leq \\text{nums}[i] \\leq 10\\)
- All integers are unique.""",
                "time_limit": 1.0,
                "memory_limit": 256,
                "examples": [
                        {"input": "3\n1 2 3", "output": "1 2 3\n1 3 2\n2 1 3\n2 3 1\n3 1 2\n3 2 1", "explanation": "All 6 permutations of [1,2,3]."},
                        {"input": "2\n0 1", "output": "0 1\n1 0", "explanation": "Both permutations of [0,1]."},
                        {"input": "1\n1", "output": "1", "explanation": "Only one permutation of [1]."},
                ],
                "testcases": [
                        {"input": "3\n1 2 3", "output": "1 2 3\n1 3 2\n2 1 3\n2 3 1\n3 1 2\n3 2 1"},
                        {"input": "2\n0 1", "output": "0 1\n1 0"},
                        {"input": "1\n1", "output": "1"},
                        {"input": "3\n-1 0 1", "output": "-1 0 1\n-1 1 0\n0 -1 1\n0 1 -1\n1 -1 0\n1 0 -1"},
                        {"input": "0\n", "output": ""},
                ],
        },
        {
                "title": "Word Search",
                "description": """Given an `m x n` grid of characters `board` and a string `word`, return `true` if `word` exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

The grid is provided row by row, with each row as a continuous string.""",
                "input_format": "The first line contains two integers `m` and `n` (rows and columns). The next `m` lines each contain a string of length `n` representing a row of the board. The last line contains the word to search.",
                "output_format": "Print `true` if the word exists in the grid, otherwise print `false`.",
                "difficulty": "Medium",
                "tags": ["Backtracking", "DFS"],
                "constraints": """- \\(1 \\leq m, n \\leq 6\\)
- \\(1 \\leq |\\text{word}| \\leq 15\\)
- \\(\\text{board}\\) and \\(\\text{word}\\) consist only of lowercase and uppercase English letters.""",
                "time_limit": 1.0,
                "memory_limit": 256,
                "examples": [
                        {"input": "3 4\nABCE\nSFCS\nADEE\nABCCED", "output": "true", "explanation": "ABCCED exists in the grid."},
                        {"input": "3 4\nABCE\nSFCS\nADEE\nSEE", "output": "true", "explanation": "SEE exists in the grid."},
                        {"input": "3 4\nABCE\nSFCS\nADEE\nABCB", "output": "false", "explanation": "ABCB does not exist (cannot reuse same cell)."},
                ],
                "testcases": [
                        {"input": "3 4\nABCE\nSFCS\nADEE\nABCCED", "output": "true"},
                        {"input": "3 4\nABCE\nSFCS\nADEE\nSEE", "output": "true"},
                        {"input": "3 4\nABCE\nSFCS\nADEE\nABCB", "output": "false"},
                        {"input": "1 1\nA\nA", "output": "true"},
                        {"input": "1 1\nA\nB", "output": "false"},
                        {"input": "2 2\nAB\nCD\nAC", "output": "false"},
                ],
        },
        {
                "title": "Subsets",
                "description": """Given an integer array `nums` of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in **any order**.

Print each subset on a new line, with its elements space-separated and sorted in ascending order.""",
                "input_format": "The first line contains an integer `n`, the size of the array. The second line contains `n` space-separated distinct integers.",
                "output_format": "Print each subset on a new line, with elements space-separated and sorted. Print an empty line for the empty subset.",
                "difficulty": "Medium",
                "tags": ["Backtracking", "Bit Manipulation"],
                "constraints": """- \\(1 \\leq n \\leq 10\\)
- \\(-10 \\leq \\text{nums}[i] \\leq 10\\)
- All numbers are unique.""",
                "time_limit": 1.0,
                "memory_limit": 256,
                "examples": [
                        {"input": "3\n1 2 3", "output": "\n1\n2\n3\n1 2\n1 3\n2 3\n1 2 3", "explanation": "All 8 subsets of [1,2,3]."},
                        {"input": "1\n0", "output": "\n0", "explanation": "Two subsets: [] and [0]."},
                        {"input": "2\n-1 1", "output": "\n-1\n1\n-1 1", "explanation": "All subsets of [-1,1]."},
                ],
                "testcases": [
                        {"input": "3\n1 2 3", "output": "\n1\n2\n3\n1 2\n1 3\n2 3\n1 2 3"},
                        {"input": "1\n0", "output": "\n0"},
                        {"input": "2\n-1 1", "output": "\n-1\n1\n-1 1"},
                        {"input": "0\n", "output": ""},
                        {"input": "2\n1 2", "output": "\n1\n2\n1 2"},
                ],
        },
        {
                "title": "Coin Change",
                "description": """You are given an integer array `coins` representing coins of different denominations and an integer `amount` representing a total amount of money.

Return the **fewest number of coins** that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return `-1`.

You may assume that you have an infinite number of each kind of coin.""",
                "input_format": "The first line contains an integer `n`, the number of coin denominations. The second line contains `n` space-separated integers (coin denominations). The third line contains the target `amount`.",
                "output_format": "Print a single integer — the minimum number of coins needed, or `-1` if impossible.",
                "difficulty": "Medium",
                "tags": ["Dynamic Programming", "BFS"],
                "constraints": """- \\(1 \\leq n \\leq 12\\)
- \\(1 \\leq \\text{coins}[i] \\leq 2^{31} - 1\\)
- \\(0 \\leq \\text{amount} \\leq 10^4\\)""",
                "time_limit": 1.0,
                "memory_limit": 256,
                "examples": [
                        {"input": "3\n1 2 5\n11", "output": "3", "explanation": "11 = 5 + 5 + 1, requiring 3 coins."},
                        {"input": "1\n2\n3", "output": "-1", "explanation": "Cannot make 3 with only coin 2."},
                        {"input": "1\n1\n0", "output": "0", "explanation": "Zero amount requires zero coins."},
                ],
                "testcases": [
                        {"input": "3\n1 2 5\n11", "output": "3"},
                        {"input": "1\n2\n3", "output": "-1"},
                        {"input": "1\n1\n0", "output": "0"},
                        {"input": "3\n1 3 5\n8", "output": "2"},
                        {"input": "4\n2 5 10 25\n37", "output": "4"},
                        {"input": "1\n2\n1", "output": "-1"},
                ],
        },
        {
                "title": "Sort Colors",
                "description": """Given an array `nums` with `n` objects colored red, white, or blue, sort them **in-place** so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers `0`, `1`, and `2` to represent the color red, white, and blue respectively.

You must solve this problem without using the library's sort function.""",
                "input_format": "The first line contains an integer `n`, the size of the array. The second line contains `n` space-separated integers (each 0, 1, or 2).",
                "output_format": "Print the sorted array as space-separated integers.",
                "difficulty": "Medium",
                "tags": ["Arrays", "Sorting", "Two Pointers"],
                "constraints": """- \\(1 \\leq n \\leq 300\\)
- \\(\\text{nums}[i] \\in \\{0, 1, 2\\}\\)
- **Follow up:** Can you do it in one pass with \\(O(1)\\) space?""",
                "time_limit": 1.0,
                "memory_limit": 256,
                "examples": [
                        {"input": "6\n2 0 2 1 1 0", "output": "0 0 1 1 2 2", "explanation": "Dutch national flag problem."},
                        {"input": "3\n2 0 1", "output": "0 1 2", "explanation": "Single pass sort."},
                        {"input": "1\n0", "output": "0", "explanation": "Single element already sorted."},
                ],
                "testcases": [
                        {"input": "6\n2 0 2 1 1 0", "output": "0 0 1 1 2 2"},
                        {"input": "3\n2 0 1", "output": "0 1 2"},
                        {"input": "1\n0", "output": "0"},
                        {"input": "5\n0 0 1 1 2", "output": "0 0 1 1 2"},
                        {"input": "5\n2 2 2 2 2", "output": "2 2 2 2 2"},
                        {"input": "4\n1 0 2 1", "output": "0 1 1 2"},
                ],
        },
        {
                "title": "Daily Temperatures",
                "description": """Given an array of integers `temperatures` representing the daily temperatures, return an array `answer` such that `answer[i]` is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep `answer[i] == 0` instead.""",
                "input_format": "The first line contains an integer `n`, the number of days. The second line contains `n` space-separated integers (temperatures).",
                "output_format": "Print `n` space-separated integers representing the number of days until a warmer temperature.",
                "difficulty": "Medium",
                "tags": ["Arrays", "Monotonic Stack"],
                "constraints": """- \\(1 \\leq n \\leq 10^5\\)
- \\(30 \\leq \\text{temperatures}[i] \\leq 100\\)""",
                "time_limit": 1.0,
                "memory_limit": 256,
                "examples": [
                        {"input": "8\n73 74 75 71 69 72 76 73", "output": "1 1 4 2 1 1 0 0", "explanation": "For each day, days until a warmer temperature."},
                        {"input": "4\n30 40 50 60", "output": "1 1 1 0", "explanation": "Each day has a warmer next day except the last."},
                        {"input": "4\n90 80 70 60", "output": "0 0 0 0", "explanation": "Temperatures strictly decreasing, never warmer."},
                ],
                "testcases": [
                        {"input": "8\n73 74 75 71 69 72 76 73", "output": "1 1 4 2 1 1 0 0"},
                        {"input": "4\n30 40 50 60", "output": "1 1 1 0"},
                        {"input": "4\n90 80 70 60", "output": "0 0 0 0"},
                        {"input": "1\n100", "output": "0"},
                        {"input": "5\n50 50 50 50 50", "output": "0 0 0 0 0"},
                        {"input": "6\n40 35 45 30 38 50", "output": "2 1 3 1 1 0"},
                ],
        },
        {
                "title": "Generate Parentheses",
                "description": """Given `n` pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Print each combination on a new line.""",
                "input_format": "A single line containing an integer `n`.",
                "output_format": "Print all combinations of well-formed parentheses, one per line.",
                "difficulty": "Medium",
                "tags": ["Backtracking", "Strings"],
                "constraints": """- \\(1 \\leq n \\leq 8\\)""",
                "time_limit": 1.0,
                "memory_limit": 256,
                "examples": [
                        {"input": "3", "output": "((()))\n(()())\n(())()\n()(())\n()()()", "explanation": "All 5 valid combinations for 3 pairs of parentheses."},
                        {"input": "1", "output": "()", "explanation": "Only one valid combination."},
                        {"input": "2", "output": "(())()\n()()", "explanation": "Two valid combinations for n=2."},
                ],
                "testcases": [
                        {"input": "3", "output": "((()))\n(()())\n(())()\n()(())\n()()()"},
                        {"input": "1", "output": "()"},
                        {"input": "2", "output": "(())()\n()()"},
                        {"input": "4", "output": "(((())))\n((()()))\n((())())\n((()))()\n(()(()))\n(()()())\n(()())()\n(())(())\n(())()()\n()((()))\n()(()())\n()(())()\n()()(())\n()()()()"},
                        {"input": "0", "output": ""},
                ],
        },
        {
                "title": "Merge k Sorted Lists",
                "description": """You are given an array of `k` linked-lists, each sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

Each list is given as space-separated integers. Multiple lists are separated by an empty line indicator (a line with `-1`).""",
                "input_format": "The first line contains an integer `k`, the number of linked lists. Then for each list: the first line contains `n_i` (size), the second line contains `n_i` space-separated integers. Repeat for each of the `k` lists.",
                "output_format": "Print the merged sorted linked list as space-separated integers.",
                "difficulty": "Hard",
                "tags": ["Linked Lists", "Divide and Conquer", "Heap"],
                "constraints": """- \\(k \\geq 1\\)
- The sum of \\(n_i\\) across all lists is at most \\(10^4\\).
- \\(-10^4 \\leq \\text{Node.val} \\leq 10^4\\)
- Each list is sorted in non-decreasing order.""",
                "time_limit": 1.0,
                "memory_limit": 256,
                "examples": [
                        {"input": "3\n3\n1 4 5\n3\n1 3 4\n2\n2 6", "output": "1 1 2 3 4 4 5 6", "explanation": "Merge three sorted lists."},
                        {"input": "1\n1\n1", "output": "1", "explanation": "Single list with one element."},
                        {"input": "2\n0\n\n1\n0", "output": "0", "explanation": "One empty list and one with a single 0."},
                ],
                "testcases": [
                        {"input": "3\n3\n1 4 5\n3\n1 3 4\n2\n2 6", "output": "1 1 2 3 4 4 5 6"},
                        {"input": "1\n1\n1", "output": "1"},
                        {"input": "2\n0\n\n1\n0", "output": "0"},
                        {"input": "2\n2\n1 3\n2\n2 4", "output": "1 2 3 4"},
                        {"input": "4\n1\n-10\n2\n-5 0\n1\n5\n2\n10 20", "output": "-10 -5 0 5 10 20"},
                ],
        },
        {
                "title": "First Missing Positive",
                "description": """Given an unsorted integer array `nums`, return the smallest positive integer that is **not present** in `nums`.

You must implement an algorithm that runs in **O(n)** time and uses **O(1)** auxiliary space.""",
                "input_format": "The first line contains an integer `n`, the size of the array. The second line contains `n` space-separated integers.",
                "output_format": "Print a single integer — the smallest missing positive integer.",
                "difficulty": "Hard",
                "tags": ["Arrays", "Hash Table"],
                "constraints": """- \\(1 \\leq n \\leq 10^5\\)
- \\(-10^9 \\leq \\text{nums}[i] \\leq 10^9\\)""",
                "time_limit": 1.0,
                "memory_limit": 256,
                "examples": [
                        {"input": "4\n1 2 0", "output": "3", "explanation": "1 and 2 are present, so 3 is the smallest missing positive."},
                        {"input": "4\n3 4 -1 1", "output": "2", "explanation": "1 is present, 2 is missing."},
                        {"input": "5\n7 8 9 11 12", "output": "1", "explanation": "1 is the smallest positive integer not present."},
                ],
                "testcases": [
                        {"input": "3\n1 2 0", "output": "3"},
                        {"input": "4\n3 4 -1 1", "output": "2"},
                        {"input": "5\n7 8 9 11 12", "output": "1"},
                        {"input": "1\n1", "output": "2"},
                        {"input": "2\n-1 -2", "output": "1"},
                        {"input": "5\n1 2 3 4 5", "output": "6"},
                ],
        },
        {
                "title": "Trapping Rain Water",
                "description": """Given `n` non-negative integers representing an elevation map where the width of each bar is `1`, compute how much water it can trap after raining.""",
                "input_format": "The first line contains an integer `n`, the size of the array. The second line contains `n` space-separated integers (heights).",
                "output_format": "Print a single integer — the total units of water trapped.",
                "difficulty": "Hard",
                "tags": ["Arrays", "Two Pointers", "Dynamic Programming", "Monotonic Stack"],
                "constraints": """- \\(1 \\leq n \\leq 2 \\times 10^4\\)
- \\(0 \\leq \\text{height}[i] \\leq 10^5\\)""",
                "time_limit": 1.0,
                "memory_limit": 256,
                "examples": [
                        {"input": "12\n0 1 0 2 1 0 1 3 2 1 2 1", "output": "6", "explanation": "The elevation map traps 6 units of rainwater."},
                        {"input": "3\n4 2 3", "output": "1", "explanation": "Traps 1 unit of water."},
                        {"input": "2\n1 2", "output": "0", "explanation": "No space to trap water between two bars."},
                ],
                "testcases": [
                        {"input": "12\n0 1 0 2 1 0 1 3 2 1 2 1", "output": "6"},
                        {"input": "3\n4 2 3", "output": "1"},
                        {"input": "2\n1 2", "output": "0"},
                        {"input": "1\n0", "output": "0"},
                        {"input": "5\n5 4 3 2 1", "output": "0"},
                        {"input": "10\n0 0 0 0 0 0 0 0 0 0", "output": "0"},
                ],
        },
        {
                "title": "Sliding Window Maximum",
                "description": """You are given an array of integers `nums`, there is a sliding window of size `k` which is moving from the very left of the array to the very right. You can only see the `k` numbers in the window. Each time the sliding window moves right by one position.

Return the max of each sliding window.""",
                "input_format": "The first line contains an integer `n`, the size of the array. The second line contains `n` space-separated integers. The third line contains the integer `k` (window size).",
                "output_format": "Print the maximum of each sliding window as space-separated integers.",
                "difficulty": "Hard",
                "tags": ["Arrays", "Queue", "Sliding Window", "Monotonic Queue"],
                "constraints": """- \\(1 \\leq n \\leq 10^5\\)
- \\(-10^4 \\leq \\text{nums}[i] \\leq 10^4\\)
- \\(1 \\leq k \\leq n\\)""",
                "time_limit": 1.0,
                "memory_limit": 256,
                "examples": [
                        {"input": "8\n1 3 -1 -3 5 3 6 7\n3", "output": "3 3 5 5 6 7", "explanation": "Window positions: [1,3,-1]→3, [3,-1,-3]→3, [-1,-3,5]→5, [-3,5,3]→5, [5,3,6]→6, [3,6,7]→7."},
                        {"input": "1\n1\n1", "output": "1", "explanation": "Single element, window size 1."},
                        {"input": "4\n1 -1\n2", "output": "1", "explanation": "Window size 2 over [1,-1] gives max 1."},
                ],
                "testcases": [
                        {"input": "8\n1 3 -1 -3 5 3 6 7\n3", "output": "3 3 5 5 6 7"},
                        {"input": "1\n1\n1", "output": "1"},
                        {"input": "4\n1 -1\n2", "output": "1"},
                        {"input": "5\n5 4 3 2 1\n2", "output": "5 4 3 2"},
                        {"input": "6\n1 2 3 4 5 6\n3", "output": "3 4 5 6"},
                        {"input": "7\n-7 -8 7 5 7 1 6\n4", "output": "7 7 7 7"},
                ],
        },
        {
                "title": "Minimum Window Substring",
                "description": """Given two strings `s` and `t` of lengths `m` and `n` respectively, return the **minimum window substring** of `s` such that every character in `t` (including duplicates) is included in the window. If there is no such substring, return an empty string `""`.

The testcases will be generated such that the answer is **unique**.""",
                "input_format": "The first line contains the string `s`. The second line contains the string `t`.",
                "output_format": "Print the minimum window substring, or an empty line if no such substring exists.",
                "difficulty": "Hard",
                "tags": ["Strings", "Sliding Window", "Hash Table"],
                "constraints": """- \\(1 \\leq |s|, |t| \\leq 10^5\\)
- \\(s\\) and \\(t\\) consist of uppercase and lowercase English letters.
- **Follow up:** Could you find an algorithm that runs in \\(O(m + n)\\) time?""",
                "time_limit": 1.0,
                "memory_limit": 256,
                "examples": [
                        {"input": "ADOBECODEBANC\nABC", "output": "BANC", "explanation": "Minimum window containing A, B, and C is 'BANC'."},
                        {"input": "a\na", "output": "a", "explanation": "Single character match."},
                        {"input": "a\naa", "output": "", "explanation": "s only has one 'a' but t needs two."},
                ],
                "testcases": [
                        {"input": "ADOBECODEBANC\nABC", "output": "BANC"},
                        {"input": "a\na", "output": "a"},
                        {"input": "a\naa", "output": ""},
                        {"input": "abc\nb", "output": "b"},
                        {"input": "ab\nA", "output": ""},
                        {"input": "aa\naa", "output": "aa"},
                ],
        },
        {
                "title": "Word Ladder",
                "description": """A transformation sequence from word `beginWord` to word `endWord` using a dictionary `wordList` is a sequence of words such that:

- The first word in the sequence is `beginWord`.
- The last word in the sequence is `endWord`.
- Only one letter is different between each adjacent pair.
- Each word in the sequence must exist in `wordList`.
- `beginWord` may not be in `wordList`.

Return the **length** of the shortest transformation sequence from `beginWord` to `endWord`. If no such sequence exists, return `0`.""",
                "input_format": "The first line contains `beginWord`. The second line contains `endWord`. The third line contains an integer `n`, the size of the word list. The fourth line contains `n` space-separated words.",
                "output_format": "Print a single integer — the length of the shortest transformation sequence, or `0` if impossible.",
                "difficulty": "Hard",
                "tags": ["BFS", "Graph", "Hash Table"],
                "constraints": """- \\(1 \\leq |\\text{beginWord}| \\leq 10\\)
- \\(\\text{endWord}\\) and all words in `wordList` have the same length.
- \\(1 \\leq n \\leq 5000\\)
- All words consist of lowercase English letters.
- All words in `wordList` are unique.""",
                "time_limit": 1.0,
                "memory_limit": 256,
                "examples": [
                        {"input": "hit\ncog\n6\nhot dot dog lot log cog", "output": "5", "explanation": "Shortest transformation: hit → hot → dot → dog → cog (5 steps)."},
                        {"input": "hit\ncog\n5\nhot dot dog lot log", "output": "0", "explanation": "endWord 'cog' is not in the wordList."},
                        {"input": "a\nc\n2\nb c", "output": "2", "explanation": "a → c (only 'c' is endWord, but there is no direct path? actually a→c: a is begin, c is end. We need to go through 'b': a→b→c, length 3. Wait 2 means just a→c? Let me reconsider. The sequence: a → c requires changing one letter. If a, c differ by 1 letter (which they do), and c is in wordList, then length is 2."},
                ],
                "testcases": [
                        {"input": "hit\ncog\n6\nhot dot dog lot log cog", "output": "5"},
                        {"input": "hit\ncog\n5\nhot dot dog lot log", "output": "0"},
                        {"input": "a\nc\n2\nb c", "output": "2"},
                        {"input": "hot\ndog\n3\nhot dog dot", "output": "3"},
                        {"input": "lost\ncost\n3\nmost cost lost", "output": "3"},
                ],
        },
        {
                "title": "Largest Rectangle in Histogram",
                "description": """Given an array of integers `heights` representing the histogram's bar height where the width of each bar is `1`, return the area of the largest rectangle in the histogram.""",
                "input_format": "The first line contains an integer `n`, the number of bars. The second line contains `n` space-separated integers (heights).",
                "output_format": "Print a single integer — the maximum area of the rectangle.",
                "difficulty": "Hard",
                "tags": ["Arrays", "Monotonic Stack"],
                "constraints": """- \\(1 \\leq n \\leq 10^5\\)
- \\(0 \\leq \\text{height}[i] \\leq 10^4\\)""",
                "time_limit": 1.0,
                "memory_limit": 256,
                "examples": [
                        {"input": "6\n2 1 5 6 2 3", "output": "10", "explanation": "The largest rectangle has area 10 (bars of height 5 and 6 form a 5x2 rectangle, or height 2 bars span width 5 giving 10)."},
                        {"input": "1\n2", "output": "2", "explanation": "Single bar of height 2 gives area 2."},
                        {"input": "3\n1 2 1", "output": "3", "explanation": "Max area is 3 (height 1 spanning width 3, or height 2 at index 1 with width 1)."},
                ],
                "testcases": [
                        {"input": "6\n2 1 5 6 2 3", "output": "10"},
                        {"input": "1\n2", "output": "2"},
                        {"input": "3\n1 2 1", "output": "3"},
                        {"input": "5\n2 1 2 3 1", "output": "5"},
                        {"input": "4\n0 0 0 0", "output": "0"},
                        {"input": "7\n6 5 4 3 2 1 0", "output": "12"},
                ],
        },
        {
                "title": "Median of Two Sorted Arrays",
                "description": """Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, return **the median** of the two sorted arrays.

The overall run time complexity should be **O(log (m+n))**.""",
                "input_format": "The first line contains an integer `m`, the size of the first array. The second line contains `m` space-separated integers (sorted ascending). The third line contains an integer `n`, the size of the second array. The fourth line contains `n` space-separated integers (sorted ascending).",
                "output_format": "Print the median as a float rounded to 5 decimal places.",
                "difficulty": "Hard",
                "tags": ["Arrays", "Binary Search", "Divide and Conquer"],
                "constraints": """- \\(0 \\leq m, n \\leq 1000\\)
- \\(-10^6 \\leq \\text{nums}[i] \\leq 10^6\\)
- Both arrays are sorted in ascending order.""",
                "time_limit": 1.0,
                "memory_limit": 256,
                "examples": [
                        {"input": "2\n1 3\n1\n2", "output": "2.00000", "explanation": "Merged array [1,2,3], median is 2."},
                        {"input": "2\n1 2\n2\n3 4", "output": "2.50000", "explanation": "Merged array [1,2,3,4], median is (2+3)/2 = 2.5."},
                        {"input": "1\n0\n0\n", "output": "0.00000", "explanation": "Only one array with element 0."},
                ],
                "testcases": [
                        {"input": "2\n1 3\n1\n2", "output": "2.00000"},
                        {"input": "2\n1 2\n2\n3 4", "output": "2.50000"},
                        {"input": "1\n0\n0\n", "output": "0.00000"},
                        {"input": "0\n\n1\n1", "output": "1.00000"},
                        {"input": "2\n1 1\n2\n1 2", "output": "1.00000"},
                        {"input": "3\n1 5 9\n4\n2 3 6 7", "output": "5.00000"},
                ],
        },
        {
                "title": "Regular Expression Matching",
                "description": """Given an input string `s` and a pattern `p`, implement regular expression matching with support for:

- `'.'` Matches any single character.
- `'*'` Matches zero or more of the preceding element.

The matching should cover the **entire** input string (not partial).""",
                "input_format": "The first line contains the string `s`. The second line contains the pattern `p`.",
                "output_format": "Print `true` if the string matches the pattern, otherwise print `false`.",
                "difficulty": "Hard",
                "tags": ["Strings", "Dynamic Programming", "Recursion"],
                "constraints": """- \\(1 \\leq |s|, |p| \\leq 20\\)
- \\(s\\) contains only lowercase English letters.
- \\(p\\) contains only lowercase English letters, `'.'`, and `'*'`.
- It is guaranteed for each `'*'` that there is a preceding valid character.""",
                "time_limit": 1.0,
                "memory_limit": 256,
                "examples": [
                        {"input": "aa\na", "output": "false", "explanation": "'a' does not match the entire string 'aa'."},
                        {"input": "aa\na*", "output": "true", "explanation": "'*' means zero or more of 'a', so 'aa' matches 'a*'."},
                        {"input": "ab\n.*", "output": "true", "explanation": "'.*' means zero or more of any character, so matches 'ab'."},
                ],
                "testcases": [
                        {"input": "aa\na", "output": "false"},
                        {"input": "aa\na*", "output": "true"},
                        {"input": "ab\n.*", "output": "true"},
                        {"input": "aab\nc*a*b", "output": "true"},
                        {"input": "mississippi\nmis*is*p*.", "output": "false"},
                        {"input": "ab\n.*c", "output": "false"},
                ],
        },
        {
                "title": "Longest Valid Parentheses",
                "description": """Given a string containing just the characters `'('` and `')'`, return the length of the longest valid (well-formed) parentheses substring.""",
                "input_format": "A single line containing the string `s` consisting of `'('` and `')'` only.",
                "output_format": "Print a single integer — the length of the longest valid parentheses substring.",
                "difficulty": "Hard",
                "tags": ["Strings", "Dynamic Programming", "Stack"],
                "constraints": """- \\(0 \\leq |s| \\leq 3 \\times 10^4\\)
- \\(s\\) consists of `'('` and `')'` only.""",
                "time_limit": 1.0,
                "memory_limit": 256,
                "examples": [
                        {"input": "(()", "output": "2", "explanation": "The longest valid parentheses substring is '()'."},
                        {"input": ")()())", "output": "4", "explanation": "The longest valid parentheses substring is '()()'."},
                        {"input": "", "output": "0", "explanation": "Empty string has length 0."},
                ],
                "testcases": [
                        {"input": "(()", "output": "2"},
                        {"input": ")()())", "output": "4"},
                        {"input": "", "output": "0"},
                        {"input": "()(()", "output": "2"},
                        {"input": "((()))", "output": "6"},
                        {"input": "))))((((", "output": "0"},
                ],
        },
        {
                "title": "Basic Calculator",
                "description": """Given a string `s` representing a valid expression, implement a basic calculator to evaluate it, and return the result.

The expression may contain `'+'`, `'-'`, `'('`, `')'`, non-negative integers, and spaces.""",
                "input_format": "A single line containing the string `s` (the expression).",
                "output_format": "Print a single integer — the result of the evaluation.",
                "difficulty": "Hard",
                "tags": ["Strings", "Stack", "Math"],
                "constraints": """- \\(1 \\leq |s| \\leq 3 \\times 10^5\\)
- \\(s\\) consists of digits, `'+'`, `'-'`, `'('`, `')'`, and spaces `' '`.
- \\(s\\) represents a valid expression.
- All intermediate results fit in a 32-bit integer.""",
                "time_limit": 1.0,
                "memory_limit": 256,
                "examples": [
                        {"input": "1 + 1", "output": "2", "explanation": "Simple addition."},
                        {"input": " 2-1 + 2 ", "output": "3", "explanation": "Expression with subtraction and addition."},
                        {"input": "(1+(4+5+2)-3)+(6+8)", "output": "23", "explanation": "Expression with nested parentheses."},
                ],
                "testcases": [
                        {"input": "1 + 1", "output": "2"},
                        {"input": " 2-1 + 2 ", "output": "3"},
                        {"input": "(1+(4+5+2)-3)+(6+8)", "output": "23"},
                        {"input": "0", "output": "0"},
                        {"input": "1-( -2)", "output": "3"},
                        {"input": "2147483647", "output": "2147483647"},
                ],
        },
        {
                "title": "Maximal Rectangle",
                "description": """Given a `rows x cols` binary matrix filled with `0`'s and `1`'s, find the largest rectangle containing only `1`'s and return its area.

Each row of the matrix is given as a string of '0's and '1's.""",
                "input_format": "The first line contains two integers `rows` and `cols`. The next `rows` lines each contain a string of length `cols` consisting of '0' and '1'.",
                "output_format": "Print a single integer — the area of the largest rectangle containing only 1's.",
                "difficulty": "Hard",
                "tags": ["Arrays", "Dynamic Programming", "Monotonic Stack", "Matrix"],
                "constraints": """- \\(1 \\leq \\text{rows}, \\text{cols} \\leq 200\\)
- \\(\\text{matrix}[i][j]\\) is `'0'` or `'1'`.""",
                "time_limit": 1.0,
                "memory_limit": 256,
                "examples": [
                        {"input": "4 5\n10100\n10111\n11111\n10010", "output": "6", "explanation": "The largest rectangle of 1's has area 6 (a 2x3 rectangle)."},
                        {"input": "1 1\n0", "output": "0", "explanation": "No 1's present."},
                        {"input": "1 1\n1", "output": "1", "explanation": "Single 1 gives area 1."},
                ],
                "testcases": [
                        {"input": "4 5\n10100\n10111\n11111\n10010", "output": "6"},
                        {"input": "1 1\n0", "output": "0"},
                        {"input": "1 1\n1", "output": "1"},
                        {"input": "2 2\n11\n11", "output": "4"},
                        {"input": "3 3\n111\n111\n111", "output": "9"},
                        {"input": "3 3\n101\n010\n101", "output": "1"},
                ],
        },
        {
                "title": "Serialize and Deserialize Binary Tree",
                "description": """Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

The input is given as a level-order traversal with `null` for missing nodes.""",
                "input_format": "The first line contains an integer `n`, the number of elements. The second line contains `n` space-separated values representing the level-order traversal (use `null` for missing nodes).",
                "output_format": "Print the serialized tree as a single line containing space-separated values (level order with `null` for missing nodes).",
                "difficulty": "Hard",
                "tags": ["Trees", "Binary Tree", "Design"],
                "constraints": """- The number of nodes in the tree is in the range \\([0, 10^4]\\).
- \\(-1000 \\leq \\text{Node.val} \\leq 1000\\)
- For serialization, use level-order traversal with `null` for missing nodes.""",
                "time_limit": 1.0,
                "memory_limit": 256,
                "examples": [
                        {"input": "7\n1 2 3 null null 4 5", "output": "1 2 3 null null 4 5", "explanation": "Serialized form is the same as the input level-order."},
                        {"input": "0\n", "output": "", "explanation": "Empty tree serializes to empty string."},
                        {"input": "3\n1 null 2", "output": "1 null 2", "explanation": "Tree with only right child."},
                ],
                "testcases": [
                        {"input": "7\n1 2 3 null null 4 5", "output": "1 2 3 null null 4 5"},
                        {"input": "0\n", "output": ""},
                        {"input": "3\n1 null 2", "output": "1 null 2"},
                        {"input": "1\n-10", "output": "-10"},
                        {"input": "5\n5 4 6 null null 3 7", "output": "5 4 6 null null 3 7"},
                ],
        },
        {
                "title": "Count of Smaller Numbers After Self",
                "description": """Given an integer array `nums`, return an integer array `counts` where `counts[i]` is the number of smaller elements to the right of `nums[i]`.""",
                "input_format": "The first line contains an integer `n`, the size of the array. The second line contains `n` space-separated integers.",
                "output_format": "Print `n` space-separated integers where the ith integer is the count of smaller elements to the right of nums[i].",
                "difficulty": "Hard",
                "tags": ["Arrays", "Binary Search Tree", "Divide and Conquer", "Fenwick Tree"],
                "constraints": """- \\(1 \\leq n \\leq 10^5\\)
- \\(-10^4 \\leq \\text{nums}[i] \\leq 10^4\\)""",
                "time_limit": 1.0,
                "memory_limit": 256,
                "examples": [
                        {"input": "5\n5 2 6 1", "output": "2 1 1 0", "explanation": "To the right of 5: [2,1] → 2 smaller. To the right of 2: [1] → 1. To the right of 6: [1] → 1. To the right of 1: [] → 0."},
                        {"input": "2\n-1 -1", "output": "0 0", "explanation": "Equal numbers, none are strictly smaller."},
                        {"input": "1\n1", "output": "0", "explanation": "Single element, nothing to the right."},
                ],
                "testcases": [
                        {"input": "5\n5 2 6 1", "output": "2 1 1 0"},
                        {"input": "2\n-1 -1", "output": "0 0"},
                        {"input": "1\n1", "output": "0"},
                        {"input": "4\n3 2 1 0", "output": "3 2 1 0"},
                        {"input": "6\n2 0 1 3 0 2", "output": "3 0 0 1 0 0"},
                ],
        },
        {
                "title": "Palindrome Pairs",
                "description": """You are given a **0-indexed** array of **unique** strings `words`.

A **palindrome pair** is a pair of integers `(i, j)` such that:

- `0 <= i, j < words.length`,
- `i != j`, and
- `words[i] + words[j]` (the concatenation of the two strings) is a palindrome.

Return an array of all the palindrome pairs. Print each pair `(i, j)` as two space-separated integers on a new line.""",
                "input_format": "The first line contains an integer `n`, the number of words. The next `n` lines each contain one word.",
                "output_format": "Print each palindrome pair `(i, j)` as two space-separated integers on a new line. If no pairs exist, print nothing.",
                "difficulty": "Hard",
                "tags": ["Strings", "Hash Table", "Trie"],
                "constraints": """- \\(1 \\leq n \\leq 5000\\)
- \\(0 \\leq |words[i]| \\leq 300\\)
- \\(words[i]\\) consists of lowercase English letters.
- All strings are unique.""",
                "time_limit": 1.0,
                "memory_limit": 256,
                "examples": [
                        {"input": "4\nabcd\ndcba\nlls\ns", "output": "0 1\n1 0\n3 2\n2 3", "explanation": "Pairs: (abcd,dcba), (dcba,abcd), (s,lls), (lls,s) form palindromes."},
                        {"input": "2\nbat\ntab", "output": "0 1\n1 0", "explanation": "bat + tab = battab (palindrome), tab + bat = tabbat (palindrome)."},
                        {"input": "3\nabc\ndef\nghi", "output": "", "explanation": "No pair forms a palindrome."},
                ],
                "testcases": [
                        {"input": "4\nabcd\ndcba\nlls\ns", "output": "0 1\n1 0\n3 2\n2 3"},
                        {"input": "2\nbat\ntab", "output": "0 1\n1 0"},
                        {"input": "3\nabc\ndef\nghi", "output": ""},
                        {"input": "1\na", "output": ""},
                        {"input": "2\na\n", "output": "0 1"},
                        {"input": "2\nab\na", "output": ""},
                ],
        },
]


class Command(BaseCommand):
    help = "Seed the database with DSA problems, test cases, and examples"

    def handle(self, *args, **options):
        tag_cache = {}

        for pdata in problems_data:
            tags = []
            for tname in pdata["tags"]:
                if tname not in tag_cache:
                    tag, _ = Tag.objects.get_or_create(name=tname)
                    tag_cache[tname] = tag
                tags.append(tag_cache[tname])

            problem, created = Problem.objects.get_or_create(
                title=pdata["title"],
                defaults={
                    "description": pdata["description"],
                    "input_format": pdata.get("input_format", ""),
                    "output_format": pdata.get("output_format", ""),
                    "difficulty": pdata["difficulty"],
                    "constraints": pdata.get("constraints", ""),
                    "time_limit": pdata.get("time_limit", 1.0),
                    "memory_limit": pdata.get("memory_limit", 256),
                },
            )
            if not created:
                problem.description = pdata["description"]
                problem.input_format = pdata.get("input_format", "")
                problem.output_format = pdata.get("output_format", "")
                problem.difficulty = pdata["difficulty"]
                problem.constraints = pdata.get("constraints", "")
                problem.time_limit = pdata.get("time_limit", 1.0)
                problem.memory_limit = pdata.get("memory_limit", 256)
                problem.save()
            problem.tags.set(tags)
            problem.save()

            for i, ex in enumerate(pdata.get("examples", [])):
                Example.objects.get_or_create(
                    problem=problem,
                    input=ex["input"],
                    output=ex["output"],
                    defaults={"explanation": ex.get("explanation", "")},
                )

            for tc in pdata.get("testcases", []):
                TestCases.objects.get_or_create(
                    problem=problem,
                    input_data=tc["input"],
                    output_data=tc["output"],
                )

            status = "Created" if created else "Already exists"
            self.stdout.write(f"{status}: {problem.title} ({problem.difficulty})")
