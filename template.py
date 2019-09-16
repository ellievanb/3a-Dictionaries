import sys, logging, json

#check to make sure we are running the right version of Python
version = (3,7)
assert sys.version_info >= version, "This script requires at least Python {0}.{1}".format(version[0],version[1])

#turn on logging, in case we have to leave ourselves debugging messages
logging.basicConfig(format='[%(filename)s:%(lineno)d] %(message)s', level=logging.DEBUG)
logger = logging.getLogger(__name__)


#if we are running this from the command line, run main
if __name__ == '__main__':

    birthdays = {
        'Maddie Stacey': '09/13/1998',
        'Madison Young': '05/05/1999',
        'Elizabeth VanBuskirk': '06/02/1999',
        }

    print('Welcome to the birthday dictionary. We know the birthdays of:')
    for name in birthdays:
        print(name)

    print('Who\'s birthday do you want to look up?')
    name = input()
    if name in birthdays:
        print ('{}\'s birthday is {}.'.format(name,birthdays[name]))
    else:
        print('Sadly, we don\'t have {}\'s birthday.'.format(name))  