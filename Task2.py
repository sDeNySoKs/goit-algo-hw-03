import random 

def get_numbers_ticket(min, max, quantity):
    if min < 1 or max > 1000: #перевіряємо обмеження
        return []
    else:
        return sorted(random.sample(range(min, max + 1), quantity))  # Основна функція


