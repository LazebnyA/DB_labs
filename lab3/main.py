from datetime import datetime

from db import WeatherData, WindData

from sqlalchemy import create_engine, select, func
from sqlalchemy.orm import sessionmaker


def get_record_by_time(records_lst, country, date):
    if not records_lst:
        print("Пусто!")
        return None
    elif len(records_lst) == 1:
        return 0, records_lst[0]

    result_dict = {index: value for index, value in enumerate(records_lst)}

    print(f"Для країни - {country} - є декілька варіантів в цей день ({date}, виберіть потрібний.")
    for i, record in enumerate(records_lst):
        print(f"{i}. Час: {record[7].strftime('%H:%M')}. Локація: {record[2]}.")

    chosen_option = int(input("Обраний час під номером: "))
    return chosen_option, result_dict[chosen_option]


def _get_table(table_name):
    tables_dict = {
        'weather_data': WeatherData.__table__,
        'wind_data': WindData.__table__
    }
    return tables_dict.get(table_name)


class WeatherDatabase:
    def __init__(self, db_url):
        self.engine = create_engine(db_url)
        self.Session = sessionmaker(bind=self.engine)

    def get_min_max_dates(self):
        session = self.Session()
        try:
            min_date = session.query(func.min(WeatherData.last_updated)).scalar()
            max_date = session.query(func.max(WeatherData.last_updated)).scalar()
            return min_date, max_date
        finally:
            session.close()

    def get_records(self, country, date):
        session = self.Session()
        table = WeatherData.__table__
        try:
            query = session.query(table).filter(
                table.c.country == country,
                func.date(table.c.last_updated) == date.date()  # Extract date portion
            )
            records = query.all()
            return records
        finally:
            session.close()

    def get_secondary_data(self, table_name, ids_lst):
        table = _get_table(table_name)
        session = self.Session()

        try:
            query = session.query(table).filter(
                table.c.weather_id.in_(ids_lst)
            )
            records = query.all()
            return records
        finally:
            session.close()


def main():
    db = WeatherDatabase('postgresql://lazebnyi_oleksandr:123@localhost:5432/lab3_db')
    min_last_updated, max_last_updated = db.get_min_max_dates()

    print("Дана програма виводить інформацію про погоду в введеній країні в відповідний час з бази даних")
    print(f"Дані існують лише за період: {min_last_updated} - {max_last_updated}")

    while True:
        try:
            country_input = input("Введіть назву країни: ")
            date_input = datetime.strptime(input("Введіть дату (в форматі YYYY-MM-DD): "), '%Y-%m-%d')

            weather_records = db.get_records(country_input, date_input)
            ids_lst = [record[0] for record in weather_records]
            print(ids_lst)

            record_obj = get_record_by_time(weather_records, country_input, date_input)
            weather_record = record_obj[1]
            record_idx = record_obj[0]

            wind_records = db.get_secondary_data('wind_data', ids_lst)
            print(1)
            wind_record = wind_records[record_idx]

            print("_" * 50)

            print(f"Країна: {weather_record[1]}\n"
                  f"Локація: {weather_record[2]}. Широта = {weather_record[3]}, Довгота = {weather_record[4]}.\n"
                  f"Часова зона: {weather_record[5]}\n"
                  f"Час і дата оновлення (Epoch або Unix формат): {weather_record[6]}\n"
                  f"Час і дата оновлення: {weather_record[7].strftime('%Y-%m-%d %H:%M')}\n"
                  f"Швидкість вітру: {wind_record[1]} km/h\n"
                  f"Напрям вітру (в градусах): {wind_record[2]} deg\n"
                  f"Напрям вітру (загальний): {wind_record[3]} deg\n")

            print("_" * 20)
            print(f"Чи варто виходити на вулицю?")
            if wind_record[-1]:
                print("Так!")
            else:
                print("Ні!")

            additional_input = input("Вивести додаткову інформацію (1 - так, будь-що - ні)?\n")

            if additional_input == '1':
                print("_" * 50)

                print(f"Температура (гр. Цельсію): {weather_record[8]}°C\n"
                      f"Температура (гр. Фаренгейта): {weather_record[9]}°F\n"
                      f"Стан: {weather_record[10]}\n"
                      f"Тиск у мілібарах: {weather_record[11]} mb\n"
                      f"Тиск у дюймах: {weather_record[12]} in\n"
                      f"Кількість опадів у міліметрах: {weather_record[13]} mm\n"
                      f"Кількість опадів у дюймах: {weather_record[14]} in\n"
                      f"Вологість у відсотках: {weather_record[15]}%\n"
                      f"Хмарність у відсотках: {weather_record[16]}%\n"
                      f"Відчутна температура в градусах Цельсія: {weather_record[17]}°C\n"
                      f"Відчутна температура в градусах Фаренгейта: {weather_record[18]}°F\n"
                      f"Видимість в кілометрах: {weather_record[19]} km\n"
                      f"Видимість в милях: {weather_record[20]} mi\n"
                      f"Ультрафіолетовий індекс: {weather_record[21]}\n"
                      f"Порив вітру в милях на годину: {weather_record[22]} mi/h \n"
                      f"Порив вітру в кілометрах на годину: {weather_record[23]} km/h \n"
                      f"Вимірювання якості повітря. Оксид вуглецю: {weather_record[24]}\n"
                      f"Вимірювання якості повітря. Озон: {weather_record[25]}\n"
                      f"Вимірювання якості повітря. Діоксид азоту: {weather_record[26]}\n"
                      f"Вимірювання якості повітря. Діоксид сірки: {weather_record[27]}\n"
                      f"Вимірювання якості повітря. PM2.5: {weather_record[28]}\n"
                      f"Вимірювання якості повітря. PM10: {weather_record[29]}\n"
                      f"Вимірювання якості повітря. US EPA Index: {weather_record[30]}\n"
                      f"Вимірювання якості повітря. GB DEFRA Index: {weather_record[31]}\n"
                      f"Місцевий час сходу сонця: {weather_record[32]}\n"
                      f"Місцевий час заходу сонця: {weather_record[33]}\n"
                      f"Місцевий час сходу місяця: {weather_record[34]}\n"
                      f"Місцевий час заходу місяця: {weather_record[35]}\n"
                      f"Поточна фаза місяця: {weather_record[36]}\n"
                      f"Відсоток освітленості Місяця: {weather_record[37]}%\n"
                      "___________________________________________________________________________________")

            break
        except Exception as e:
            print("Спробуйте ще раз.", e)
            continue


if __name__ == "__main__":
    main()
