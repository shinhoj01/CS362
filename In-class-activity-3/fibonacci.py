
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return(fibonacci(n-1)+fibonacci(n-2))

def factorial(n):
    if n <= 1:
        return n
    else:
        return(n*factorial(n-1))
