def calculate_unique_values(cases):
    results = []
    
    for n, coins in cases:
        possible_values = set()
        
        for coin in coins:
            possible_values.update({v + coin for v in possible_values})
            possible_values.add(coin)
        
        results.append(len(possible_values))
    
    return results

cases = [
    (7, [3, 8, 1, 6, 4, 7, 3, 10]),
    (3, [8, 1, 10]),
    (3, [1, 3, 10])
]

print(calculate_unique_values(cases))