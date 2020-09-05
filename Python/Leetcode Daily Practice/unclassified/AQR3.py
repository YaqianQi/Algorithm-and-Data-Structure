"""
Given an array of unique integers numbers, your task is to return all element pairs with the minimal absolute difference, in ascending order. Lower number in the pairs should come first.

Formally, return an array of pairs (arrays of size 2), of the form [i, j], where i is less than j. The pairs themselves should also be listed in ascending order within the resulting array, ordered firstly by the first number in pair, and in case of a tie by the second number.

NOTE: The pairs are not necessarily adjacent elements in numbers.

Example

For numbers = [6, 2, 4, 10], the output should be closestNumbers(numbers) = [[2, 4], [4, 6]].

The minimal absolute difference between any two elements in the array is 2, and there are two pairs with this difference: (a[0], a[2]) = (6, 4) and (a[1], a[2]) = (2, 4).
After ordering the numbers in each pair, they will be ordered as follows: [(4, 6), (2, 4)].
After ordering the pairs themselves, they will be ordered as follows: [(2, 4), (4, 6)].

For numbers = [4, 2, 1, 3], the output should be closestNumbers(numbers) = [[1, 2], [2, 3], [3, 4]].

The minimal absolute difference between any two elements in the array is 1, and there are three pairs with this difference: (a[0], a[3]) = (4, 3), (a[1], a[3]) = (2, 3), and (a[1], a[2]) = (2, 1).
After ordering the numbers in each pair, they will be ordered as follows: [(3, 4), (2, 3), (1, 2)].
After ordering the pairs themselves, they will be ordered as follows: [(1, 2), (2, 3), (3, 4)].

For numbers = [4, -2, -1, 3], the output should be closestNumbers(numbers) = [[-2, -1], [3, 4]].

The minimal absolute difference between any two elements in the array is 1, and there are two pairs with this difference: (a[0], a[3]) = (4, 3) and (a[1], a[2]) = (-2, -1).
After ordering the numbers in pairs, and the pairs themselves, they will look like this: [(-2, -1), (3, 4)].

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.integer numbers

An array containing unique integers.

Guaranteed constraints:
1 ≤ numbers.length ≤ 105,
-2 · 106 ≤ numbers[i] ≤ 2 · 106.

[output] array.array.integer

An array of pairs with the minimal absolute difference. The numbers in pairs and the pairs themselves should be sorted in ascending order.
"""