import itertools

# counter = itertools.count()

# print(next(counter))
# print(next(counter))
# print(next(counter))

# data = [100, 200, 300, 400]

# daily_data = zip(itertools.count(), data)

# print(next(daily_data))
# print(next(daily_data))
# print(next(daily_data))
# print(next(daily_data))

# daily_data = list(zip(itertools.count(), data))
#
# print(daily_data)

# counter = itertools.count(5)
#
# print(next(counter))
# print(next(counter))
# print(next(counter))

# counter = itertools.count(start=5, step=5)
#
# print(next(counter))
# print(next(counter))
# print(next(counter))

# counter = itertools.count(start=5, step=-2.5)
# print(next(counter))
# print(next(counter))
# print(next(counter))

# data = [100, 200, 300, 400]
#
# daily_data = list(zip(range(10), data))
# print(daily_data)

# data = [100, 200, 300, 400]
#
# daily_data = list(itertools.zip_longest(range(10), data))
# print(daily_data)

# counter = itertools.cycle([1, 2, 3])
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))


# counter = itertools.cycle(('ON', 'OFF'))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))

# counter = itertools.repeat(2)
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))


# counter = itertools.repeat(2, times=3)
# print(next(counter))
# print(next(counter))
# print(next(counter))


# squares = map(pow, range(10), itertools.repeat(2))
#
# print(list(squares))


# squares = itertools.starmap(pow, [(0, 2), (1, 2), (2, 2)])
#
# print(list(squares))

squares = itertools.starmap(pow, [(0, 2), (1, 2), (2, 2)])

print(list(squares))