# import sys

# list_data = [i for i in range(9100000)]
# gen_data = (i for i in range(9100000))

# print("List size:", sys.getsizeof(list_data))
# print("Generator size:", sys.getsizeof(gen_data))

def get_numbers():
    for i in range(20):
        yield i
        
def filter_even(numbers):
    for num in numbers:
        if num % 2 == 0:
            yield num
            
def square(numbers):
    for num in numbers:
        yield num * num
        
nums = get_numbers()
evens = filter_even(nums)
squared = square(evens)

for value in squared:
    print(value)
    
squares = (x*x for x in range(10))
for square in squares:
    print(square)