import time


def accepts(*types):
    args_of_types = types

    def decorator(func):
        def check_types(args):
            for i in range(0, len(args)):
                if type(args[i]) is not args_of_types[i]:
                    raise TypeError(f'Argument {i} of {func.__name__} is not {type}')

        def result(*args):
            check_types(args)
            return func(*args)
        return result
    return decorator


# @accepts(str, int)
# def deposit(name, money):
    # print("deposit {} sends {} $!".format(name, money))


def performance(filename):
    def decorator(func):
        def log_time():
            start = time.time()
            return_value = func()
            end = time.time()
            time_taken = end - start
            with open(filename, 'a') as f:
                f.write(f'{func.__name__} was called and took {time_taken:.2f} seconds to complete\n')
            return return_value
        return log_time
    return decorator


# @performance('log.txt')
# def something_heavy():
    # time.sleep(2)
    # return "I am done!"


def silence(filename):
    def decorator(func):
        def check_type(value):
            if value >= 50:
                with open(filename, 'w') as f:
                    f.write(f"Calling {func.__name__} raised an error - ValueError: 'Omg'. " +
                            f"Provided argument: {value}\n")
            return None
        return check_type
    return decorator


# @silence('errors.txt')
# def foo(x):
    # if x > 50:
    # raise ValueError('Omg.')
