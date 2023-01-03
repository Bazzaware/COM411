class SetColour:
    """
    Sets colours for print() command
    ref: https://stackoverflow.com/questions/287871/how-do-i-print-colored-text-to-the-terminal
    """
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    WARNING = '\033[96m'
    FAIL = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def setup_module(module):
    print(f'\n{SetColour.OKBLUE}Setting up MODULE {format(module.__name__)}{SetColour.ENDC}')


def teardown_module(module):
    print(f'{SetColour.OKBLUE}Tearing down MODULE {format(module.__name__)}{SetColour.ENDC}')


def test_a_function():
    print('Running test function')


class BaseTest:

    def setup_class(cls):
        # pylint: disable=no-self-argument,no-member
        print(f"\n{SetColour.WARNING}setting up CLASS {format(cls.__name__)}{SetColour.ENDC}")

    def teardown_class(cls):
        # pylint: disable=no-self-argument,no-member
        print(f"{SetColour.WARNING}tearing down CLASS {format(cls.__name__)}{SetColour.ENDC}\n")

    def setup_method(self, method):
        print(f"\n{SetColour.FAIL}setting up METHOD {format(method.__name__)}{SetColour.ENDC}")

    def teardown_method(self, method):
        print(f"\n{SetColour.FAIL}tearing down METHOD {format(method.__name__)}{SetColour.ENDC}")


class TestClass1(BaseTest):

    def test_method_1(self):
        print("RUNNING METHOD 1-1")

    def test_method_2(self):
        print("RUNNING METHOD 1-2")


class TestClass2(BaseTest):

    def test_method_1(self):
        print("RUNNING METHOD 2-1")

    def test_method_2(self):
        print("RUNNING METHOD 2-2")

# Phillips, Dusty. Python 3 Object-Oriented Programming: Build robust and maintainable software with object-oriented design patterns in Python 3.8, 3rd Edition . Packt Publishing. Kindle Edition.
