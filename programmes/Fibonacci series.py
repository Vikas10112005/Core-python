n_terms = 10
a, b = 0, 1

print("Fibonacci Series:")
for _ in range(n_terms):
    print(a, end=" ")
    a, b = b, a + b 