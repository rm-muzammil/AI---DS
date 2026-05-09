

    
# def decorator_function(func):
#     def wrapper():
#         print("Before function")

#         func()

#         print("After function")
        

#     return wrapper


# @decorator_function
# def greet():
#     print("Hello")
    
# @decorator_function
# def farewell():
#     print("Goodbye")
    
# greet()
# farewell()

# def logger(func):
#     def wrapper(*args, **kwargs):
#         print(f"Running function: {func.__name__}")

#         result = func(*args, **kwargs)

#         print("Function finished")

#         return result

#     return wrapper

# @logger
# def greet(name):
#     print(f"Hello {name}")

# greet("Muzammil")

# @logger
# def add(a, b):
#     print(a + b)

# add(5, 10)

import time

def log_execution(func):
    def wrapper(*args, **kwargs):
        print(f"\nExecuting: {func.__name__}")

        start = time.time()

        result = func(*args, **kwargs)

        end = time.time()

        print(f"Execution time: {end - start:.4f} sec")

        return result

    return wrapper

@log_execution
def process_data():
    total = 1

    for i in range(340578784):
        total *= i

    print("Processing complete with total:", total)

process_data()