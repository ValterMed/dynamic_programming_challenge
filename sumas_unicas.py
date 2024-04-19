def count_unique_sums(coins):
    unique_sums = set()
    unique_sums.add(0)
    
    for coin in coins:
        temp_sums = set(unique_sums)
        for value in temp_sums:
            unique_sums.add(value + coin)
    return len(unique_sums) - 1

def main():
    t = int(input('Enter the number of cases: '))
    
    list_all_uniquesums = []
    for _ in range(t):
        n = int(input(f'Provide the number of coins for case {_+1}: '))
        coins = list(map(int, input('Enter the value of each coin separated by a comma: ').split(',')))
        
        sum_unique = count_unique_sums(coins)
        print(f'The number of unique sums for case {_+1} is: ', sum_unique)
        
        list_all_uniquesums.append(sum_unique)

    print('The results were: ',list_all_uniquesums)

main()

