from typing import Generator

# Creating an infinity Fibonacci iterator
class InfinityFibonacci:

    def __init__(self):
        self._start = 0
        self._next = 1

    def __iter__(self):
        return self

    def __next__(self):
        fibonacci = self._start
        self._start, self._next = self._next, self._start + self._next
        return fibonacci


fibo = InfinityFibonacci()


# for numbers in range(10):   # printing 10 fibonacci numbers
#     print(next(fibo))


# --------------------------------------------------------------------------------------------------------

# Creating an infinity Fibonacci generator

def infinity_fibonacci_generator() -> Generator[int]:
    """Generate an infinite sequence of Fibonacci numbers."""
    current, next_num = 0, 1
    while True:
        yield current
        current, next_num = next_num, next_num + current


fibo_gen = infinity_fibonacci_generator()


#
# for i in range(10):
#     print(next(fibo_gen))


# --------------------------------------------------------------------------------------------------------

def programming_language_gen() -> Generator[str]:
    """A generator that yields a programming language it receives."""
    while True:
        language: str = yield
        yield language


a = programming_language_gen()


# next(a)
# print(a.send('Python'))
# next(a)
# print(a.send('Java'))

def using_throw():
    try:
        for language in ['python', 'java', 'c++']:
            next(a)  # Move to the point where it expects to receive a value
            print(a.send(language))  # # Send value to the generator and print its
        a.throw(ValueError('Something went wrong'))  # Throw an exception inside the generator
    except StopIteration:
        print('The end of the generator was reached.')
    except Exception as e:
        print(e)


# using_throw()  # run function


# ------------------------------------------------------------------------------------------------------

# close example
def using_close():
    while True:
        count = 0
        for lang in ['python', 'go', 'java', 'c++']:
            count += 1
            next(a)
            print(a.send(lang))
            if count == 3:
                a.close()  # it helps to stop printing after 3rd print
                print('The generator was closed.')

# using_close()  # run function
