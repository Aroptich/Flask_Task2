import sqlite3
from datetime import datetime



class Database:
    @staticmethod
    def connect_db(func):
        def wrapper(*args, **kwargs):
            try:
                with sqlite3.connect("sqldb.db") as con:
                    print("successfully connected....")
                    cursor = con.cursor()
                    cursor.execute(func(*args, **kwargs))
                    con.commit()
            except Exception as err:
                print("Connection refused...")
                print(err)
            finally:
                con.close()

        return wrapper

    @staticmethod
    def reading_data(func):
        def wrapper(*args, **kwargs):
            try:
                with sqlite3.connect("sqldb.db") as con:
                    print("successfully connected....")
                    cursor = con.cursor()
                    cursor.execute(func(*args, **kwargs))
                    rows = cursor.fetchall()
                    if len(rows) == 0:
                        print(f'Данных не найдено!')
                        return ''
                    else:
                        return [row[0] for row in rows][0]
                    con.commit()
            except Exception as err:
                print("Connection refused...")
                print(err)
            finally:
                con.close()
        return wrapper

    @staticmethod
    def logger(func):
        def wrapper(*args, **kwargs):
            try:
                with open('log.txt', 'a', encoding='utf-8') as file:
                    query = func(*args, **kwargs)
                    file.writelines(f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
                    file.writelines(f"{'=' * 35}\n")
                    file.writelines(f'{query}\n')
                    file.writelines(f"{'=' * 35}\n")
                    return query
            except Exception as err:
                print(err)

        return wrapper

    @connect_db
    @logger
    def create_table(self, table_name: str, **dict_data: dict) -> str:
        try:
            columns_name = [keys for keys in dict_data]
            type_data = [dict_data[keys] for keys in dict_data]
            res = ',\n'.join([' '.join(i) for i in zip(columns_name, type_data)])
            return f"CREATE TABLE IF NOT EXISTS {table_name} \n({res});"
        except Exception as err:
            print(err)

    @connect_db
    @logger
    def insert_data(self, table_name: str, data: dict) -> str:
        try:
            columns_name = ','.join([keys for keys in data])
            values = ','.join([str(f"'{data[keys]}'") for keys in data])
            return f"INSERT INTO {table_name} ({columns_name}) \nVALUES ({values});"
        except Exception as err:
            print(err)

    @reading_data
    @logger
    def query_email(self, table_name: str, email: str) -> str:
        return f"SELECT email\nFROM {table_name}\nWHERE email='{email}';"


# if __name__ == '__main__':
#     db = Database()
#     db.create_table('User', id='int auto_increment primary key',
#                     email='varchar(40)',
#                     password='varchar(40)')
#     db.insert_data('User', {'email': '546@mail.ru', 'password': '123'})
#     print(db.query_email())
