import psycopg2
import multiprocessing
import time

username = 'lazebnyi_oleksandr'
password = '123'
database = 'BD_labs'
host = 'localhost'
port = '5432'


def lost_update():
    conn = psycopg2.connect(database=database, user=username, password=password, host=host, port=port)
    cursor = conn.cursor()

    for _ in range(1, 10001):
        cursor.execute("SELECT counter FROM user_counter WHERE user_id = 1")
        counter_row = cursor.fetchone()
        counter = counter_row[0] if counter_row else 0
        counter += 1
        cursor.execute(f"UPDATE user_counter SET counter = {counter} WHERE user_id = 1")
        conn.commit()

    cursor.close()
    conn.close()


def in_place_update():
    conn = psycopg2.connect(database=database, user=username, password=password, host=host, port=port)
    cursor = conn.cursor()

    for _ in range(1, 10001):
        cursor.execute("UPDATE user_counter set counter = counter + 1 where user_id = 1")
        conn.commit()

    cursor.close()
    conn.close()

    print("SQL execution complete.")


def row_level_locking():
    conn = psycopg2.connect(database=database, user=username, password=password, host=host, port=port)
    cursor = conn.cursor()

    for _ in range(1, 10001):
        cursor.execute("SELECT counter FROM user_counter WHERE user_id = 1 FOR UPDATE")
        counter_row = cursor.fetchone()
        counter = counter_row[0] if counter_row else 0

        counter += 1

        cursor.execute(f"UPDATE user_counter SET counter = {counter} WHERE user_id = 1")

        conn.commit()

    cursor.close()
    conn.close()

    print("SQL execution complete.")


def occ():
    conn = psycopg2.connect(database=database, user=username, password=password, host=host, port=port)
    cursor = conn.cursor()

    for _ in range(1, 10001):

        while True:
            cursor.execute("SELECT counter, version FROM user_counter WHERE user_id = 1")
            counter, version = cursor.fetchone()

            counter += 1
            cursor.execute(
                f"UPDATE user_counter set counter = {counter}, version = {version + 1} WHERE user_id = 1 and version = {version}")

            conn.commit()
            count = cursor.rowcount

            if count > 0:
                break

    cursor.close()
    conn.close()

    print("SQL execution complete.")


def clean_table():
    conn = psycopg2.connect(database=database, user=username, password=password, host=host, port=port)
    cursor = conn.cursor()

    cursor.execute("UPDATE user_counter SET counter = 0, version = 0 WHERE user_id = 1")

    conn.commit()

    cursor.close()
    conn.close()

    print("SQL execution complete. Table cleaned successfully")


def show_table():
    conn = psycopg2.connect(database=database, user=username, password=password, host=host, port=port)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM user_counter")

    column_names = [desc[0] for desc in cursor.description]

    # Print column names
    print(" | ".join(column_names))

    rows = cursor.fetchall()

    for row in rows:
        print(" | ".join(str(cell) for cell in row))

    conn.commit()

    cursor.close()
    conn.close()


if __name__ == "__main__":

    options = {
        '1': lost_update,
        '2': in_place_update,
        '3': row_level_locking,
        '4': occ,
        '5': clean_table
    }

    while True:
        print("\nМеню:")
        print("1. Lost update")
        print("2. In-place update")
        print("3. Row-level locking")
        print("4. OCC")
        print("5. Очистити таблицю")
        print("6. Завершити виконання програми")

        choice = input("Оберіть опцію (1/2/3/4/5/6): ")

        if choice == '5':
            clean_table()
            continue
        elif choice == '6':
            break

        try:
            selected_option = options[choice]
        except KeyError:
            print("Помилка: недопустима опція.")
            continue

        print("Ви обрали: ", options[choice].__name__)

        chosen_func = options[choice]

        start_time = time.time()
        processes = []

        for _ in range(10):
            process = multiprocessing.Process(target=chosen_func)
            processes.append(process)
            process.start()

        for process in processes:
            process.join()

        end_time = time.time()
        total_time = end_time - start_time

        print("All processes have finished.")
        print("Total time taken:", total_time, "seconds.")
        print("The table looks like this: ")
        show_table()
