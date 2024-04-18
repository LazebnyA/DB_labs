from sqlalchemy import Column, Integer, String, Float, Time, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class WeatherData(Base):
    __tablename__ = "weather_data"

    weather_id = Column(Integer, primary_key=True)
    country = Column(String(255))
    location_name = Column(String(255))
    latitude = Column(Float)
    longitude = Column(Float)
    timezone = Column(String(255))
    last_updated_epoch = Column(Integer)
    last_updated = Column(DateTime)
    temperature_celsius = Column(Float)
    temperature_fahrenheit = Column(Float)
    condition_text = Column(String(255))
    pressure_mb = Column(Float)
    pressure_in = Column(Float)
    precip_mm = Column(Float)
    precip_in = Column(Float)
    humidity = Column(Integer)
    cloud = Column(Integer)
    feels_like_celsius = Column(Float)
    feels_like_fahrenheit = Column(Float)
    visibility_km = Column(Float)
    visibility_miles = Column(Float)
    uv_index = Column(Float)
    gust_mph = Column(Float)
    gust_kph = Column(Float)
    air_quality_Carbon_Monoxide = Column(Float)
    air_quality_Ozone = Column(Float)
    air_quality_Nitrogen_dioxide = Column(Float)
    air_quality_Sulphur_dioxide = Column(Float)
    air_quality_PM25 = Column(Float)
    air_quality_PM10 = Column(Float)
    air_quality_us_epa_index = Column(Integer)
    air_quality_gb_defra_index = Column(Integer)
    sunrise = Column(Time)
    sunset = Column(Time)
    moonrise = Column(Time)
    moonset = Column(Time)
    moon_phase = Column(String(255))
    moon_illumination = Column(Integer)


class WindData(Base):
    __tablename__ = "wind_data"

    wind_id = Column(Integer, primary_key=True)
    country = Column(String(255))

    last_updated_epoch = Column(Integer)
    last_updated = Column(DateTime)
    wind_kph = Column(Float)
    wind_degree = Column(Integer)
    wind_direction = Column(String(3))
    go_outside = Column(Boolean)
