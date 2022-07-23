n_terms = int(input("How many terms the user wants to print: "))
n_1 = 0
n_2 = 1
count = 0
fib = []
if n_terms <= 0:
    print("Please enter a positive integer, the given number is not valid")
elif n_terms == 1:
    fib.append(n_1)
elif n_terms >= 2:
    while count < n_terms:
        fib.append(n_1)
        nth = n_1 + n_2
        n_1 = n_2
        n_2 = nth
        count += 1
print(f'The Fibonacci sequence of the numbers up to {n_terms} is : {fib}')
