# Dynamic Programming Challenge

## Problem Statement
![Problem Image](https://i.ibb.co/r5V9d7Z/Ejercicio-programacion-dinamica.jpg)

## Solution
To solve this challenge have developed the following fuction:

~~~python
def count_unique_sums(coins):
    unique_sums = set()
    unique_sums.add(0)

    for coin in coins:
        temp_sums = set(unique_sums)
        for value in temp_sums:
            unique_sums.add(value + coin)
    
    return len(unique_sums) - 1
~~~

1. As you can see it takes a list as an argument, that list contains the value of each coin.
2. Then it creates a set to store the unique values.
3. We add the 0 value as first item.
4. Then we use a for loop to iterate over each coin.
5. After that we create a temporary copy of the `unique_sums set`.
6. Then using a for loop to iterate over each value in the temporary list and adding the current coin to all of them.
7. In the end each sum is stored in the set and returns the length of the set.

~~~
def main():
    t = int(input('Enter the number of cases: '))
    
    list_all_uniquesums = []
    for _ in range(t):
        n = int(input(f'Provide the number of coins {_+1}: '))
        coins = list(map(int, input('Enter the value of each coin separated by a comma').split(',')))
        
        sum_unique = count_unique_sums(coins)
        list_all_uniquesums.append(sum_unique)

    print(list_all_uniquesums)
~~~
- This is the function main which controls the flow of the program.
-  You need to provide the amount of cases you want to solve.
- Then we create an empty list to save the value of each case.
- Then using a foor loop it iterates the amount of cases we provided.
- It will ask you to input the amount of coins and then you will input the value of each coin separated by a comma.
- Then the function `count_unique_sums()` is called and as argument it takes the list that contains the value of each coin.
- Finally, it stores each result in a list and print it.

