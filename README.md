# Number Guessing Game

This repository contains Python scripts implementing two approaches to guess a number within a specified range: an iterative approach and a recursive approach.

## Iterative Approach

### Description
The iterative approach repeatedly divides the search range in half until it finds the correct number. It utilizes a while loop to iterate through the guessing process.

### Files
- `guess_number_iterative.py`: Python script containing the iterative implementation of the number guessing game.

### Usage
1. Run the script `guess_number_iterative.py`.
2. Enter the value of `n`, which represents the upper bound of the initial range.
3. Enter the number to be guessed.
4. The program will print each guess made and finally reveal the guessed number along with the number of iterations it took to find it.

## Recursive Approach

### Description
The recursive approach employs a recursive function to perform the guessing process. It recursively calls itself, adjusting the range and making guesses until it finds the correct number.

### Files
- `guess_number_recursive.py`: Python script containing the recursive implementation of the number guessing game.

### Usage
1. Run the script `guess_number_recursive.py`.
2. Enter the value of `n`, which represents the upper bound of the initial range.
3. Enter the number to be guessed.
4. The program will print each guess made and finally reveal the guessed number along with the number of recursive calls it took to find it.

## Main Script

### Description
The main script `main.py` provides an interface to choose between the iterative and recursive approaches and test the number guessing game.

### Files
- `main.py`: Python script containing the main interface to run the number guessing game.

### Usage
1. Run the script `main.py`.
2. Follow the prompts to choose between the iterative and recursive approaches.
3. Enter the required inputs (upper bound of the range and the number to guess).
4. The program will execute the chosen approach and display the guessed number along with relevant details.

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



