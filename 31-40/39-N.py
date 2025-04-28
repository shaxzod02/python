import random

def select_random_numbers(n, m):

    if n > m:
        return "n soni m sonidan kichik bolsin"
    
    select_numbers = random.sample(range(1, m+1), n)
    return select_numbers


print(select_random_numbers(8, 10))
print(select_random_numbers(10, 10))