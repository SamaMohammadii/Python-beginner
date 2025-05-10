number = 2
prime_numbers = []
while number <= 100:
    is_prime = True
    for i in range (2, int(number ** 0.5) + 1):
        if number % i == 0:
            is_prime = False
            break
    if is_prime:
        prime_numbers.append(number)
    number += 1

print(prime_numbers)

        




