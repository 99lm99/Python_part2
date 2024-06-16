def generate_bonus_dict(names, rate, bonus_percentages):
    """
    One-liner generator to create a dictionary where names are keys and bonus amounts are values.
    """
    return {name: rate * float(percentage.rstrip('%')) / 100 for name, rate, percentage in zip(names, rate, bonus_percentages)}


names = ['Alice', 'Bob', 'Charlie']
rate = [1000, 1500, 800]
bonus_percentages = ['10.25%', '8.75%', '12.50%']

bonus_dict = generate_bonus_dict(names, rate, bonus_percentages)
print(bonus_dict)






def fibonacci_generator():
    """
    Generator function to generate Fibonacci numbers indefinitely.
    """
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Пример 
fib_gen = fibonacci_generator()
for i in range(10):
    print(next(fib_gen))

