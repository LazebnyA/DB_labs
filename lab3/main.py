import csv
from datetime import datetime

from db import WeatherData, WindData

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def main():
    engine = create_engine('postgresql://lazebnyi_oleksandr:123@localhost:5432/lab3_db')

    Session = sessionmaker(bind=engine)
    session = Session()

    with open('GlobalWeatherRepository.csv', 'r') as weather_data:
        reader = csv.DictReader(weather_data)
        for i, row in enumerate(reader):
            last_updated_epoch = int(row['last_updated_epoch'])
            last_updated = datetime.strptime(row['last_updated'], '%Y-%m-%d %H:%M')

            weather_obj = WeatherData(
                weather_id=i,
                country=row['country'],
                location_name=row['location_name'],
                latitude=float(row['latitude']),
                longitude=float(row['longitude']),
                timezone=row['timezone'],
                last_updated_epoch=last_updated_epoch,
                last_updated=last_updated,
                temperature_celsius=float(row['temperature_celsius']),
                temperature_fahrenheit=float(row['temperature_fahrenheit']),
                condition_text=row['condition_text'],
                pressure_mb=float(row['pressure_mb']),
                pressure_in=float(row['pressure_in']),
                precip_mm=float(row['precip_mm']),
                precip_in=float(row['precip_in']),
                humidity=int(row['humidity']),
                cloud=int(row['cloud']),
                feels_like_celsius=float(row['feels_like_celsius']),
                feels_like_fahrenheit=float(row['feels_like_fahrenheit']),
                visibility_km=float(row['visibility_km']),
                visibility_miles=float(row['visibility_miles']),
                uv_index=float(row['uv_index']),
                gust_mph=float(row['gust_mph']),
                gust_kph=float(row['gust_kph']),
                air_quality_Carbon_Monoxide=float(row['air_quality_Carbon_Monoxide']),
                air_quality_Ozone=float(row['air_quality_Ozone']),
                air_quality_Nitrogen_dioxide=float(row['air_quality_Nitrogen_dioxide']),
                air_quality_Sulphur_dioxide=float(row['air_quality_Sulphur_dioxide']),
                air_quality_PM25=float(row['air_quality_PM2.5']),
                air_quality_PM10=float(row['air_quality_PM10']),
                air_quality_us_epa_index=int(row['air_quality_us-epa-index']),
                air_quality_gb_defra_index=int(row['air_quality_gb-defra-index']),
                sunrise=datetime.strptime(row['sunrise'], '%I:%M %p').time(),
                sunset=datetime.strptime(row['sunset'], '%I:%M %p').time(),
                moonrise=None if row['moonrise'] == 'No moonrise' else datetime.strptime(row['moonrise'], '%I:%M %p').time(),
                moonset=None if row['moonset'] == 'No moonset' else datetime.strptime(row['moonset'], '%I:%M %p').time(),
                moon_phase=row['moon_phase'],
                moon_illumination=int(row['moon_illumination'])
            )
            wind_obj = WindData(
                wind_id=i,
                country=row['country'],
                last_updated_epoch=last_updated_epoch,
                last_updated=last_updated,
                wind_mph=float(row['wind_mph']),
                wind_kph=float(row['wind_kph']),
                wind_degree=int(row['wind_degree']),
                wind_direction=row['wind_direction']
            )

            try:
                session.add(weather_obj)
                session.add(wind_obj)
                session.commit()
            except Exception as e:
                session.rollback()
                print(f"Error: {e}")
                continue



if __name__ == "__main__":
    main()
