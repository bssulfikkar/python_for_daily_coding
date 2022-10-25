nums = [1, 2, 3]

# for num in nums:
#     print(num)
# print(dir(nums))
# i_nums = nums.__iter__()
# i_nums = iter(nums)
# print(i_nums)
# print(dir(i_nums))
# print(next(i_nums))
# print(next(i_nums))
# print(next(i_nums))
# print(next(i_nums))
# if an object has module __iter__ then its an iterable
# print(next(nums))
# if an object has modules __next__ and __iter__ then its an iterator(object with a state
# which remembers its position during iteration  in an iterable
# while True:
#     try:
#         item = next(i_nums)
#         print(item)
#     except StopIteration:
#         break
# iteration iterable
# class MyRange:
#     def __init__(self, start, end):
#         self.value = start
#         self.end = end
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.value >= self.end:
#             raise StopIteration
#         current = self.value
#         self.value += 1
#         return current


# nums = MyRange(1, 10)
#
# for num in nums:
#     print(num)
#
# print(next(nums))
# print(next(nums))
# print(next(nums))
# print(next(nums))
# print(next(nums))
# print(next(nums))
# print(next(nums))
# print(next(nums))
# print(next(nums))

# generator are iterators
# def my_range(start, end):
#     current = start
#     while current < end:
#         yield current
#         current += 1
#
#
# nums = my_range(1, 10)

# for num in nums:
#     print(num)

#
# print(next(nums))
# print(next(nums))
# print(next(nums))
# print(next(nums))
# print(next(nums))
# print(next(nums))
# print(next(nums))
# print(next(nums))
# print(next(nums))

# infinite loop, without an end value or limit(iterators can go in infinite loops)

# def my_range(start):
#     current = start
#     while True:
#         yield current
#         current += 1
#
#
# nums = my_range(1)
#
# for num in nums:
#     print(num)
