import logging
import logging_emp

# logging.basicConfig(filename='calc.log', level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(levelname)s:%(asctime)s:%(name)s:%(message)s')
file_handler = logging.FileHandler('calc.log')
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.ERROR)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)


def add(x, y):
    return x * y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        logger.exception('Tried to Divide by zero')
    else:
        return result


num1 = 20
num2 = 0

add_result = add(num1, num2)
# print('Add: {} + {} = {}'.format(num1, num2, add_result))
# logging.debug('Add: {} + {} = {}'.format(num1, num2, add_result))
# logging.warning('Add: {} + {} = {}'.format(num1, num2, add_result))
logger.debug('Add: {} + {} = {}'.format(num1, num2, add_result))

sub_result = subtract(num1, num2)
# print('Sub: {} - {} = {}'.format(num1, num2, sub_result))
# logging.debug('Sub: {} - {} = {}'.format(num1, num2, sub_result))
# logging.warning('Sub: {} - {} = {}'.format(num1, num2, sub_result))
logger.debug('Sub: {} - {} = {}'.format(num1, num2, sub_result))

multi_result = multiply(num1, num2)
# print('Multi: {} * {} = {}'.format(num1, num2, multi_result))
# logging.debug('Multi: {} * {} = {}'.format(num1, num2, multi_result))
# logging.warning('Multi: {} * {} = {}'.format(num1, num2, multi_result))
logger.debug('Multi: {} * {} = {}'.format(num1, num2, multi_result))

div_result = divide(num1, num2)
# print('Div: {} / {} = {}'.format(num1, num2, div_result))
# logging.debug('Div: {} / {} = {}'.format(num1, num2, div_result))
# logging.warning('Div: {} / {} = {}'.format(num1, num2, div_result))
logger.debug('Div: {} / {} = {}'.format(num1, num2, div_result))
