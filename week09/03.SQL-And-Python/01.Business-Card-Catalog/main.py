from businessCardCatalog import *


def main():
    print(
        f'''

        Hello! This is your business card catalog. What would you like?
              (enter "help" to list all available options)
            '''
    )

    command = input('Enter command: ')

    if command == 'help':
        help_command()
        command = input('Enter new command: ')
    if command == 'add':
        add_command()
    if command == 'list':
        list_command()
    if command == 'delete':
        get_command()
        print(f'Enter again the ID you want to delete for sure!!')
        delete_command()
    if command == 'get':
        get_command()


if __name__ == '__main__':
    main()
