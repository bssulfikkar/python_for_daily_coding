# condition = True
#
# if condition:
#     x = 1
# else:
#     x = 0
#
# print(x)


# condition = False
#
# if condition:
#     x = 1
# else:
#     x = 0
#
# print(x)

# efficient
# condition = True
# x = 1 if condition else 0
# print(x)


# num1 = 10000000000
# num2 = 100000000
# total = num1 + num2
# print(total)

# efficient way of displaying and printing numbers
# num1 = 10_000_000_000
# num2 = 100_000_000
# total = num1 + num2
# print(f'{total:,}')

# f = open('test_file.txt', 'r')
# file_contents = f.read()
# f.close()
#
# words = file_contents.split(' ')
# word_count = len(words)
# print(word_count)

# efficient way is to use context managers
# with open('test_file.txt', 'r') as f:
#     file_contents = f.read()
# words = file_contents.split(' ')
# word_count = len(words)
# print(word_count)

# names = ['name1', 'name2', 'name3', 'name4']
# index = 0
# for name in names:
#     print(index, name)
#     index += 1

# efficient way is to use enumerate
# names = ['name1', 'name2', 'name3', 'name4']
# for index, name in enumerate(names):
#     print(index, name)

# names = ['name1', 'name2', 'name3', 'name4']
# for index, name in enumerate(names, start=1):
#     print(index, name)


# names = ['Peter', 'Clark', 'Wade', 'Bruce']
# heroes = ['spiderman', 'superman', 'deadpool', 'batman']
#
# for index, name in enumerate(names):
#     hero = heroes[index]
#     print(f'{name} is actually {hero}')

# efficient way here to use is zip to loop over two lists
# names = ['Peter', 'Clark', 'Wade', 'Bruce']
# heroes = ['spiderman', 'superman', 'deadpool', 'batman']
#
# for name, hero in zip(names, heroes):
#     print(f'{name} is actually {hero}')


# names = ['Peter', 'Clark', 'Wade', 'Bruce']
# heroes = ['spiderman', 'superman', 'deadpool', 'batman']
# universes = ['Marvel', 'DC', 'Marvel', 'DC']
# for name, hero, universe in zip(names, heroes, universes):
#     print(f'{name} is actually {hero} from {universe}')


# names = ['Peter', 'Clark', 'Wade', 'Bruce']
# heroes = ['spiderman', 'superman', 'deadpool', 'batman']
# universes = ['Marvel', 'DC', 'Marvel', 'DC']
# for value in zip(names, heroes, universes):
#     print(value)

# unpacking
# a, b = (1, 2)
# print(a)
# print(b)

# if to ignore the second value use underscore
# a, _ = (1, 2)
# print(a)

# a, b, *c = (1, 2, 3, 4, 5)
# print(a)
# print(b)
# print(c)

# a, b, *_ = (1, 2, 3, 4, 5)
# print(a)
# print(b)

# a, b, *c, d = (1, 2, 3, 4, 5)
# print(a)
# print(b)
# print(c)
# print(d)

# a, b, *c, d = (1, 2, 3, 4, 5, 6, 7)
# print(a)
# print(b)
# print(c)
# print(d)

# a, b, *_, d = (1, 2, 3, 4, 5, 6, 7)
# print(a)
# print(b)
# print(d)

# setting and getting attributes on certain objects
# class Person:
#     pass
#
# person = Person()

# person.first = "First"
# person.last = "Last"
# print(person.first)
# print(person.last)

# class Person:
#     pass
#
# person = Person()
#
# first_key = "first"
# first_value = "Corey"
#
# setattr(person, 'first', 'Corey')
#
# print(person.first)

# class Person:
#     pass
#
#
# person = Person()
#
# first_key = "first"
# first_value = "Corey"
#
# setattr(person, first_key, first_value)
# print(person.first)
#
# first = getattr(person, first_key)
# print(first)


# class Person:
#     pass
#
#
# person = Person()
#
# person_info = {'first': 'Corey', 'last': 'Schafer'}
#
# for key, value in person_info.items():
#     setattr(person, key, value)
#
# print(person.first)
# print(person.last)
#
# for key in person_info.keys():
#     print(getattr(person, key))


# inputting secret information

# username = input('Username:')
# password = input('Password:')
#
# print('Logging In...')

# efficient way is to use getpass
# from getpass import getpass
# username = input('Username:')
# password = getpass('Password:')
#
# print('Logging In...')

# python -m search for the module in sys.path and run th module
# dir(datetime)
# help(smtpd)