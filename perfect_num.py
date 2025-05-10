user_input = int(input("Enter a number: "))
Divisors = []
for i in range(1, user_input):
    if user_input % i == 0 and i < user_input:
        Divisors.append(i)
print (f"\'{user_input}\' is perfect number and divisors of it are {Divisors}")
print (f"Summation of divisors is {sum(Divisors)}")