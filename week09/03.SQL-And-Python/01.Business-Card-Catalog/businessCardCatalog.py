import sqlite3


def create_database():
    connection = sqlite3.connect('businessCard.db')
    cursor = connection.cursor()

    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS User(
        id INTEGER PRIMARY KEY UNIQUE NOT NULL,
        full_name VARCHAR(50) UNIQUE NOT NULL,
        email VARCHAR(50) UNIQUE NOT NULL,
        age INTEGER NOT NULL,
        phone VARCHAR(10) NOT NULL,
        additional_info TEXT
        );
        '''
    )

    connection.commit()
    connection.close()


def add_command():
    connection = sqlite3.connect('businessCard.db')
    cursor = connection.cursor()

    name = input('Enter user name: ')
    email = input('Enter email: ')
    age = input('Enter age: ')
    phone = input('Enter phone: ')
    added_info = input('Enter additional info(optional): ')

    if added_info == '':
        added_info = None

    query_string = f'''
    INSERT INTO User(full_name, email, age, phone, additional_info)
      VALUES(?, ?, ?, ?, ?);
    '''

    cursor.execute(query_string, (name, email, age, phone, added_info))

    connection.commit()
    connection.close()


def list_command():
    connection = sqlite3.connect('businessCard.db')
    cursor = connection.cursor()

    cursor.execute(
        '''
        SELECT * FROM User;
        '''
    )
    all_info = cursor.fetchall()

    print(
        '''
                ###################################
                ##########   Contacts  ############
                ###################################
    '''
    )

    for c in all_info:
        print(f'ID: {c[0]}, Email: {c[2]}, Full name: {c[1]}')
    print()

    connection.commit()
    connection.close()


def delete_command():
    connection = sqlite3.connect('businessCard.db')
    cursor = connection.cursor()

    id_of_deleted = input('Enter user id:')

    query_string = f'''
        DELETE FROM User
        WHERE  id = ?;
        '''

    cursor.execute(query_string, id_of_deleted)

    connection.commit()
    connection.close()


def get_command():
    connection = sqlite3.connect('businessCard.db')
    cursor = connection.cursor()

    id = input('Enter user id:')

    cursor.execute(f'''
        SELECT * FROM User
        WHERE id = {id}
    ''')
    user_data = cursor.fetchall()

    print(f'''
Contact info:
#########################################
Id: {user_data[0][0]},
Name: {user_data[0][1]},
Email: {user_data[0][2]},
Age: {user_data[0][3]},
Phone: {user_data[0][4]},
Additional info: {user_data[0][5]}
########################################
        ''')

    connection.commit()
    connection.close()


def help_command():
    print('''
                ######################################
                ############   Options  ##############
                ######################################
                1. `add` - insert new business card
                2. `list` - list all business cards
                3. `delete` - delete a certain business card (`ID` is required)
                4. `get` - display full information for a certain business card
                (`ID` is required)
                5. `help` - list all available options
    ''')
