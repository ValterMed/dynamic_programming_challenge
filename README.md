
# Dynamic Programming Challenge

This Python script implements a function to count how many different positive values can be obtained by summing the coin values provided in each case.

## Function Description

The function `calcular_valores(casos)` takes a list of cases, where each case consists of an integer `n` representing the number of coins, and a list `monedas` representing the values of the coins. It calculates and returns a list of integers, each representing the count of different positive values that can be obtained by summing the coin values in the corresponding case.

## Input Format

The input `casos` is a list of tuples, where each tuple contains:
- An integer `n` representing the number of coins.
- A list `monedas` containing `n` integers representing the values of the coins.

## Output Format

The function returns a list of integers, where each integer represents the count of different positive values that can be obtained by summing the coin values in the corresponding case.

## Example

```python
casos = [
    (7, [3, 8, 1, 6, 4, 7, 3, 10]),
    (3, [8, 1, 10]),
    (3, [1, 3, 10])
]

print(calcular_valores(casos))



