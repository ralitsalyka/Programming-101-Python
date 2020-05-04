import sqlite3


def create_database_table():
    connection = sqlite3.connect('vehicleManager.db')
    cursor = connection.cursor()

    query_script = '''
        CREATE TABLE IF NOT EXISTS BaseUser(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_name VARCHAR(50) UNIQUE NOT NULL,
        email VARCHAR(50) UNIQUE NOT NULL,
        phone_number INTEGER NOT NULL,
        address VARCHAR(50) UNIQUE NOT NULL
        );

        CREATE TABLE IF NOT EXISTS Client(
        base_id INTEGER UNIQUE NOT NULL,
        FOREIGN KEY(base_id) REFERENCES BaseUser(id)
        );

        CREATE TABLE IF NOT EXISTS Mechanic(
        base_id INTEGER UNIQUE NOT NULL,
        title VARCHAR(50) UNIQUE NOT NULL,
        FOREIGN KEY(base_id) REFERENCES BaseUser(id)
        );

        CREATE TABLE IF NOT EXISTS Vehicle(
        id INTEGER PRIMARY KEY UNIQUE NOT NULL,
        category VARCHAR(50) UNIQUE NOT NULL,
        make VARCHAR(50) UNIQUE NOT NULL,
        model VARCHAR(50) UNIQUE NOT NULL,
        register_number VARCHAR(50) UNIQUE NOT NULL,
        gear_box VARCHAR(50) UNIQUE NOT NULL,
        owner INTEGER NOT NULL,
        FOREIGN KEY(owner) REFERENCES Client(base_id)
        );

        CREATE TABLE IF NOT EXISTS Mechanic_services(
        id INTEGER PRIMARY KEY,
        mechanic_id INTEGER NOT NULL,
        service_id INTEGER NOT NULL,
        FOREIGN KEY(mechanic_id) REFERENCES Mechanic(base_id),
        FOREIGN KEY(service_id) REFERENCES Service(id)
        );

        CREATE TABLE IF NOT EXISTS Service(
        id INTEGER PRIMARY KEY UNIQUE NOT NULL,
        name VARCHAR(50) UNIQUE NOT NULL
        );

        CREATE TABLE IF NOT EXISTS RepairHour(
        id INTEGER PRIMARY KEY,
        date VARCHAR(10) NOT NULL,
        start_hour VARCHAR(5) NOT NULL,
        vehicle INTEGER UNIQUE NOT NULL,
        bill REAL UNIQUE NOT NULL,
        mechanic_service INTEGER UNIQUE NOT NULL,
        FOREIGN KEY(vehicle) REFERENCES Vehicle(id),
        FOREIGN KEY(mechanic_service) REFERENCES MechanicService(id)
        );
        '''

    cursor.executescript(query_script)

    connection.commit()
    connection.close()


def main():
    create_database_table()


if __name__ == '__main__':
    main()
