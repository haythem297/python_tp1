def generate_fibonacci(n):
    fibonacci_sequence = []
    a, b = 0, 1
    while len(fibonacci_sequence) < n:
        fibonacci_sequence.append(a)
        a, b = b, a + b
    return fibonacci_sequence

# Specify the number of terms you want
n = 10
result = generate_fibonacci(n)
print(result)
