# def outer_function():
#     message = 'Hi'
#
#     def inner_function():
#         print(message)
#
#     return inner_function()
#
#
# outer_function()

# def outer_function():
#     message = 'Hi'
#
#     def inner_function():
#         print(message)
#
#     return inner_function
#
#
# my_func = outer_function()
# my_func()

# def outer_function(msg):
#     def inner_function():
#         print(msg)
#     return inner_function
#
#
# hi_func = outer_function('Hi1')
# hello_func = outer_function('Hello!')
#
# hi_func()
# hello_func()


# def decorator_function(original_function):
#     def wrapper_function():
#         print('wrapper executed before {}'.format(original_function.__name__))
#         return original_function()
#
#     return wrapper_function
#
#
# def display():
#     print('display function ran')
#
#
# decorated_display = decorator_function(display)
#
# decorated_display()

# def decorator_function(original_function):
#     def wrapper_function(*args, **kwargs):
#         print('wrapper executed before {}'.format(original_function.__name__))
#         return original_function(*args, **kwargs)
#
#     return wrapper_function

# @decorator_function
# def display():
#     print('display function ran')
#
#
# display()
#
#
# @decorator_function
# def display_info(name, age):
#     print('display_info ran with arguments ({}, {})'.format(name, age))
#
#
# display_info('test', 0)


# class DecoratorClass(object):
#     def __init__(self, original_function):
#         self.original_function = original_function
#
#     def __call__(self, *args, **kwargs):
#         print('call method executed before {}'.format(self.original_function.__name__))
#         return self.original_function(*args, **kwargs)
#
#
# @DecoratorClass
# def display():
#     print('display function ran')
#
#
# display()
#
#
# @DecoratorClass
# def display_info(name, age):
#     print('display_info ran with arguments ({}, {})'.format(name, age))
#
#
# display_info('test', 0)



# def my_logger(orig_func):
#     import logging
#     logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)
#
#     def wrapper(*args, **kwargs):
#         logging.info('Run with args: {} and kwargs: {}'.format(args, kwargs))
#         return orig_func(*args, **kwargs)
#
#     return wrapper


# @my_logger
# def display_info(name, age):
#     print('display_info ran with arguments ({}, {})'.format(name, age))
#
#
# display_info('test', 0)
# display_info('test1', 1)

# def my_logger(orig_func):
#     import logging
#     logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)
#
#     def wrapper(*args, **kwargs):
#         logging.info('Run with args: {} and kwargs: {}'.format(args, kwargs))
#         return orig_func(*args, **kwargs)
#
#     return wrapper
#
#
# def my_timer(orig_func):
#     import time
#
#     def wrapper(*args, **kwargs):
#         t1 = time.time()
#         result = orig_func(*args, **kwargs)
#         t2 = time.time() - t1
#         print('{} ran in : {} sec'.format(orig_func.__name__, t2))
#         return result
#
#     return wrapper
#
#
# @my_logger
# @my_timer
# def display():
#     import time
#     time.sleep(1)
#     print('display function ran')


#display = my_logger(my_timer(display))
#print(display.__name__)
#display()


from functools import wraps


def my_logger(orig_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        logging.info('Run with args: {} and kwargs: {}'.format(args, kwargs))
        return orig_func(*args, **kwargs)

    return wrapper


def my_timer(orig_func):
    import time

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in : {} sec'.format(orig_func.__name__, t2))
        return result

    return wrapper


@my_logger
@my_timer
def display():
    import time
    time.sleep(1)
    print('display function ran')

#display = my_timer(display)
#print(display.__name__)
display()