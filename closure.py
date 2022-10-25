# def outer_func():
#     message = 'Hi'
#
#     def inner_func():
#         print(message)
#
#     return inner_func()
#
#
# outer_func()


# def outer_func():
#     message = 'Hi'
#
#     def inner_func():
#         print(message)
#
#     return inner_func
#
#
# my_func = outer_func()
# print(my_func.__name__)
# my_func()

def outer_func(msg):
    def inner_func():
        print(msg)

    return inner_func


hi_func = outer_func('Hi!')
hello_func = outer_func('Hello!')
hi_func()
hello_func()