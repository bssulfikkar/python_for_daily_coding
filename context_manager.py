# f = open('sample.txt', 'w')
# f.write('I am testing writing words to a file')
# f.close

# with open('context_manager_sample.txt', 'w') as f:
#     f.write('I am testing again writing words into a file by using context manager')


# class OpenFile:
#     def __init__(self, filename, mode):
#         self.filename = filename
#         self.mode = mode
#
#     def __enter__(self):
#         self.file = open(self.filename, self.mode)
#         return self.file
#
#     def __exit__(self, exec_type, exec_val, traceback):
#         self.file.close()
#
#
# with OpenFile('context_manager_class.txt', 'w') as f:
#     f.write('Testing if CM class is working')
#
# print(f.closed)

# from contextlib import contextmanager
#
#
# @contextmanager
# def open_file(file, mode):
#     f = open(file, mode)
#     yield f
#     f.close()
#
#
# with open_file('context_manager_function.txt', 'w') as f:
#     f.write('Testing if context manager function is working')
#
# print(f.closed)

# from contextlib import contextmanager
#
#
# @contextmanager
# def open_file(file, mode):
#     try:
#         f = open(file, mode)
#         yield f
#     finally:
#         f.close()
#
#
# with open_file('context_manager_function.txt', 'w') as f:
#     f.write('Testing if context manager function is working')
#
# print(f.closed)


# import os
# from contextlib import contextmanager
# cwd = os.getcwd()
# os.chdir('Sample_One_Dir')
# print(os.listdir())
# os.chdir(cwd)
#
# cwd = os.getcwd()
# os.chdir('Sample_Two_Dir')
# print(os.listdir())
# os.chdir(cwd)

import os
from contextlib import contextmanager


@contextmanager
def list_change_dir(destination):
    try:
        cwd = os.getcwd()
        os.chdir(destination)
        yield
    finally:
        os.chdir(cwd)


with list_change_dir('Sample_One_Dir'):
    print(os.listdir())

with list_change_dir('Sample_Two_Dir'):
    print(os.listdir())
    