def fibonacci(n):
    #Base Case
    if n == 0:
        return 0
    if n == 1:
        return 1
    #Recursive Case
    return fibonacci(n - 1) + fibonacci(n - 2)

#test case
test_variable = fibonacci(10)
print(test_variable)
