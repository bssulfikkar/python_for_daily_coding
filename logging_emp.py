import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(levelname)s:%(asctime)s:%(name)s:%(message)s')
file_handler = logging.FileHandler('employee.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


#logging.basicConfig(filename='employee.log', level=logging.INFO,format='%(levelname)s:%(asctime)s:%(name)s:%(message)s')


class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last

        # print('Created Employee: {} - {}'.format(self.fullname, self.email))
        # logging.info('Created Employee: {} - {}'.format(self.fullname, self.email))
        logger.info('Created Employee: {} - {}'.format(self.fullname, self.email))

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)


emp1 = Employee('John', 'Smith')
emp2 = Employee('Corey', 'Schafer')
