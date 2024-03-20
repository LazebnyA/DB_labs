import psycopg2
import multiprocessing
import time


username = 'lazebnyi_oleksandr'
password = '123'
database = 'BD_labs'
host = 'localhost'
port = '5432'


def execute_sql():
    try:
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

    except psycopg2.Error as e:
        print("Error:", e)


if __name__ == "__main__":
    start_time = time.time()

    processes = []
    for _ in range(10):
        process = multiprocessing.Process(target=execute_sql)
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    end_time = time.time()

    total_time = end_time - start_time

    print("All processes have finished.")
    print("Total time taken:", total_time, "seconds.")